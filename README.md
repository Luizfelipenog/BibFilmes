# BibFilmes

BibFilmes é um sistema desenvolvido para rankear, recomendar e tabular filmes. O repositório contém scripts Python que realizam essas operações com base em dados de filmes. O projeto foi criado para fornecer funcionalidades úteis para manipulação de informações de filmes.

## 🚀 Funcionalidades

- **Rankear.py**: Classifica filmes com base em critérios definidos.
- **Recomendar.py**: Gera recomendações de filmes baseadas em preferências ou histórico.
- **Tabelar.py**: Organiza dados em formato tabular para visualização ou exportação.

## 📁 Estrutura do Projeto







## 📌 Requisitos

- **Python** 3.x
- Dependências podem ser instaladas através do arquivo `setup.py` ou diretamente com `pip`:

```bash
pip install -r requirements.txt
```


---

### Resumo da Utilização:

- **`Rankear('comedy')`**: Rankeia os filmes do gênero "comedy".
- **`Rankear('comedy', 1)`**: Rankeia os melhores filmes do gênero "comedy".
- **`Rankear('comedy', 2)`**: Rankeia os filmes recomendados do gênero "comedy".
- **`Recomendar('comedy')`**: Recomenda filmes do gênero "comedy".
- **`Tabelar('comedy', 1)`**: Exibe uma tabela dos melhores filmes do gênero "comedy".
- **`Tabelar('comedy', 2)`**: Exibe uma tabela dos filmes recomendados do gênero "comedy".

Essas funções permitem a manipulação dos filmes de acordo com o gênero e preferências do usuário, tornando o sistema flexível para diferentes necessidades de visualização e recomendação de filmes.

