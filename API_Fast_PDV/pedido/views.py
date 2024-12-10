from rest_framework.decorators import action
from rest_framework import viewsets, mixins
from .models import FormaPagamento, Pedido, ClientePedido, FormaPagamentoPedido, ProdutoPedido
from usuarios.models import Cliente, Genero, Estado
from produto.models import Produto, Categoria
from .serializers import FormaPagamentoSerializer, PedidoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework import status
from django.db import transaction
from reportlab.lib.units import cm
import json
from rest_framework.permissions import IsAuthenticated
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import io
from io import BytesIO
from django.conf import settings
import os

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size' 

class FormaPagamentoViewSet(mixins.ListModelMixin, 
                     viewsets.GenericViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer
    #pagination_class = CustomPagination

class PedidoViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all().order_by('-criacao')
    serializer_class = PedidoSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        pedido_json = request.data

        cliente_data = pedido_json.get('cliente', {})
        if len(cliente_data) > 0:
            cliente_obj = Cliente.objects.get(pk=cliente_data.get('cliente_id'))

            cliente_pedido = ClientePedido.objects.create(
                cliente_id=cliente_obj,
                cpf=cliente_data.get('cpf'),
                nome=cliente_data.get('nome'),
                data_nascimento=cliente_data.get('data_nascimento'),
                genero_id=cliente_data.get('genero'), 
                cep=cliente_data.get('cep'),
                endereco=cliente_data.get('endereco'),
                numero=cliente_data.get('numero'),
                bairro=cliente_data.get('bairro'),
                cidade=cliente_data.get('cidade'),
                uf_estado_id=cliente_data.get('uf_estado'),
                email=cliente_data.get('email'),
                tel_celular=cliente_data.get('tel_celular')
            )
        else:
            cliente_data = 0
            cliente_pedido = 0

        valores_pagos = pedido_json.get("valores", {})

        pedido_data = {
            'json_pedido': pedido_json,
            'cliente_pedido_id': cliente_pedido.cliente_id if cliente_pedido != 0 else None,
            'valor_total_pago': valores_pagos.get('valor_total'),
            'valor_total_desconto': valores_pagos.get('valor_desconto')
        }
        serializer = self.get_serializer(data=pedido_data)
        serializer.is_valid(raise_exception=True)
        pedido = serializer.save()

        formas_pagamento_data = pedido_json.get('formas_pagamento', [])

        for forma_data in formas_pagamento_data:
            forma_pagamento = FormaPagamento.objects.get(pk=forma_data.get('forma_pagamento_id'))

            FormaPagamentoPedido.objects.create(
                pedido_id=pedido,
                forma_pagamento_id=forma_pagamento,
                descricao_forma=forma_data.get('descricao_forma'),
                numero_parcela=forma_data.get('numero_parcela'),
                valor_forma=forma_data.get('valor_forma'),
                troco=forma_data.get('valor_troco')
            )

        produtos_pedido_data = pedido_json.get('produtos', [])

        for produto_data in produtos_pedido_data:

            produto = Produto.objects.get(pk=produto_data.get('produto_id'))
            nome_categoria = Categoria.objects.get(nome=produto_data.get('categoria'))

            ProdutoPedido.objects.create(
                pedido_id=pedido,
                produto_id=produto,
                quantidade=1,
                nome=produto_data.get('nome'),
                descricao=produto_data.get('descricao'),
                preco_venda=produto_data.get('preco_venda'),
                preco_custo=produto_data.get('preco_custo'),
                preco_desconto=produto_data.get('preco_desconto'),
                porcentagem_desconto=produto_data.get('porcentagem_desconto'),
                codigo_barras=produto_data.get('codigo_barras'),
                estoque=produto_data.get('estoque'),
                sku=produto_data.get('sku'),
                categoria=nome_categoria
            )

            produto.estoque -= 1
            produto.save()

        response_data = serializer.data
        response_data['pedido_id'] = pedido.pedido_id

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def gerar_nota_fiscal(self, request, pk=None):
        pedido = self.get_object()
        pedido_json=pedido.json_pedido
        buffer = gerar_pdf_pedido(pedido_json, pedido)
        return FileResponse(buffer, as_attachment=True, filename=f"nota_fiscal_pedido_{pk}.pdf")
    


def gerar_pdf_pedido(pedido_data, id_pedido):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)

    cliente = pedido_data.get("cliente", {})
    valores = pedido_data.get("valores", {})
    produtos = pedido_data.get("produtos", [])
    pagamentos = pedido_data.get("formas_pagamento", [])

    #Calculando altura
    altura_minima = 9.5

    altura_cliente = 1.4 if len(cliente) > 0 else 0
    altura_valores = 0.38 if valores.get('valor_troco') > 0 else 0
    altura_produtos = 0.38 * len(produtos)
    altura_pagamentos = 0.38 * len(pagamentos)
    
    largura = 8 * cm
    altura = (altura_minima+altura_cliente+altura_valores+altura_produtos+altura_pagamentos) * cm
    
    # Sem cliente 10 cm
    # Com cliente 11.5 cm
    # cliente = 1,5cm
    # linha = 0,38cm

    pdf = canvas.Canvas(buffer, pagesize=(largura, altura))
    pdf.setFont("Times-Roman", 8)

    logo = os.path.join(settings.MEDIA_ROOT, 'fast_logo_black_cupom.png')

    margem_esquerda = 7
    margem_topo = altura - 2 * cm
    margem_inferior = 2 * cm
    espacamento = 9
    y_position = margem_topo
    max_caracteres = 80
    
    caracteres_por_linha = 33
    largura_coluna_nome = 5 * cm 
    largura_coluna_valor = 2.5 * cm


    pdf.drawImage(logo, x=5, y=y_position-8, width=70, height=70)
    y_position = y_position + 40

    pdf.drawString(82, y_position, f"FAST PDV EMPRESA FICTICIA.LTDA")
    y_position -= espacamento 
    pdf.drawString(82, y_position, f"R. TESTE DO TESTE, 9999")
    y_position -= espacamento 
    pdf.drawString(82, y_position, f"99.999-999 CIDADE - UF")
    y_position -= espacamento 
    pdf.drawString(82, y_position, f"CNPJ: 99.999.999/0009-09")
    y_position -= espacamento 
    pdf.drawString(82, y_position, f"IE: 99999999-99")
    
    y_position -= espacamento*2
    
    data_pedido = pedido_data.get('data_pedido')
    # 2024-10-27T12:51:59.921274-03:00

    pdf.drawString(margem_esquerda, y_position, "--------------------------------------------------------------------------------")
    y_position -= espacamento
    pdf.drawString(margem_esquerda, y_position, f"{data_pedido[8:10]}/{data_pedido[5:7]}/{data_pedido[0:4]} {data_pedido[11:19]}")
    pdf.drawRightString(margem_esquerda+213, y_position, f"Pedido Nº: {id_pedido}")
    y_position -= espacamento
    pdf.drawString(margem_esquerda, y_position, "--------------------------------------------------------------------------------")
    y_position -= espacamento

    if len(cliente)>0:
        pdf.drawString(margem_esquerda, y_position, f"CPF: {cliente.get('cpf')}")
        y_position -= espacamento
        pdf.drawString(margem_esquerda, y_position, f"NOME: {cliente.get('nome')}")
        y_position -= espacamento
        pdf.drawString(margem_esquerda, y_position, f"END.: {cliente.get('endereco')}, {cliente.get('numero')}")
        y_position -= espacamento
        pdf.drawString(margem_esquerda, y_position, f"BAIRO: {cliente.get('bairro')}, CEP:{cliente.get('cep')}")
        y_position -= espacamento
        pdf.drawString(margem_esquerda, y_position, f"CIDADE: {cliente.get('cidade')}, {cliente.get('uf_estado')}")
        y_position -= espacamento
    else:
        pdf.drawString(margem_esquerda, y_position, f"*CLIENTE NÃO IDENTIFICADO")
        y_position -= espacamento

    pdf.drawString(margem_esquerda, y_position, "--------------------------------------------------------------------------------")
    y_position -= espacamento
    pdf.setFont("Times-Roman", 10)
    pdf.drawString(margem_esquerda, y_position-1, "                         CUPOM NÃO FISCAL                            ")
    pdf.setFont("Times-Roman", 8)
    y_position -= espacamento
    pdf.drawString(margem_esquerda, y_position, "--------------------------------------------------------------------------------")
    y_position -= espacamento
    pdf.drawString(margem_esquerda, y_position, "CÓDIGO -------- DESCRICAO --------------------------- SUBTOAL")
    y_position -= espacamento

    for produto in produtos:
        codigo_barras = f"{produto.get('codigo_barras')}"
        nome_produto = produto.get("nome", "")
        valor_produto = f"R$ {produto.get('preco_venda').replace('.',',')}"

        pdf.drawString(margem_esquerda, y_position, codigo_barras)

        if len(nome_produto) > caracteres_por_linha:
            nome_produto_curto = nome_produto[:caracteres_por_linha - 3] + '...'
        else:
            nome_produto_curto = nome_produto.ljust(caracteres_por_linha)

        pdf.drawString(margem_esquerda+57, y_position, nome_produto_curto)

        x_pos_valor = largura - largura_coluna_valor
        pdf.drawRightString(margem_esquerda+213, y_position, valor_produto)

        y_position -= espacamento
        if y_position <= 2 * cm:
            pdf.showPage()
            y_position = margem_topo

    if y_position <= margem_inferior:
        pdf.showPage()
        y_position = margem_topo

    y_position -= espacamento   
    pdf.drawString(margem_esquerda, y_position, f"Quantidade total de itens: ")
    pdf.drawRightString(margem_esquerda+213, y_position, f"{len(produtos)} UND")

    y_position -= espacamento   
    pdf.drawString(margem_esquerda, y_position, f"Subtotal:")
    valor_subtotal = str(valores.get('valor_subtotal')).replace(".", ",") if "." in str(valores.get('valor_subtotal')) else f"{valores.get('valor_subtotal')},00"
    pdf.drawRightString(margem_esquerda+213, y_position, f"R$ {valor_subtotal}")

    y_position -= espacamento   
    pdf.drawString(margem_esquerda, y_position, f"Desconto:")
    valor_desconto = str(valores.get('valor_desconto')).replace(".", ",") if "." in str(valores.get('valor_desconto')) else f"{valores.get('valor_desconto')},00"
    pdf.drawRightString(margem_esquerda+213, y_position, f"- R$ {valor_desconto}")

    y_position -= espacamento   
    pdf.drawString(margem_esquerda, y_position, f"Valor Total:")
    valor_total = str(valores.get('valor_total')).replace(".", ",") if "." in str(valores.get('valor_total')) else f"{valores.get('valor_total')},00"
    pdf.drawRightString(margem_esquerda+213, y_position, f"R$ {valor_total}")

    if valores.get('valor_troco') > 0:
        y_position -= espacamento   
        pdf.drawString(margem_esquerda, y_position, f"Troco:")
        valor_troco = str(valores.get('valor_troco')).replace(".", ",") if "." in str(valores.get('valor_troco')) else f"{valores.get('valor_troco')},00"
        pdf.drawRightString(margem_esquerda+213, y_position, f"R$ {valor_troco}")
    


    y_position -= espacamento*2
    pdf.drawString(margem_esquerda, y_position, "FORMA PAGAMENTO")
    pdf.drawString(margem_esquerda+162, y_position, "VALOR PAGO")
    y_position -= espacamento

    for pagamento in pagamentos:

        if pagamento.get('numero_parcela') == 1:
            numero_parcela = 'A Vista'
        else:
            numero_parcela = f"Parcelado {pagamento.get('numero_parcela')}X"

        descricao = f"{pagamento.get('descricao_forma')} {numero_parcela}"
        valor_forma = f"R$ {pagamento.get('valor_forma')}"
        valor_forma = str(valor_forma).replace(".", ",") if "." in str(valor_forma) else f"{valor_forma},00"
        
        if len(descricao) > caracteres_por_linha:
            descricao_ajustada = descricao[:caracteres_por_linha - 3] + '...'
        else:
            descricao_ajustada = descricao.ljust(caracteres_por_linha)

        pdf.drawString(margem_esquerda, y_position, descricao_ajustada)
        pdf.drawRightString(margem_esquerda+213, y_position, valor_forma)


        y_position -= espacamento
        if y_position <= 2 * cm:
            pdf.showPage()
            y_position = margem_topo

    y_position -= espacamento*2.5
    pdf.drawString(margem_esquerda, y_position-1, "                      OBRIGADO PELA PREFERÊNCIA!                         ")


    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer