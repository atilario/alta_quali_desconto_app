# alta_quali_desconto_app# 📦 Sistema de Cálculo e Gestão de Pedidos

Um sistema robusto e escalável para o cálculo de pedidos e aplicação de regras de desconto, desenvolvido para atender ao crescimento e à complexidade das operações de uma loja online.

---

## 🚀 Sobre o Projeto

O que começou como uma lógica simples de desconto fixo evoluiu. Hoje, o negócio lida com múltiplos perfis de clientes (Normais e VIPs), campanhas promocionais dinâmicas e a necessidade de registrar e persistir pedidos com alta extensibilidade. 

Este projeto foi arquitetado para resolver esse cenário, aplicando **Princípios SOLID** e **Design Patterns** (como *Strategy* e *State*) para garantir que novas regras de negócio possam ser adicionadas sem alterar o código já existente (Princípio Aberto/Fechado - OCP).

---

## 🛠️ Tecnologias e Arquitetura

* **Linguagem / Framework:** *(A definir, ex: Python, Java, Node.js)*
* **Padrões de Projeto:** *Strategy Pattern* (para os diferentes tipos de cálculo de desconto) e *Factory Pattern* (para a criação flexível de pedidos e campanhas).
* **Arquitetura:** Separação clara de responsabilidades (Clean Architecture / Camadas de Domínio, Aplicação e Infraestrutura).

---

## 📐 Regras de Negócio e Funcionalidades

* **Tipos de Clientes:**
  * **Cliente Normal:** Regras padrão de aplicação de descontos promocionais.
  * **Cliente VIP:** Elegível a descontos diferenciados, bonificações e isenções parciais.
* **Campanhas Promocionais:**
  * Descontos fixos em moeda (ex: R$ 20 off).
  * Descontos percentuais (ex: 10% off).
  * Descontos progressivos baseados no volume ou valor total do carrinho.
* **Gestão de Pedidos:**
  * Registro completo do histórico de compras.
  * Auditoria detalhada de quais descontos foram aplicados em cada item/pedido.

---

## 📂 Estrutura do Repositório

```text
ainda a pensar a arquitetura
```