price = float(input('price: '))
if price > 50:
    price = price - (price / 5)
elif 20 <= price <= 50:
    price = price - (price / 10)
elif price < 20:
    price = price

print(f"This product after sale is {price}$.")