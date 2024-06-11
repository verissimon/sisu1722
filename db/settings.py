import csv
from sqlalchemy import Engine, create_engine
from dotenv import load_dotenv
import psycopg2
import os


class PgConnector:
    from dotenv import load_dotenv

    def __init__(self):
        load_dotenv()
        USERNAME = os.environ.get("DB_USERNAME")
        PASSWORD = os.environ.get("DB_PASSWORD")
        DB_NOME = os.environ.get("DB_NAME")

        self.engine: Engine = create_engine(
            f"postgresql://{USERNAME}:{PASSWORD}@localhost:5432/{DB_NOME}"
        )
        self.conn = psycopg2.connect(
            database=DB_NOME,
            user=USERNAME,
            password=PASSWORD,
            host="localhost",
            port="5432",
        )
        self.cur = self.conn.cursor()

    def load_csv_pgsql(self, csv_path, nome_tabela):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.reader(f, delimiter="|")
                next(reader)
                self.cur.copy_expert(f"COPY {nome_tabela} FROM STDIN CSV DELIMITER '|' NULL AS ''", f)

            self.conn.commit()
        except Exception as e:
            print(e)


    def execute(self, query: str):
        try:
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)

    def close_connection(self):
        self.cur.close()
        self.conn.close()