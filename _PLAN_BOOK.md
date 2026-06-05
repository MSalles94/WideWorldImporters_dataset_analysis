# PLAN BOOK

## 01. Infrastructure

## 02. Explore database

* Overview of the dataset 
    * Explain each table and describe

* Business questions
    * Chat GPT
* Nível 1 — Básico
    * Quais são os 10 clientes com o maior número de pedidos realizados?
    * Quais são os 10 produtos mais vendidos em quantidade?
    * Qual é o faturamento total da empresa?
    * Quantos clientes existem por categoria de cliente?
    * Quantos produtos existem por categoria de produto?
    * Quais são as 10 cidades com maior número de clientes cadastrados?
    * Qual foi o faturamento por ano?
    * Qual foi o faturamento por mês?
    * Quais vendedores registraram mais pedidos?
    * Quais métodos de entrega são mais utilizados pelos clientes?
* Nível 2 — Intermediário
    * Quais clientes geraram maior faturamento para a empresa?
    * Quais produtos geraram maior receita total?
    * Qual é o ticket médio dos pedidos por cliente?
    * Quais cidades apresentam o maior faturamento médio por cliente?
    * Qual a participação percentual de cada categoria de produto no faturamento total?
    * Quais clientes não realizaram compras nos últimos 12 meses disponíveis na base?
    * Existe sazonalidade nas vendas? Quais meses apresentam maior e menor faturamento?
    * Qual é o tempo médio entre a realização do pedido e a entrega, por método de entrega?
    * Quais vendedores possuem os maiores valores médios de venda por pedido?
    * Quais combinações de cliente, cidade e categoria de produto geram o maior faturamento?
* Nível 3 — Avançado
    * Quais clientes apresentam maior crescimento de faturamento entre anos consecutivos?
    * Qual é a concentração de receita da empresa? Os 20% maiores clientes representam qual percentual do faturamento?
    * Quais produtos apresentam crescimento consistente de vendas ao longo do tempo?
    * Quais clientes possuem comportamento de compra recorrente e previsível?
    * Qual é o ciclo médio de recompra por cliente?
    * Existem clientes com alto volume de pedidos, mas baixo faturamento médio? Quem são eles?
    * Quais categorias de produtos apresentam maior margem de crescimento considerando histórico de vendas?
    * Qual é o impacto de cada vendedor no faturamento total da empresa ao longo do tempo?
    * Quais regiões apresentam maior potencial de expansão considerando quantidade de clientes e faturamento médio?
    * Como segmentar os clientes em grupos de valor (alto, médio e baixo) utilizando critérios de faturamento e frequência de compras?
* Nível 4 — Preparação para DW e Dashboard
    * Quais KPIs devem compor o dashboard executivo da empresa?
    * Como definir uma tabela fato de vendas e quais dimensões serão necessárias?
    * Quais métricas devem ser calculadas na camada de Data Warehouse em vez de no dashboard?
    * Quais indicadores permitem acompanhar retenção de clientes ao longo do tempo?
    * Como medir o desempenho de vendedores considerando volume, faturamento e ticket médio?
    * Quais produtos devem ser classificados como estratégicos para o negócio?
    * Como identificar clientes VIP utilizando critérios de faturamento, frequência e recência?
    * Quais indicadores ajudam a monitorar a eficiência logística das entregas?
    * Quais dimensões são mais relevantes para explicar variações de faturamento?
    * Como construir uma visão executiva que responda rapidamente: "Quem vendeu, o quê, para quem, quando e onde?" utilizando um modelo dimensional?
 
--- 

## 03. Define Business requirements

---
* Ideas

    * Data analyst
        * Service
            * Calculate backorders and backlog by day
            * OTIF metrics
        * Inventory
            * Inventory balance and growth
            * ABC analysis
        * Commercial
            * Sales indicators

    * Data engineering
        * make snapshots of the data
            * use date
            * try to make an original order using backorder


    