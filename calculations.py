from math import sqrt, pow


def price_count(price):
    if price < 50:
        floor = '0'
        ceiling = '50'
    elif price < 100:
        floor = '51'
        ceiling = '100'
    elif price < 150:
        floor = '101'
        ceiling = '150'
    elif price < 200:
        floor = '151'
        ceiling = '200'
    elif price < 250:
        floor = '201'
        ceiling = '250'
    elif price < 300:
        floor = '251'
        ceiling = '300'
    elif price < 350:
        floor = '301'
        ceiling = '350'
    elif price < 400:
        floor = '351'
        ceiling = '400'
    elif price < 450:
        floor = '401'
        ceiling = '450'
    elif price < 500:
        floor = '451'
        ceiling = '500'
    elif price < 600:
        floor = '501'
        ceiling = '600'
    elif price < 700:
        floor = '601'
        ceiling = '700'
    elif price < 800:
        floor = '701'
        ceiling = '800'
    elif price < 900:
        floor = '801'
        ceiling = '900'
    elif price < 1000:
        floor = '901'
        ceiling = '1000'
    elif price < 2000:
        floor = '1001'
        ceiling = '2000'
    else:
        floor = '2001'
        ceiling = '10000'

    return '$' + str(floor) + ' - $' + str(ceiling)
