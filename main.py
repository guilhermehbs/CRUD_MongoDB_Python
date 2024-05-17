from models.connection_options.connection import DBConnection
from models.repository.IDelivery_repository import IDeliveryRepository
from models.services.cliente_service import ClienteService
from models.services.pedido_service import PedidoService
import os
from pprint import pprint
from bson import ObjectId


def conexao_banco() -> IDeliveryRepository:
    db_handle = DBConnection()
    db_handle.connect_to_db()
    db_connection = db_handle.get_db_connection()
    return IDeliveryRepository(db_connection)


idelivery_repository = conexao_banco()

def limpar_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def exibir_menu_inicial() -> int:
    limpar_console()
    print('#' * 14)
    print('#' * 4, 'Menu', '#' * 4)
    print('#' * 14)
    print('1 - Cadastrar pedido')
    print('2 - Atualizar pedido')
    print('3 - Deletar pedido')
    print('4 - Mostrar pedido')
    print('0 - Sair')
    print('#' * 14)
    opcao = int(input('Digite a opção desejada: '))
    return opcao


def cadastrar_pedido() -> None:
    dados_cliente = receber_dados_cliente()
    dados_pedido = receber_dados_pedido()
    cliente_service = ClienteService()
    pedido_service = PedidoService()
    document = cliente_service.cadastrar_cliente(dados_cliente['nome'],
                                                 dados_cliente['email'],
                                                 dados_cliente['telefone'],
                                                 dados_cliente['endereco'])

    document['pedido'] = pedido_service.criar_pedido(dados_pedido['itens'], dados_pedido['observacoes'])
    id = ObjectId()
    document['_id'] = id

    idelivery_repository.insert_document(document)
    print(f'Cadastrado com sucesso - id = {id}')


def receber_dados_pedido() -> dict:
    itens = {
        1: 'pizza',
        2: 'refrigerante',
        3: 'suco',
        4: 'hamburguer',
        5: 'sorvete'
    }
    pedido = {'itens':{}}

    opcao = -1

    while (opcao != 0):
        limpar_console()
        print('#' * 8)
        print('Opções')
        print('#' * 8)
        for chave, valor in itens.items():
            print(f'{chave} - {valor}')
        print('0 - Sair')

        opcao = int(input('Digite a opção desejada: '))
        if(opcao != 0):
            quantidade = int(input('Digite a quantidade desejada: '))

        if opcao in itens:
            item = itens[opcao]
            if item in pedido['itens']:
                pedido['itens'][item] += quantidade
            else:
                pedido['itens'][item] = quantidade

    observacoes = input('Digite as observações: ')

    pedido['observacoes'] = observacoes
    return pedido


def receber_dados_cliente() -> dict:
    limpar_console()
    print('#' * 15)
    print('#', 'Cadastrar Cliente', '#')
    print('#' * 15)
    nome = input('Digite o nome: ')
    email = input('Digite o email: ')
    telefone = input('Digite o telefone: ')
    endereco = input('Digite o endereço: ')

    dados_cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone,
        'endereco': endereco,
    }
    return dados_cliente


def atualizar_pedido() -> bool:
    print('#'*10)
    print('Atualização')
    print('#'*10)
    print('1 - Atualizar por id (um por vez)')
    print('2 - Atualizar por nome do cliente (varios por vez)')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            id = input('Digite o id do pedido: ')
            filter = {'_id': id}

            print('Editado com sucesso')
        case 2:
            nome = input('Digite o nome do cliente: ')
            filter = {'nome': nome}
            
            print('Editados com sucesso')
        case _:
            print('Opção inexistente')


def deletar_pedido() -> bool:
    print('#'*10)
    print('Exclusão')
    print('#'*10)
    print('1 - Excluir por id (um por vez)')
    print('2 - Excluir por nome do cliente (varios por vez)')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            id = input('Digite o id do pedido: ')
            filter = {'_id': ObjectId(id)}
            idelivery_repository.delete_one_registry(filter)
            print('Excluido com sucesso')
        case 2:
            nome = input('Digite o nome do cliente: ')
            filter = {'nome': nome}
            idelivery_repository.delete_many_registries(filter)
            print('Excluidos com sucesso')
        case _:
            print('Opção inexistente')


def mostrar_pedidos() -> None:
    limpar_console()
    print('#'*10)
    print('Exibição')
    print('#' * 10)
    print('1 - Mostrar todos pedidos')
    print('2 - Mostrar pedido por cliente')
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            pedidos = idelivery_repository.select_all()
            pprint(pedidos)
        case 2:
            nome = input('Digite o nome do cliente: ')
            filter = {'nome': nome}
            pedidos = idelivery_repository.select_many(filter)
            pprint(pedidos)
        case _:
            print('Opção inexistente')


def main():
    opcao = -1
    while opcao != 0:
        opcao = exibir_menu_inicial()
        match opcao:
            case 1:
                cadastrar_pedido()
            case 2:
                pass
            case 3:
                deletar_pedido()
            case 4:
                mostrar_pedidos()
            case _:
                print('Opção não existe')

if __name__ == "__main__":
    main()
