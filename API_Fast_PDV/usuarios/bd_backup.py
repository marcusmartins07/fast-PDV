from .models import Cliente, Estado, Genero
from produto.models import Categoria, Produto
from pedido.models import FormaPagamento
from django.contrib.auth.models import User

def insert_generos():
    generos = [
        {'id_genero': 'M', 'genero': 'Masculino'},
        {'id_genero': 'F', 'genero': 'Feminino'},
        {'id_genero': 'I', 'genero': 'Indefinido'}
    ]

    for genero in generos:
        Genero.objects.create(
            id_genero = genero['id_genero'],
            genero = genero['genero']
        )

def insert_estados():
    estados = [
        {'uf': 'AC', 'estado': 'Acre'}, {'uf': 'AL', 'estado': 'Alagoas'}, {'uf': 'AP', 'estado': 'Amapá'}, {'uf': 'AM', 'estado': 'Amazonas'},
        {'uf': 'BA', 'estado': 'Bahia'}, {'uf': 'CE', 'estado': 'Ceará'}, {'uf': 'DF', 'estado': 'Distrito Federal'},
        {'uf': 'ES', 'estado': 'Espírito Santo'}, {'uf': 'GO', 'estado': 'Goiás'}, {'uf': 'MA', 'estado': 'Maranhão'},
        {'uf': 'MT', 'estado': 'Mato Grosso'}, {'uf': 'MS', 'estado': 'Mato Grosso do Sul'}, {'uf': 'MG', 'estado': 'Minas Gerais'},
        {'uf': 'PA', 'estado': 'Pará'}, {'uf': 'PB', 'estado': 'Paraíba'}, {'uf': 'PR', 'estado': 'Paraná'}, {'uf': 'PE', 'estado': 'Pernambuco'},
        {'uf': 'PI', 'estado': 'Piauí'}, {'uf': 'RJ', 'estado': 'Rio de Janeiro'}, {'uf': 'RN', 'estado': 'Rio Grande do Norte'},
        {'uf': 'RS', 'estado': 'Rio Grande do Sul'}, {'uf': 'RO', 'estado': 'Rondônia'}, {'uf': 'RR', 'estado': 'Roraima'},
        {'uf': 'SC', 'estado': 'Santa Catarina'}, {'uf': 'SP', 'estado': 'São Paulo'}, {'uf': 'SE', 'estado': 'Sergipe'}, {'uf': 'TO', 'estado': 'Tocantins'}
    ]

    for estado in estados:
        Estado.objects.create(
            uf = estado['uf'],
            estado = estado['estado']
        )

