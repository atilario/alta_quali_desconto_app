# 📦 Sistema de Cálculo e Gestão de Pedidos (Clean Architecture)

Aplicação desenvolvida em **Python** para cálculo e gestão de pedidos com aplicação dinâmica de descontos, estruturada rigorosamente sob os princípios da **Arquitetura Limpa (Clean Architecture)** e boas práticas de **Engenharia de Software (SOLID & Design Patterns)**.

---

## 🎯 Sobre o Projeto

O projeto evoluiu de uma versão legada baseada em camadas acopladas (`src_antigo/`) para uma arquitetura modular, testável e altamente desacoplada (`src/app/`).

A aplicação atende a múltiplos perfis de clientes (Normal, VIP e Premium), calcula descontos através do padrão *Strategy*, transporta dados entre camadas através de *DTOs (Data Transfer Objects)*, persiste os dados através de repositórios desacoplados via *Gateways* e formata a resposta para apresentação utilizando *Presenters*.

---

## 🏛️ Arquitetura (Clean Architecture)

A aplicação foi organizada em camadas concêntricas respeitando a **Regra de Dependência**, onde as dependências apontam exclusivamente para dentro (em direção às regras de negócio de mais alto nível):

```
       ┌────────────────────────────────────────────────────────┐
       │ Frameworks & Drivers (MemoryDatabase)                  │
       │   ┌──────────────────────────────────────────────────┐ │
       │   │ Interface Adapters                               │ │
       │   │ (Controllers, Gateways, Repositories, Presenters)│ │
       │   │   ┌────────────────────────────────────────────┐ │ │
       │   │   │ Use Cases (CriarPedido, DTOs)              │ │ │
       │   │   │   ┌──────────────────────────────────────┐ │ │ │
       │   │   │   │ Entities (Pedido, Desconto Strategy) │ │ │ │
       │   │   │   └──────────────────────────────────────┘ │ │ │
       │   │   └────────────────────────────────────────────┘ │ │
       │   └──────────────────────────────────────────────────┘ │
       └────────────────────────────────────────────────────────┘
```

### 1. 🟢 Entities (Regras de Negócio Corporativas)
- **`Pedido`** (`src/app/entities/pedido.py`): Entidade que encapsula as propriedades do pedido (cliente, valor original e a estratégia de desconto) e calcula o valor do desconto e o valor final.
- **`Desconto`** (`src/app/entities/desconto.py`): Interface base `IDesconto` com subclasses concretas aplicando o padrão *Strategy*:
  - `DescontoNormal`: 10% de desconto.
  - `DescontoVIP`: 20% de desconto.
  - `DescontoPremium`: 30% de desconto.

### 2. 🔴 Use Cases (Regras de Negócio da Aplicação)
- **`CriarPedido`** (`src/app/use_cases/criar_pedido.py`): Orquestra o fluxo de negócio:
  - `executar(input_dto)`: Recebe `CriarPedidoInputDTO`, seleciona a estratégia de desconto adequada, instancia a entidade `Pedido`, salva via `IPedidoGateway` e retorna `CriarPedidoOutputDTO`.
  - `listar_pedidos()`: Recupera os pedidos salvos no gateway e mapeia para uma lista de `CriarPedidoOutputDTO`.

### 3. 🟡 Interface Adapters (Adaptadores de Interface)
- **DTOs (Data Transfer Objects)**:
  - `CriarPedidoInputDTO` (`src/app/dtos/criar_pedido_input_dto.py`): Encapsula e valida os dados de entrada (`cliente`, `valor_original`, `tipo_desconto`).
  - `CriarPedidoOutputDTO` (`src/app/dtos/criar_pedido_output_dto.py`): Transporta os dados calculados entre o caso de uso e os adaptadores de saída.
- **Gateways**:
  - `IPedidoGateway` (`src/app/gateways/pedido_gateway.py`): Contrato de interface abstrato para persistência (`salvar` e `listar`), viabilizando a Inversão de Dependência (DIP).
- **Repositories**:
  - `MemoryPedidoRepository` (`src/app/adapters/repositories/memory_pedido_repository.py`): Implementação concreta do gateway para armazenamento em banco de memória.
