from .available_products import pruducts, update_avaible_products

order = [
    {
        "product_name": "chleb",
        "quantity": 10,
        "price": 41.90
    }
]


def create_an_order(manufacture, amount):

    if amount > pruducts[manufacture]["ilość"]:
        print("Nie mamy takiej ilości dostępnej w sklepie.")
        return None

    total_price = amount * pruducts[manufacture]["cena"]
    new_product = {
        "product_name": manufacture,
        "quantity": amount,
        "total_price": total_price
    }
    update_avaible_products(manufacture, amount)

    order.append(new_product)
    return new_product
