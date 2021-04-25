from extractorArgUrl import ExtractorArgumentUrl

url1 = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dollar&valor=1500"
url2 = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dollar&valor=1500"
url3 = "https://www.bytebank.com/cambio?moedaorigem=real&moedadestino=dollar&valor=500"

args1 = ExtractorArgumentUrl(url1)
args2 = ExtractorArgumentUrl(url2)
args3 = ExtractorArgumentUrl(url3)

print(len(args1))

print(args1)

print(args1 == args2)
print(args1 == args3)
