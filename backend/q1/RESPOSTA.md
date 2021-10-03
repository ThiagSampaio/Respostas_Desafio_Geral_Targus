# Resposta Backend - Q1 

Bem vindo leitor. Neste documento você terá acesso a toda documentação e o passo a passo para realização dessa questão.

# Tabela de conteúdo - Geral

1. [ Questão pedida. ](#desc)
2. [ Solução. ](#usage)

---

<a name="desc"></a>
<h2> Backend - Q1 </h2>

Valor: 1.5 pt

Corrija e otimize o Dockerfile existente no diretório.
O projeto inicial buildado pesará, aproximadamente, 1.1GB.

🏋️ Reduza o peso geral da imagem o máximo possível.  
⏰ Reduza o tempo de build o máximo que conseguir. Considere que o código pode mudar.

Crie uma versão "Dockerfile.otimizado" contendo suas alterações e mantenha o original.

Para executar o build, utilize o script bash ```docker-build.bash``` disponibilizado:

```bash
bash docker-build.bash -t q1:dev .
```

O script irá gerar um JSON contendo os tempos de build em cada etapa.
Compartilhe a saída JSON do bash executado, tal como o exemplo abaixo:

```json
[
  {
    "time": 1632846937,
    "step": 0,
    "cmd": "START"
  },
  {
    "time": 1632846958,
    "step": 1,
    "cmd": "FROM python:latest"
  },
  {...}
]
```

Descreva abaixo, em poucas linhas, o que você fez e por que o fez para melhorar o
Dockerfile e colocar o projeto para funcionar.

---

<a name="usage"></a>
<h2>Solução</h2>

<h3> 1- Análise da imagem passada </h3>

Com o comando abaixo, montei o container para a análise. 

```bash
docker build -t analise:01 .
```
<h4> 1.1 - 1° Análise: Tamanho da imagem </h4>
Após montar o container com a imagem passada temos o primeiro dado: o tamanho do arquivo = 1.14GB

![Imagem da primeira montagem ](Imgs/b_q1.1.PNG)

Para reduzir o peso desta imagem , vamos primeiro mudar a versão do python utilizado.

<h5> 1.1.1 -> Primeira mudança do arquivo Dockefile.
  
A primeira mudança será, como já relatado, na versão do python utilizado. 
Para tal mudaremos a seguinte linha no Dockfile:
  
DE:
  
```python
FROM python:latest
```

  
RESULTADO: 

Rodando o comando:
```bash
docker build -t analise:01 .
```

Obtemos o primeiro passo:

![Imagem da segunda montagem ](Imgs/b_q1.2.PNG)

OU seja
