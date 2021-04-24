import re

email1 = "Meu numero é 1234-1234 jkhjjh 12345678"
email2 = "Meu numero é 1234-1234 jjkhkjhj 654654 - 65464654 654654 -44654"
email3 = "Meu numero é 1234-1234 + 55555555555555555555 464564654654 64654-456454"

partner = "[0-9]{4,5}[-]*[0-9]{4}"

filtered1 = re.findall(partner, email1)
filtered2 = re.findall(partner, email2)
filtered3 = re.findall(partner, email3)

print(filtered1, filtered2, filtered3)