def insert_clientes():
    clientes = [
        {
            'cpf': '12345678901',
            'nome': 'João da Silva',
            'data_nascimento': '1980-05-10',
            'genero': 'M',
            'cep': '01001000',
            'endereco': 'Rua das Flores',
            'numero': '123',
            'bairro': 'Centro',
            'cidade': 'São Paulo',
            'uf_estado': 'SP',
            'email': 'joao.silva@example.com',
            'tel_celular': '11999999999',
        },
        {
            'cpf': '23456789012',
            'nome': 'Maria Souza',
            'data_nascimento': '1992-03-22',
            'genero': 'F',
            'cep': '20020030',
            'endereco': 'Avenida Brasil',
            'numero': '456',
            'bairro': 'Jardim América',
            'cidade': 'Rio de Janeiro',
            'uf_estado': 'RJ',
            'email': 'maria.souza@example.com',
            'tel_celular': '21988888888',
        },
        {
            'cpf': '34567890123',
            'nome': 'Carlos Pereira',
            'data_nascimento': '1975-12-15',
            'genero': 'M',
            'cep': '30110001',
            'endereco': 'Rua Augusta',
            'numero': '789',
            'bairro': 'Savassi',
            'cidade': 'Belo Horizonte',
            'uf_estado': 'MG',
            'email': 'carlos.pereira@example.com',
            'tel_celular': '31977777777',
        },
        {
            'cpf': '45678901234',
            'nome': 'Ana Clara Lima',
            'data_nascimento': '1990-07-08',
            'genero': 'F',
            'cep': '40010010',
            'endereco': 'Rua Direita',
            'numero': '321',
            'bairro': 'Pelourinho',
            'cidade': 'Salvador',
            'uf_estado': 'BA',
            'email': 'ana.clara@example.com',
            'tel_celular': '71966666666',
        },
        {
            'cpf': '56789012345',
            'nome': 'Bruno Fernandes',
            'data_nascimento': '1985-02-14',
            'genero': 'M',
            'cep': '60020020',
            'endereco': 'Avenida Beira Mar',
            'numero': '543',
            'bairro': 'Meireles',
            'cidade': 'Fortaleza',
            'uf_estado': 'CE',
            'email': 'bruno.fernandes@example.com',
            'tel_celular': '85955555555',   
        },
        {
            'cpf': '67890123456',
            'nome': 'Camila Ribeiro',
            'data_nascimento': '1995-10-25',
            'genero': 'I',
            'cep': '70040040',
            'endereco': 'Setor Comercial',
            'numero': '654',
            'bairro': 'Asa Norte',
            'cidade': 'Brasília',
            'uf_estado': 'DF',
            'email': 'camila.ribeiro@example.com',
            'tel_celular': '61944444444',
        },
        {
            'cpf': '78901234567',
            'nome': 'Diego Oliveira',
            'data_nascimento': '1988-09-18',
            'genero': 'I',
            'cep': '80030030',
            'endereco': 'Rua XV de Novembro',
            'numero': '987',
            'bairro': 'Centro',
            'cidade': 'Curitiba',
            'uf_estado': 'PR',
            'email': 'diego.oliveira@example.com',
            'tel_celular': '41933333333',
        },
        {
            'cpf': '89012345678',
            'nome': 'Eduarda Santos',
            'data_nascimento': '1987-06-29',
            'genero': 'F',
            'cep': '90050050',
            'endereco': 'Avenida Borges',
            'numero': '852',
            'bairro': 'Cidade Baixa',
            'cidade': 'Porto Alegre',
            'uf_estado': 'RS',
            'email': 'eduarda.santos@example.com',
            'tel_celular': '51922222222',
        },
        {
            'cpf': '90123456789',
            'nome': 'Fernando Gomes',
            'data_nascimento': '1993-04-03',
            'genero': 'M',
            'cep': '36060060',
            'endereco': 'Rua Halfeld',
            'numero': '159',
            'bairro': 'Centro',
            'cidade': 'Juiz de Fora',
            'uf_estado': 'MG',
            'email': 'fernando.gomes@example.com',
            'tel_celular': '32911111111',
        },
        {
            'cpf': '01234567890',
            'nome': 'Gabriela Silva',
            'data_nascimento': '1998-11-11',
            'genero': 'F',
            'cep': '11060060',
            'endereco': 'Avenida Ana Costa',
            'numero': '753',
            'bairro': 'Gonzaga',
            'cidade': 'Santos',
            'uf_estado': 'SP',
            'email': 'gabriela.silva@example.com',
            'tel_celular': '13900000000',
        }
    ]       
    for cliente in clientes:

        genero = Genero.objects.get(id_genero=cliente['genero'])

        estadoUF = Estado.objects.get(uf=cliente['uf_estado'])

        Cliente.objects.create(
            cpf = cliente['cpf'],
            nome = cliente['nome'],
            data_nascimento = cliente['data_nascimento'],
            genero = genero,
            cep = cliente['cep'],
            endereco = cliente['endereco'],
            numero = cliente['numero'],
            bairro =cliente['bairro'],
            cidade = cliente['cidade'],
            uf_estado = estadoUF,
            email = cliente['email'],
            tel_celular =cliente['tel_celular'],
        )



