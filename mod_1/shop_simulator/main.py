from shopping_actions.order_creating import create_an_order


def run_shop():
    print("Symulator sklepu.")
    product_name = input("Podaj nazwę produktu, który chciałbyś zamówić:")
    quantity = int(input("Podaj ilość kg/szt:"))

    value = create_an_order(manufacture=product_name, amount=quantity)
    if value is not None:
        total_price = value["total_price"]
        print(f"Łączny koszt zakupów wynosi {total_price} PLN")


if __name__ == '__main__':
    run_shop()
