# Sistema Bancário em Python

## Índice

1. [Descrição](#descrição)
2. [Como Usar](#como-usar)
3. [Exemplo de Saída Esperada](#exemplo-de-saída-esperada)
4. [Pré-Requisitos](#pré-requisitos)
5. [Contribua](#contribuições)
6. [Licença](#licença)
7. [Contatos e Network](#contatos-e-network)


## Descrição

Este projeto implementa um **sistema bancário simples** utilizando **Python**. O objetivo principal do sistema é gerenciar contas bancárias de usuários, com funcionalidades como depósito, saque, extrato e a criação de contas bancárias. Através deste repositório, é possível realizar transações bancárias como um **banco digital básico**, com a criação de usuários e contas, além de fornecer um extrato das transações realizadas.

### Funcionalidades Principais:

- **Criar Usuário**: Cadastra um novo usuário com informações como nome, CPF, data de nascimento e endereço.
- **Criar Conta**: Cria uma conta bancária para um usuário cadastrado.
- **Depósito**: Permite realizar depósitos em uma conta bancária.
- **Saque**: Permite realizar saques de uma conta bancária, com um limite de saques diário.
- **Extrato**: Exibe o histórico de transações de uma conta, incluindo depósitos e saques.
- **Listar Contas**: Exibe uma lista com as informações das contas cadastradas no sistema.


## Como Usar

### Passo a Passo:

1. **Clone o Repositório**:
   - Para obter uma cópia local do projeto, rode o seguinte comando no terminal:
   ```bash
   git clone https://github.com/jacivaldocarvalho/sistema-bancario-python.git
   ```

2. **Execute o Código**:
   - Navegue até o diretório do projeto e execute o código:
   ```bash
   python sistema_bancario.py
   ```

3. **Interaja com o Sistema**:
   - O sistema apresentará um menu interativo onde você poderá escolher as opções disponíveis:
     - **[d]**: Depósito
     - **[s]**: Saque
     - **[e]**: Extrato
     - **[nu]**: Novo Usuário
     - **[nc]**: Nova Conta
     - **[lc]**: Listar Contas
     - **[q]**: Sair

4. **Exemplo de Uso**:
   - Ao selecionar a opção para **novo usuário**, o sistema pedirá para inserir informações como CPF, nome, data de nascimento e endereço.
   - Ao selecionar **nova conta**, será necessário informar o CPF do usuário, e uma nova conta será criada para ele.
   - Ao selecionar **depósito** ou **saque**, você poderá realizar transações em uma conta já existente.
   - O **extrato** mostrará todas as transações realizadas na conta (depósitos e saques).


## Exemplo de Saída Esperada

**Menu Principal**:

```
===== MENU PRINCIPAL =====
[d]  Depósito
[s]  Saque
[e]  Extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q]  Sair
=> 
```

**Após Realizar um Depósito**:
```
***** Depósito realizado com sucesso! *****
```

**Após Realizar um Saque**:
```
Valor autorizado R$ 50.00
```

**Exibindo Extrato**:
```
================ EXTRATO ================
Saque:           R$ 50.00
Depósito:        R$ 100.00

Saldo:           R$ 50.00
==========================================
```


## Pré-Requisitos

- **Python 3.x**: Este código foi desenvolvido e testado na versão 3.8 ou superior do Python.
- **Nenhuma dependência externa**: O código não requer pacotes ou bibliotecas externas. Tudo o que é necessário está incluído na instalação do Python.

### Como Instalar:

1. **Instale o Python 3.x**:
   - Caso não tenha o Python 3 instalado, faça o download a partir do site oficial: [Python](https://www.python.org/downloads/).

2. **Verifique se o Python está instalado corretamente**:
   - No terminal ou prompt de comando, execute:
   ```bash
   python --version
   ```


## Contribuições

Se você tiver sugestões de melhorias ou encontrar problemas com o script, sinta-se à vontade para abrir um **issue** ou submeter um **pull request**.

## Contatos e Network

- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/) 👔
- **E-mail**: [E-mail](mailto:jacivaldocarvalho@gmail.com) 📧
- **GitHub**: [GitHub](https://github.com/jacivaldocarvalho) 🐙
- **Medium**: [Medium](https://medium.com/@jacivaldocarvalho) ✍️

Sempre aberto a novas conexões e oportunidades de aprendizado!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
