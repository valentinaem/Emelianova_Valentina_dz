import requests

def currency_rates(x):
    x = x.upper()
    answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    answer_2 = str(answer.text)
    answer_2 = answer_2.split('>')
    name = str(f'{x}</CharCode')
    if name not in answer_2:
        return None
    else:
        index_usd = answer_2.index(name)
        value = answer_2[index_usd + 6]
        price = (value.split('</'))[0]
        price = price.split(',')
        price = '.'.join(price)
        price = float(price)
    # print(type(price))
        return (f'Курс {x} к рублю составлаяет: {price}')

print(currency_rates('EUr'))

