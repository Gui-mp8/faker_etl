from typing import IO

from pyspark.sql import DataFrame

from abstraction.db_extraction import DBExtraction

class PostgresqlExtraction(DBExtraction):
    """
        This class extracts data from a PostgreSQL database

        Args:
            config (dict): _description_

        Methods:
            extracst_to_csv(): extracts the dataframe data to a csv
    """
    def __init__(self, config: dict) -> None:
        self.config = config

    def extract_to_csv(self, df: DataFrame) -> IO[str]:
        '''
            Extract data from database tables, create tempViews and merge in 'movimento_flat' dataframe
        '''
        # Write movimento_flat dataframe in a csv file
        return df.coalesce(1).write.csv(
            path=f"data/{self.config['final_result_path']}",
            sep=';',
            header=True,
            mode='overwrite'
        )