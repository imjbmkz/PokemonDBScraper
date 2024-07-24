import traceback
import sqlite3
import requests
import bs4
import pandas as pd
from bs4 import BeautifulSoup
from loguru import logger

logger.add("logs/std_out.log", level="INFO")
logger.add("logs/std_err.log", level="ERROR")
   
class PokemonDB:
    def __init__(self, url: str) -> None:
        self.url = url

        # Create the destination table upon class initialization if it doesn't exist 
        with sqlite3.connect("pokemondb.db") as conn:
            sql = "select count(1) as n from sqlite_master WHERE type='table' AND name='pokedex'"
            cursor = conn.execute(sql)
            if cursor.fetchone()[0]==0:
                sql = """ create table pokedex (
                            number varchar(10),
                            name varchar(255),
                            type varchar(255),
                            total int,
                            hp int,
                            attack int,
                            defense int,
                            sp_attack int,
                            sp_defense int,
                            speed int
                        )
                """
                conn.execute(sql)

    def download_html(self) -> str:
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            logger.info(f"Sucessfully fetched {self.url}")
            self.html = response.text
            self.soup = BeautifulSoup(self.html, "html.parser")

        except Exception as e:
            logger.info(e)
            logger.error(traceback.format_exc())
    
    def transform_row(self, row: bs4.element.Tag) -> dict:
        try:
            columns = row.find_all("td")
            return {
                "number": columns[0].find("span").text,
                "name": columns[1].text,
                "type": columns[2].text,
                "total": columns[3].text,
                "hp": columns[4].text,
                "attack": columns[5].text,
                "defense": columns[6].text,
                "sp_attack": columns[7].text,
                "sp_defense": columns[8].text,
                "speed": columns[9].text,
            }
        
        except Exception as e:
            logger.error(f"Error processing row {row}: {e}")

    def process_data(self):
        rows = self.soup.find_all("tr")
        data_rows = []
        for row in rows[1:]: # skip table headers
            dr = self.transform_row(row)
            data_rows.append(dr)

        try:
            self.consolidated = pd.DataFrame(data_rows)
            logger.info("Successfully processed all rows.")

        except Exception as e:
            logger.error(f"Error in consolidating rows: {e}")
            raise e

    def load_data(self):
        try:
            with sqlite3.connect("pokemondb.db") as conn:
                df = self.get_consolidated_data()
                n = df.shape[0]
                conn.execute("delete from pokedex")
                df.to_sql("pokedex", con=conn, index=False, if_exists="append")
                logger.info(f"{n} rows have been loaded to db.")

        except Exception as e:
            logger.error(f"Error occurred when loading data to db: {e}")
            raise e

    def compile(self):
        self.download_html()
        self.process_data()
        self.load_data()

    def get_consolidated_data(self):
        try:
            return self.consolidated
        except Exception as e:
            raise ValueError("The consolidated data may not be available yet. Run self.compile() first. {e}")
        
    
