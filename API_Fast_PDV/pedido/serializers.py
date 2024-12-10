from rest_framework import serializers
from .models import FormaPagamento, Pedido, ClientePedido
from usuarios.models import Cliente

class FormaPagamentoSerializer(serializers.ModelSerializer): 

    class Meta:
        model = FormaPagamento
        fields = (
            'forma_pagamento_id',
            'descricao_forma',
            'numero_parcela',  
        )

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('pedido_id',
                  'json_pedido',
                  'valor_total_pago',
                  'valor_total_desconto')

    def create(self, validated_data):
        json_pedido = validated_data.get('json_pedido')

        valores_pagos = json_pedido.get("valores", {})
        
        valor_total_pago = valores_pagos.get('valor_total')
        valor_total_desconto = valores_pagos.get('valor_desconto')

        '''
         cliente_data = json_pedido.get('cliente', {})
        if len(cliente_data) > 0:
            print(cliente_data.get('cliente_id'))
            cliente_pedido = ClientePedido.objects.get(pk=cliente_data.get('cliente_id'))
        else:
            cliente_pedido = None
        '''
        
        return Pedido.objects.create(
            json_pedido=json_pedido,
            valor_total_pago=valor_total_pago,
            valor_total_desconto=valor_total_desconto,
            cliente_pedido_id=None
        )