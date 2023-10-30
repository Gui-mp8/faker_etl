from database.tables import PostgreSQL
from etl.load import PostegresqlLoad
from etl.extraction import PostgresqlExtraction
from utils.config import load_config

def main(config):
    db = PostgreSQL()
    # db.conn = "postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge"
    db.conn = "postgresql://sicredi:postgresql@postgres/sicredi_data_challenge"
    print("Droping tables..")
    db.drop_table()
    print("Tables dropped!!! \nCreating Tables...")
    db.create_table()
    print("Tables Created!!!")

    print("Inserting data...")
    PostegresqlLoad(config).add_data_to_tables()
    print("Data Inserted!")

    print("Extracting data to csv...")
    PostgresqlExtraction(config).extract_to_csv()
    print('csv file was created in the specified path')
if __name__ == "__main__":
    config = load_config()
    main(config)