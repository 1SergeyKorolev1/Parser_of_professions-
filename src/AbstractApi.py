from abc import ABC, abstractmethod

class AbstractApi(ABC):
    @abstractmethod
    def get_vacancy(self, search_query):
        pass
