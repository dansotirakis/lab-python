days = int(input())
eat = int(round(float(input()), 0))
air = 2 * int(round(float(input()), 0))
hotel = int(round(float(input()), 0))
print((days * (hotel + eat) - hotel) + air)
