class ExtractorArgumentUrl:

    def __init__(self, url):
        if self.urlValid(url):
            self.url = url
        else:
            raise LookupError("Invalid url!")

    @staticmethod
    def urlValid(url):
        if url:
            return True
        else:
            return False

    def Extractor(self):
        ORIGEM = "moedaorigem"
        DESTINO = "moedadestino"
        M_ORIGEM = self.url[self.findInitialIndices(ORIGEM):self.url.find("&")]
        M_DETINO = self.url[self.findInitialIndices(DESTINO):]
        return M_ORIGEM, M_DETINO

    def findInitialIndices(self, find):
        return self.url.find(find) + len(find) + 1