def insert_categorias_produto():
    categorias = [
        
    {'id': '0001', 'nome': 'Frescos'},
    {'id': '0002', 'nome': 'Carnes e Peixes'},
    {'id': '0003', 'nome': 'Frios e Embutidos'},
    {'id': '0004', 'nome': 'Pães e Massas'},
    {'id': '0005', 'nome': 'Cereais e Grãos'},
    {'id': '0006', 'nome': 'Laticínios'},
    {'id': '0007', 'nome': 'Congelados'},
    {'id': '0008', 'nome': 'Doces e Sobremesas'},
    {'id': '0009', 'nome': 'Bebidas Alcoólicas'},
    {'id': '0010', 'nome': 'Refrigerantes e Sucos'},
    {'id': '0011', 'nome': 'Água'},
    {'id': '0012', 'nome': 'Bebidas Energéticas e Isotônicas'},
    {'id': '0013', 'nome': 'Café e Chá'},
    {'id': '0014', 'nome': 'Produtos para o Corpo'},
    {'id': '0015', 'nome': 'Cuidado Capilar'},
    {'id': '0016', 'nome': 'Cuidado Bucal'},
    {'id': '0017', 'nome': 'Cuidados Femininos'},
    {'id': '0018', 'nome': 'Perfumes e Cosméticos'},
    {'id': '0019', 'nome': 'Produtos de Limpeza'},
    {'id': '0020', 'nome': 'Utensílios de Limpeza'},
    {'id': '0021', 'nome': 'Papelaria e Descartáveis'},
    {'id': '0022', 'nome': 'Produtos para Lavanderia'},
    {'id': '0023', 'nome': 'Rações e Petiscos'},
    {'id': '0024', 'nome': 'Higiene para Animais'},
    {'id': '0025', 'nome': 'Acessórios para Animais'},
    {'id': '0026', 'nome': 'Medicamentos OTC (sem prescrição)'},
    {'id': '0027', 'nome': 'Suplementos Alimentares'},
    {'id': '0028', 'nome': 'Produtos Naturais'},
    {'id': '0029', 'nome': 'Fraldas'},
    {'id': '0030', 'nome': 'Alimentação Infantil'},
    {'id': '0031', 'nome': 'Higiene Infantil'},
    {'id': '0032', 'nome': 'Eletrodomésticos e Utensílios Domésticos'},
    {'id': '0033', 'nome': 'Material Escolar'},
    {'id': '0034', 'nome': 'Itens Sazonais'},
    {'id': '0035', 'nome': 'Acessórios Automotivos'},
    {'id': '0036', 'nome': 'Produtos para Limpeza de Carro'},
    {'id': '0037', 'nome': 'Maquiagem'},
    {'id': '0038', 'nome': 'Cremes e Tratamentos'},
    {'id': '0039', 'nome': 'Esmaltes e Acessórios para Unhas'},
    {'id': '0040', 'nome': 'Pães e Bolos'},
    {'id': '0041', 'nome': 'Biscoitos e Bolachas'},
    {'id': '0042', 'nome': 'Carnes Bovinas'},
    {'id': '0043', 'nome': 'Carnes Suínas'},
    {'id': '0044', 'nome': 'Aves e Peixes'},
    ]

    for categoria in categorias:
        Categoria.objects.create(
            codigo_categoria = categoria['id'],
            nome = categoria['nome']
        )



