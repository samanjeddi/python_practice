products = {
    'laptop' : 1200,
    'mouse' : 30,
    'keyboard' : 80,
    'monitor' : 300,
    'phone' : 900
}

valuable_products = {}

for product in products:
    if products[product] > 300:
        valuable_products[product] = products[product]

print(valuable_products)