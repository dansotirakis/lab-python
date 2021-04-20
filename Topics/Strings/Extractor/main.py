from extractorArgUrl import ExtractorArgumentUrl

url = "http://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar"

args = ExtractorArgumentUrl(url)

origem, destino = args.Extractor()

print(origem, destino)
