from database.create_tables import create_tables, drop_tables
# from database.insert_data import insert_data
from database.insert_data_v2 import insert_data_to_db

def main():
    print("Droping tables...")
    drop_tables()
    print("Tables droped!!")
    print("creating tables...")
    create_tables()
    print("Tables created!!")
    print("Inserting data")
    # insert_data()
    insert_data_to_db(100)
    print("Data Inserted!")

if __name__ == "__main__":
    main()