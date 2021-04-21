from extractorArgUrl import ExtractorArgumentUrl

url = "https://www.bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"

args = ExtractorArgumentUrl(url)

origem, destino = args.Extractor()

print(origem, destino)
