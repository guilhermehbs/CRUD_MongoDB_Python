## IDelivery - Sistema de Delivery com MongoDB e Python

Este projeto implementa um sistema de delivery chamado IDelivery utilizando MongoDB como banco de dados e Python para a lógica do sistema. O sistema permite as seguintes operações CRUD (Create, Read, Update, Delete) para pedidos:

* **Criar novo pedido:** Cadastrar um novo pedido com informações como data, hora, endereço de entrega, itens do pedido e valor total.
* **Atualizar pedido:** Modificar informações de um pedido existente, como status de entrega, endereço de entrega, itens do pedido, etc.
* **Deletar pedido:** Remover um pedido do sistema.
* **Listar pedidos:** Consultar todos os pedidos cadastrados no sistema, com a possibilidade de filtrar por data, status, etc.

### Pré-requisitos

* Python 3.6+
* MongoDB instalado e funcionando
* Biblioteca `pymongo` instalada: `pip install pymongo`

### Instalação

1. Clone o repositório: `git clone https://github.com/guilhermehbs/CRUD_MongoDB_Python.git`
2. Navegue até a pasta do projeto: `cd CRUD_MongoDB_Python`

### Configuração

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```
HOST=localhost
PORT=27017
DB_NAME=IDelivery
```

2. Substitua `mongodb://localhost:27017` com a URI de conexão do seu MongoDB.

### Uso

1. Execute o script `main.py`: `python main.py`
2. O sistema irá iniciar e você poderá utilizar as opções disponíveis pelo menu interativo.

### Estrutura do Projeto

```
CRUD_MongoDB_Python/
├── main.py        # Script principal do sistema
├── models/
|   ├── entities/  
│         ├── pedido.py     # Modelo de dados para pedidos
│         └── cliente.py      # Modelo de dados para o cliente
|   ├── connection_options/
│         ├── connection.py  # Funções de conexão com o MongoDB
│         └── mongo_db_configs.py     # Funções para conexão com o MongoDB
|   ├── services/
│         ├── pedido_services.py  # Funções criação de pedidos
│         └── cliente_services.py     # Funções criação de clientes
|   ├── repository/
│         └── IDeliveryRepository.py     # Funções para interação com o MongoDB
└── requirements.txt   # Lista de dependências

```

### Recursos

* **Criar novo pedido:** Insere um novo pedido no banco de dados.
* **Atualizar pedido:** Altera as informações de um pedido existente.
* **Deletar pedido:** Remove um pedido do banco de dados.
* **Listar pedidos:** Retorna todos os pedidos cadastrados, com opções de filtro por data, status, etc.
* **Validação de dados:** Implementa validação para garantir a integridade dos dados inseridos.
* **Menu interativo:** Interface simples para interação com o sistema.
* **Testes unitários:** Testes para garantir o funcionamento correto dos modelos de dados.

### Próximos Passos

* **Integração com API externa:** Implementar a integração com uma API externa para obter informações de geolocalização, cálculo de distância e valor do frete.
* **Sistema de autenticação:** Implementar um sistema de autenticação para controlar o acesso ao sistema.
* **Interface gráfica:** Criar uma interface gráfica para facilitar a interação com o sistema.
* **Notificações:** Implementar sistema de notificações para clientes e entregadores.
* **Gerenciamento de pagamentos:** Integrar o sistema com uma plataforma de pagamento para gerenciar as transações.

### Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para este repositório.

### Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
