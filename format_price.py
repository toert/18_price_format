from re import findall
import argparse


def parse_price():
    parser = argparse.ArgumentParser()
    parser.add_argument('price',
                        help='enter the price, which will convert into a beatiful shape')
    return parser.parse_args()


def make_float_beatiful(price):
    beatiful_price = '{0:,.2f}'.format(price).replace(',',' ')
    if findall(r'\d*[.]00', beatiful_price):
        beatiful_price = beatiful_price[:-3]
    return beatiful_price


def format_price(price):
    try:
        price = float(price)
    except ValueError:
        return None
    if price < 0 :
        return None
    return make_float_beatiful(price)


if __name__ == '__main__':
    parser = parse_price()
    user_price = parser.price
    formatted_price = format_price(user_price)
    if formatted_price is None:
        print('Input error')
    else:
        print(formatted_price)