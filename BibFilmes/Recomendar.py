from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup

genero = input("Digite o nome do gênero: ")

url = f'https://www.imdb.com/search/title/?title_type=feature&genres={genero}&user_rating=,10&sort=num_votes,desc'

headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

requisicao = requests.get(url, headers=headers)

if requisicao.status_code == 200:
    site = BeautifulSoup(requisicao.text, "html.parser")
    #pesquisa = site.find_all("h3")
    #print(pesquisa[0])
    pesquisa= site.find_all("h3", class_="ipc-title__text")
    # Filtrando apenas os títulos
    titulos = [titulo.text.strip() for titulo in pesquisa if titulo.text.strip().isdigit() == False]

    print("Títulos dos filmes:")
    for i, titulo in enumerate(titulos, start=1):
        print(f"{titulo}")
else:
    print(f"Erro na requisição: {requisicao.status_code}")
