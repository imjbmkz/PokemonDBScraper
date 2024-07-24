# PokemonDB Scraper

This Python project scrapes data from the Pokemon Database (pokemondb.net) and stores it in a SQLite database.

## Overview

The project consists of two main files:

- **pokemondbscraper**: Contains the `PokemonDB` class responsible for scraping, processing, and storing Pokemon data.
- **app.py**: Uses the `PokemonDB` class to initiate the scraping process.

## Requirements

To run this project, ensure you have the following installed: 
- [**Python ^3.11**](https://www.python.org/downloads/)
- [**Poetry**](https://python-poetry.org/docs/)


## Usage

1. Clone the Repository:
```
git clone git@github.com:imjbmkz/PokemonDBScraper.git
cd pokemondbscraper
```

2. **Setup**: Run the following command to install the dependencies required.
```
poetry install
```

3. **Running the Scraper**:
   - Modify `url` in `app.py` if you want to scrape a different page from Pokemon Database.
   - Run `app.py` using the following command:
     ```
     poetry run python app.py
     ```
   This will initiate the scraping process, which involves downloading HTML, processing data, and storing it in the SQLite database.

3. **Logs**: Logs for INFO level are stored in `logs/std_out.log` and ERROR level logs are stored in `logs/std_err.log`.

4. **Database**: The scraped data is stored in `pokemondb.db` in a table named `pokedex`.

## Files

- **scraper.py**: Contains the `PokemonDB` class for scraping and processing logic.
- **app.py**: Entry point for running the scraper. Initializes `PokemonDB` with the URL and compiles the data.
- **logs/**:
  - `logs/std_out.log`: INFO level logs.
  - `logs/std_err.log`: ERROR level logs.
- **pokemondb.db**: SQLite database file where the scraped data is stored.

## Contributing

Feel free to fork this repository, enhance the scraper, or fix any bugs you encounter. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
