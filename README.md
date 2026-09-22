# Sistema de Descontos

Projeto em Python para calcular o valor final de pedidos com diferentes regras de desconto.

O cenário cobre a evolução de uma loja online que começou com um desconto fixo simples e agora precisa lidar com:

- clientes normais e clientes VIP;
- campanhas promocionais;
- múltiplas regras de desconto;
- registro de pedidos;
- uma base preparada para crescer sem acoplar demais as regras de negócio.

## Objetivo

Centralizar o cálculo do valor final de pedidos de forma clara e extensível. A ideia é permitir que novas regras sejam adicionadas sem reescrever o fluxo inteiro do sistema.

## Estrutura esperada

O projeto hoje está em fase inicial e contém o arquivo principal `desconto.py`. A evolução natural é separar o código em camadas, por exemplo:

- modelo de pedido e cliente;
- regras de desconto;
- serviço responsável por aplicar as regras;
- persistência ou registro dos pedidos;
- testes automatizados.

## Como executar

Quando a implementação estiver pronta, o script principal poderá ser executado com:

```bash
python desconto.py
```

