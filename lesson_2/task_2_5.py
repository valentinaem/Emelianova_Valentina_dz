
shop_bag = ['67.5', '49.3', '78.0', '36.4', '34.0', '18.0', '34.5', '23.7', '25.0', '91.3', '77.0']

new_list = []
for i in shop_bag:
    i = str(i)
    part = i.split('.')
    text = f'{part[0]} руб. {part[1]:0>2} коп.'
    new_list.append(text)
print(', '.join(new_list))

print(id(shop_bag))
shop_bag.sort()
print(id(shop_bag))
print(shop_bag)
new_shop_bag = shop_bag.copy()[::-1]
print(new_shop_bag)
top_5 = new_shop_bag[:5]
top_5.sort()
print(', '.join(top_5))