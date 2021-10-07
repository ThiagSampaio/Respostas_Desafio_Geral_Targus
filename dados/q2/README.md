# Dados - Q2

# Questão
valor: 1.5 pt.

Leia o arquivo ```DP.txt```, onde:

- ss = subsistema, sendo:
  - 1 = seco
  - 2 = s
  - 3 = ne
  - 4 = n
  - 11 = imperatriz
- di = dia
- hi = hora
- m = meiahora (bool)
- df = desconsidere
- hf = desconsidere
- m (segunda) = desconsidere
- Demanda = demanda energética

e ajuste a estrutura de dados para o seguinte modelo (ao invés de ISODate, use datetime):

```json
{
    "subsistema" : "seco",
    "data_partida" : ISODate("2021-09-25T00:00:00.000Z"),
    "valores" : [ 
        {
            "demanda" : 36712.0,
            "data" : ISODate("2021-09-26T00:00:00.000Z")
        }, 
        {
            "demanda" : 35628.0,
            "data" : ISODate("2021-09-26T00:30:00.000Z")
        }, 
        {...}
    ]
}
```

Onde:

- subsistema: subsistema avaliado.
- data_partida: data de partida da previsão.
- valores: Lista de previsões com a data prevista.

Nota: no primeiro dia, a previsão acontece de meia em meia hora. A partir do segundo dia previsto, a previsão não possui uma frequência fixa.


Resposta 
---
Solução no notebook do diretório
---