- **Controllers**:
  - `PedidoController` (`src/app/adapters/controllers/pedido_controller.py`): Ponto de entrada das requisições na aplicação, convertendo entradas em DTO e coordenando a execução com o caso de uso e o presenter.
- **Presenters**:
  - `PedidoPresenter` (`src/app/presenters/pedido_presenter.py`): Formata os DTOs produzidos pelo caso de uso em representações adequadas para exibição/interface (dicionários).

### 4. 🔵 Frameworks & Drivers
- **`MemoryDatabase`** (`src/app/frameworks/database/memory_database.py`): Camada externa de persistência temporária (banco em memória).

---

## 💎 Princípios SOLID e Padrões Aplicados

- **S (Single Responsibility Principle)**: Cada componente possui responsabilidade estrita (ex.: Controller lida com fluxo de entrada/saída, Use Case com regras da aplicação, Presenter com formatação de visualização).
- **O (Open/Closed Principle)**: Novos tipos de desconto podem ser criados implementando `IDesconto` sem modificar classes existentes.
- **L (Liskov Substitution Principle)**: Todas as implementações de `IDesconto` podem substituir a interface base sem quebrar o comportamento de `Pedido`.
- **I (Interface Segregation Principle)**: Interfaces enxutas e focadas (`IDesconto`, `IPedidoGateway`).
- **D (Dependency Inversion Principle)**: O caso de uso `CriarPedido` depende da abstração `IPedidoGateway`, e não de implementações concretas de bancos de dados.
- **Padrões de Projeto**:
  - *Strategy Pattern*: Polimorfismo nos cálculos de descontos.
  - *DTO Pattern*: Desacoplamento do tráfego de dados entre camadas.
  - *Gateway / Repository Pattern*: Abstração da camada de persistência.
  - *Presenter Pattern*: Isolamento da camada de apresentação.

---

## 📂 Estrutura de Diretórios

```text
desconto_app/
├── src/
│   └── app/
│       ├── adapters/
│       │   ├── controllers/
│       │   │   └── pedido_controller.py
│       │   └── repositories/
│       │       └── memory_pedido_repository.py
│       ├── dtos/
│       │   ├── criar_pedido_input_dto.py
│       │   └── criar_pedido_output_dto.py
│       ├── entities/
│       │   ├── desconto.py
│       │   └── pedido.py
│       ├── frameworks/
│       │   └── database/
│       │       └── memory_database.py
│       ├── gateways/
│       │   └── pedido_gateway.py
│       ├── presenters/
│       │   └── pedido_presenter.py
│       └── use_cases/
│           └── criar_pedido.py
├── src_antigo/                     # Código legado preservado para histórico
│   ├── controllers/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   └── services/
├── main.py                         # Ponto de entrada e orquestração do fluxo
├── README.md
└── .gitignore
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Executando a Aplicação
No terminal, execute o ponto de entrada `main.py`:

```bash
python main.py
# ou (no Windows)
py main.py
```

### Saída Esperada no Console
```text
Pedidos criados:
{'cliente': 'cliente A', 'valor_original': 100, 'valor_desconto': 10.0, 'valor_final': 90.0, 'tipo_desconto': 'normal'}
{'cliente': 'cliente B', 'valor_original': 200, 'valor_desconto': 60.0, 'valor_final': 140.0, 'tipo_desconto': 'premium'}
{'cliente': 'cliente C', 'valor_original': 300, 'valor_desconto': 60.0, 'valor_final': 240.0, 'tipo_desconto': 'vip'}

Pedidos salvos:
{'cliente': 'cliente A', 'valor_original': 100, 'valor_desconto': 10.0, 'valor_final': 90.0, 'tipo_desconto': 'normal'}
{'cliente': 'cliente B', 'valor_original': 200, 'valor_desconto': 60.0, 'valor_final': 140.0, 'tipo_desconto': 'premium'}
{'cliente': 'cliente C', 'valor_original': 300, 'valor_desconto': 60.0, 'valor_final': 240.0, 'tipo_desconto': 'vip'}
```