import requests

class PokemonAPI:
    def find_pokemon(name):
        url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
        try:
            res = requests.get(url)
            res.raise_for_status() # excpetion se o status for error
            data = res.json()
            print(f"Nome: {data['name']}")
            print(f"Peso: {data['weight']}")
            print(f"Habilidades:")
            for ability in data['abilities']:
                print(f"- {ability['ability']['name']}")           
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar o Pokemon. =(\n{e}")
            
nome_pokemon = input('Digite o nome do pokemon: ')
PokemonAPI.find_pokemon(nome_pokemon)