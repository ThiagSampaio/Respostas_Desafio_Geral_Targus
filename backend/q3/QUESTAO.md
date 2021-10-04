# Resposta Backend - Q3

Bem vindo leitor. Neste documento você terá acesso a toda documentação e o passo a passo para realização dessa questão.

# Tabela de conteúdo - Geral

1. [ Questão pedida. ](#desc)
2. [ Solução. ](#usage)

---

<a name="desc"></a>
<h2> Backend - Q3 </h2>

Esta questão possui múltiplos objetivos. Leia todos para planejar sua rota de trabalho.

Para cumprir os próximos, finalize este antes:

- Crie um container com uma API simples usando Flask ou FastAPI e adicione uma rota para receber requisições GET e responder com JSON. A API deverá ser acessível a partir do host (1 pt).

Após cumprir o primeiro item:

- Adicione uma rota para receber requisições POST com um endereço URL no corpo. Faça a requisição à URL e crie um log informando a data e hora da requisição, o link recebido e o estado da URL (online ou offline) (1 pt).
- Valide os dados recebidos e enviados pela API com dataclasses, Pydantic ou equivalente (1 pt).
- Crie um segundo container com um banco de dados da sua preferência e armazene os eventos POST (1pt).
  - Adicione uma rota que permita coletar os eventos POST armazenados no DB a partir da data do evento (1 pt).

Extra:

- Crie uma network para a API e um novo container para atuar como "ponte". O host deverá apenas (E SOMENTE) conseguir se comunicar com a ponte e nunca com a API diretamente (1 pt).

Deixe todos os arquivos do projeto neste diretório.

---

<a name="usage"></a>
<h2>Solução</h2>

<h3> Tabela de Solução</h3>

1. [ Criação da aplicação FASTAPI em um container. ](#1)
2. [ Solução da diminuição da imagem. ](#2)
3. [ Debug. ](#3)
3. [ Solução Final do Debug. ](#4)


<a name="1"></a>
<h3> 1- Criação da aplicação FASTAPI em um container </h3>