def insert_produtos():
    produtos = [
        {
            'nome': 'Tomate',
            'descricao': 'Tomate fresco e orgânico',
            'preco_venda': 3.50,
            'preco_custo': 2.00,
            'codigo_barras': '0123456789012',
            'estoque': 50,
            'sku': '000189012',
            'categoria': '0001',
        },
        {
            'nome': 'Alface',
            'descricao': 'Alface americana',
            'preco_venda': 2.00,
            'preco_custo': 1.50,
            'codigo_barras': '0123456789013',
            'estoque': 50,
            'sku': '000104013',
            'categoria': '0001',
        },
        {
            'nome': 'Frango Inteiro',
            'descricao': 'Frango caipira',
            'preco_venda': 15.00,
            'preco_custo': 12.00,
            'codigo_barras': '0123456789014',
            'estoque': 50,
            'sku': '000204014',
            'categoria': '0002',
        },
        {
            'nome': 'Salmão',
            'descricao': 'Salmão fresco',
            'preco_venda': 45.00,
            'preco_custo': 35.00,
            'codigo_barras': '0123456789015',
            'estoque': 50,
            'sku': '000204015',
            'categoria': '0002',
        },
        {
            'nome': 'Leite Integral',
            'descricao': 'Leite integral de 1 litro',
            'preco_venda': 4.50,
            'preco_custo': 3.00,
            'codigo_barras': '0123456789016',
            'estoque': 50,
            'sku': '000304016',
            'categoria': '0003',
        },
        {
            'nome': 'Queijo Prato',
            'descricao': 'Queijo prato fatiado',
            'preco_venda': 25.00,
            'preco_custo': 18.00,
            'codigo_barras': '0123456789017',
            'estoque': 50,
            'sku': '000304017',
            'categoria': '0003',
        },
        {
            'nome': 'Pão Francês',
            'descricao': 'Pão francês quentinho',
            'preco_venda': 0.50,
            'preco_custo': 0.30,
            'codigo_barras': '0123456789018',
            'estoque': 50,
            'sku': '000404018',
            'categoria': '0004',
        },
        {
            'nome': 'Bolo de Chocolate',
            'descricao': 'Bolo de chocolate com cobertura',
            'preco_venda': 15.00,
            'preco_custo': 10.00,
            'codigo_barras': '0123456789019',
            'estoque': 50,
            'sku': '000404019',
            'categoria': '0004',
        },
        {
            'nome': 'Refrigerante Lata',
            'descricao': 'Refrigerante sabor cola',
            'preco_venda': 4.00,
            'preco_custo': 2.50,
            'codigo_barras': '0123456789020',
            'estoque': 50,
            'sku': '000504020',
            'categoria': '0005',
        },
        {
            'nome': 'Suco Natural',
            'descricao': 'Suco natural de laranja',
            'preco_venda': 6.00,
            'preco_custo': 4.00,
            'codigo_barras': '0123456789021',
            'estoque': 50,
            'sku': '000504021',
            'categoria': '0005',
        },
        {
            'nome': 'Detergente',
            'descricao': 'Detergente para lavar louça',
            'preco_venda': 2.50,
            'preco_custo': 1.50,
            'codigo_barras': '0123456789022',
            'estoque': 50,
            'sku': '000604022',
            'categoria': '0006',
        },
        {
            'nome': 'Desinfetante',
            'descricao': 'Desinfetante multiuso',
            'preco_venda': 8.00,
            'preco_custo': 5.00,
            'codigo_barras': '0123456789023',
            'estoque': 50,
            'sku': '000604023',
            'categoria': '0006',
        },
        {
            'nome': 'Peixe Congelado',
            'descricao': 'Peixe congelado para fritar',
            'preco_venda': 30.00,
            'preco_custo': 22.00,
            'codigo_barras': '0123456789024',
            'estoque': 50,
            'sku': '000704024',
            'categoria': '0007',
        },
        {
            'nome': 'Sopa Congelada',
            'descricao': 'Sopa de legumes congelada',
            'preco_venda': 10.00,
            'preco_custo': 7.00,
            'codigo_barras': '0123456789025',
            'estoque': 50,
            'sku': '000704025',
            'categoria': '0007',
        },
        {
            'nome': 'Arroz',
            'descricao': 'Arroz branco tipo 1',
            'preco_venda': 5.00,
            'preco_custo': 3.50,
            'codigo_barras': '0123456789026',
            'estoque': 50,
            'sku': '000804026',
            'categoria': '0008',
        },
        {
            'nome': 'Feijão Preto',
            'descricao': 'Feijão preto em grãos',
            'preco_venda': 7.00,
            'preco_custo': 4.00,
            'codigo_barras': '0123456789027',
            'estoque': 50,
            'sku': '000804027',
            'categoria': '0008',
        },
        {
            'nome': 'Chocolate ao Leite',
            'descricao': 'Chocolate ao leite',
            'preco_venda': 5.00,
            'preco_custo': 3.00,
            'codigo_barras': '0123456789028',
            'estoque': 50,
            'sku': '000904028',
            'categoria': '0009',
        },
        {
            'nome': 'Bala de Goma',
            'descricao': 'Bala de goma sortida',
            'preco_venda': 3.00,
            'preco_custo': 2.00,
            'codigo_barras': '0123456789029',
            'estoque': 50,
            'sku': '000904029',
            'categoria': '0009',
        },
        {
            'nome': 'Maçã',
            'descricao': 'Maçã fresca',
            'preco_venda': 1.00,
            'preco_custo': 0.70,
            'codigo_barras': '0123456789030',
            'estoque': 50,
            'sku': '001004030',
            'categoria': '0010',
        },
        {
            'nome': 'Teste com nome maior de produto',
            'descricao': 'Teste com descrição maior de produto',
            'preco_venda': 999.99,
            "preco_desconto": "250.00",
            "porcentagem_desconto": 25,
            'preco_custo': 0.80,
            'codigo_barras': '0123456789031',
            'estoque': 50,
            'sku': '001004031',
            'categoria': '0010',
        },
        {
            "nome": "Teste com nome maior de produto agora ainda maior",
            "descricao": "Teste com nome maior de produto agora ainda maior",
            "preco_venda": "50.00",
            "preco_desconto": "25.00",
            "porcentagem_desconto": 50,
            "preco_custo": "0.80",
            "codigo_barras": "0123456789033",
            "estoque": 50,
            "sku": "001004033",
            "categoria": "0010",
            "status": "ativo"
        },
        {
            "nome": "Teste com nome maior de produto agora sim",
            "descricao": "Teste com descrição maior de produto agora sim",
            "preco_venda": "999.99",
            "preco_desconto": "230.00",
            "porcentagem_desconto": 23,
            "preco_custo": "0.80",
            "codigo_barras": "0123456789034",
            "estoque": 50,
            "sku": "001004034",
            "categoria": "0010",
            "status": "ativo"
        }
    ]

    for produto in produtos:

        categoria = Categoria.objects.get(codigo_categoria=produto['categoria'])

        Produto.objects.create(
            nome = produto['nome'],
            descricao = produto['descricao'],
            preco_venda = produto['preco_venda'],
            preco_custo = produto['preco_custo'],
            codigo_barras = produto['codigo_barras'],
            estoque = produto['estoque'],
            sku = produto['sku'],
            categoria = categoria,
        )

