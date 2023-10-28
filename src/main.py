# from database.create_tables import create_tables, drop_tables
# from database.insert_data_v2 import insert_data_to_db
# from etl.extraction import extract_to_new_table

# def main():
#     print("Droping tables...")
#     drop_tables()
#     print("Tables droped!!")
#     print("creating tables...")
#     create_tables()
#     print("Tables created!!")
#     print("Inserting data")
#     # insert_data()
#     insert_data_to_db(100)
#     print("Data Inserted!")
#     extract_to_new_table('data/movimento_flat')
#     print('csv file was created in the specified path')
#     print('---------------')
from database.tables import PostgreSQL
from etl.load import PostegresqlLoad
from etl.extraction import PostgresqlExtraction
from utils.config import load_config

def main(config):
    db = PostgreSQL()
    db.conn = "postgresql://sicredi:postgresql@localhost:5432/sicredi_data_challenge"
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