from pandas import DataFrame
from handler import Handler


class UploadHandler(Handler):
    def pushDataToDb(self, path: str) -> bool:
        pass


class QueryHandler(Handler):
    def getById(self, id: str) -> DataFrame:
        pass
