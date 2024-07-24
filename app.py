from pokemondbscraper.scraper import PokemonDB

url = "https://pokemondb.net/pokedex/all"

if __name__=="__main__":

    processor = PokemonDB(url)
    processor.compile()