def insert_forma_pagamento():
    formas = [
        {'descricao_forma': 'Dinheiro', 'numero_parcela': 1}, 
        {'descricao_forma': 'Débito', 'numero_parcela': 1}, 
        {'descricao_forma': 'Crédito', 'numero_parcela': 10}, 
        {'descricao_forma': 'Pix', 'numero_parcela': 1}, 
    ]

    for forma in formas:
        FormaPagamento.objects.create(
            descricao_forma = forma['descricao_forma'],
            numero_parcela = forma['numero_parcela'],
        )

senha = '1234'
def insert_operadores():
    operadores = [
        {'username': '1234', 'first_name': 'Jorge', 'last_name': 'Cardoso', 'is_active': '1', 'is_staff': '1'},
        {'username': '2345', 'first_name': 'Alberto', 'last_name': 'Nogueira', 'is_active': '1', 'is_staff': '1'},
        {'username': '3456', 'first_name': 'Geovana', 'last_name': 'Santos', 'is_active': '1', 'is_staff': '1'},
    ]
    for operador in operadores:
        User.objects.create_user(
            password = senha,
            username = operador['username'],
            first_name = operador['first_name'],
            last_name = operador['last_name'],
            is_active = operador['is_active'],
            is_staff = operador['is_staff']
        )

def insert_bd():
    insert_generos()
    print('Generos inseridos com sucesso')
    insert_estados()
    print('Estados inseridos com sucesso')
    insert_clientes()
    print('Clientes inseridos com sucesso')
    insert_categorias_produto()
    print('Categorias de produto inseridos com sucesso')
    insert_produtos()
    print('Produtos inseridos com sucesso')
    insert_forma_pagamento()
    print('Formas de pagamento inseridos com sucesso')
    insert_operadores()
    print('Operadores inseridos com sucesso')
    