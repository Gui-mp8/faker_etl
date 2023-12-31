from typing import Any, Dict, List, Optional, Sequence, Union
from datetime import date

from faker import Faker

class DataGenerator(Faker):
    """
        This class generates fake data for database tables

        Attributes:
            faker (class): its a  library that generates fake data

        Methods:
            sample_(table): generates data for an especific table

    """
    def __init__(self):
        self.fake = Faker()

    def sample_associado(self, row_number: int) -> List[Dict[str, Any]]:
        """
            This method generates data for the table associado

            Args:
                row_number (int): Are the quantity of rows that you want in your fake data

            Returns:
                List[Dict[str, Any]]: It's returns a list that will be add at the database table
        """
        data = list()

        for row in range(1, row_number + 1):
            teste = {
                'id': self.fake.unique.random_int(min=1, max=row_number),
                'nome': self.fake.first_name(),
                'sobrenome': self.fake.last_name(),
                'idade': self.fake.random_int(min=18, max=100),
                'email': self.fake.email()
            }

            data.append(teste)

        return data

    def sample_conta(self, row_number):
        """
            This method generates data for the table conta

            Args:
                row_number (int): Are the quantity of rows that you want in your fake data

            Returns:
                List[Dict[str, Any]]: It's returns a list that will be add at the database table
        """
        data = list()

        for row in range(1, row_number + 1):
            teste = {
                'id': row,
                'tipo': self.fake.pystr(max_chars=5),
                'data_criacao': self.fake.date_time_between(start_date=date(2020, 1, 1), end_date=date(2022, 1, 1)),
                'id_associado': row
            }

            data.append(teste)

        return data

    def sample_cartao(self, row_number) -> List[Dict[str, Any]]:
        """
            This method generates data for the table cartao

            Args:
                row_number (int): Are the quantity of rows that you want in your fake data

            Returns:
                List[Dict[str, Any]]: It's returns a list that will be add at the database table
        """
        data = list()

        for row in range(1, row_number + 1):
            teste = {
                'id': row,
                'num_cartao': self.fake.random_int(),
                'nom_impresso': self.fake.name(),
                'data_criacao': self.fake.date_time_between(start_date=date(2020, 1, 1), end_date=date(2022, 1, 1)),
                'id_conta': row,
                'id_associado': row
            }

            data.append(teste)

        return data

    def sample_movimento(self, row_number) -> List[Dict[str, Any]]:
        """
            This method generates data for the table movimento

            Args:
                row_number (int): Are the quantity of rows that you want in your fake data

            Returns:
                List[Dict[str, Any]]: It's returns a list that will be add at the database table
        """
        data = list()

        for row in range(1, row_number + 1):
            teste = {
                'id': row,
                'vlr_transacao': self.fake.pyfloat(min_value=1, max_value=10000, right_digits=2),
                'des_transacao': self.fake.pystr(max_chars=5),
                'data_movimento': self.fake.date_time_between(start_date=date(2020, 1, 1), end_date=date(2022, 1, 1)),
                'id_cartao': row
            }

            data.append(teste)

        return data