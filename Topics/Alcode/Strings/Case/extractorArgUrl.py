class ExtractorArgumentUrl:

    def __init__(self, url):
        if url:
            self.url = url.lower()
        else:
            raise LookupError("Invalid url!")

    def extractor(self):
        ORIGIN = ["moedaorigem=", "moedadestino=", "valor="]
        TYPES = ["dollar", "euro", "real", "drachma"]
        SIZE = self.url.count("&")
        return self.get_parameters(ORIGIN, SIZE, TYPES)

    def get_parameters(self, origin, size, types):
        param = []
        terminate = 0
        self.core_process(origin, size, param, terminate)
        self.validate_parameter(param, types)
        return param

    def core_process(self, origin, size_it, param, terminate):
        size = 1
        for i in origin:
            if terminate == size_it:
                value = self.url[self.findInitialIndices(i):]
            else:
                value = self.url[self.findInitialIndices(i):self.url.index('&', size, len(self.url))]

            size += self.url.index('&', self.url.find('&'), len(self.url))

            if value:
                param.append(value)
            terminate += 1

    def findInitialIndices(self, find):
        return self.url.find(find) + len(find)

    @staticmethod
    def validate_parameter(param, types):
        for i in param:
            if i not in types:
                return LookupError("Invalid parameter! options : " + str(types).replace("[", "").replace("]", ""))
