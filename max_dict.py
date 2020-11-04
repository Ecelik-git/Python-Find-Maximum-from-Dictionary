
stock = dict(apple=85, banana=40, chocolate=35, bean=70)
price = dict(apple=1.2, banana=0.5, chocolate=1.7, bean=1.45)
max_key = max(price, key=price.get)
max_item = max(stock, key=stock.get)
print(max_key, "is the most expensive one here")
print("yet we have a lot of", max_item, "in this store")
