from abc import ABC, abstractmethod

class AbstractData(ABC):
    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def add_data(self, vacancy, vacancy_path):
        pass

    @abstractmethod
    def delete_data(self):
        pass
