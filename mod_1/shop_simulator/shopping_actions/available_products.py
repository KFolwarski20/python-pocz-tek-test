
pruducts = {
    "chleb": {
        "ilość": 130,
        "cena": 4.19
    },
    "jabłko": {
        "ilość": 56,
        "cena": 3.99
    },
    "snickers": {
        "ilość": 48,
        "cena": 2.49}
}


def update_avaible_products(manufacture, quantity):
    pruducts[manufacture]["ilość"] -= quantity
