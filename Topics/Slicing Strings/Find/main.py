url = "http://www.google.com/cambio?moedqaorigem=real&moedadestino=dolar&valor=100,00"

arg = url.find("=")
sep = url.find("&")

print(url[arg+1:sep])
