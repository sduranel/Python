from functools import wraps

def currency(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))

    return wrapper


@currency
def price_with_tax(price):
    return ROUND(price * (1 + (7.25 * .01))

deger = float(input('Deger'))
deger = price_with_tax(deger)
deger = round(int(deger),2)
print(deger)