from marvel_api_handler import MarvelAPI
from apps.omni_catalog.models import Omnibus

class APIDBHandler:
    @staticmethod
    def test():
        print(Omnibus)
if __name__ == '__main__':
    APIDBHandler.test()