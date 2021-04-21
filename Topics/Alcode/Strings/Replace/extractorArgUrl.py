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
        ORIGIN = "moedaorigem="
        DESTINY = "moedadestino="

        ROOT_ORIGIN = self.url[self.findInitialIndices(ORIGIN):self.url.find("&")]

        if ROOT_ORIGIN != "moedadestino":
            M_ORIGIN = ROOT_ORIGIN
        else:
            M_ORIGIN_ROOT = self.changeCurrentOrigin()
            M_ORIGIN = M_ORIGIN_ROOT[self.findInitialIndices(ORIGIN):M_ORIGIN_ROOT.find("&")]

        M_DESTINY = self.url[self.findInitialIndices(DESTINY):]

        return M_ORIGIN, M_DESTINY

    def validate_parameter(self, ORIGIN):
        return self.changeCurrentOrigin()[self.findInitialIndices(ORIGIN):self.url.find("&")]

    def findInitialIndices(self, find):
        return self.url.find(find) + len(find)

    def changeCurrentOrigin(self):
        return self.url.replace("moedadestino", "real")
