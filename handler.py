class Handler:
    def __init__(self):
        self.dbPathOrUrl: str = ""

    def getDbPathOrUrl(self) -> str:
        pass

    def setDbPathOrUrl(self, pathOrUrl: str) -> bool:
        pass
