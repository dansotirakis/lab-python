from extractorArgUrl import ExtractorArgumentUrl

url = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dollar&valor=1500"

args = ExtractorArgumentUrl(url)

print(args.extractor())
