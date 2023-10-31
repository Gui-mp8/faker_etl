from abc import ABC, abstractmethod
from typing import IO

class DBExtraction(ABC):
    # def __init__(self) -> None:
    #     self._jar_file_path = None

    # @property
    # def jar_file_path(self):
    #     return self._jar_file_path

    # @jar_file_path.setter
    # def jar(self, path: str):
    #     self._jar_file_path = path

    @abstractmethod
    def extract_to_csv(self) -> IO[str]:
        pass