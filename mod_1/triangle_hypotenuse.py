# Zadanie numer 2 (pakiety i moduły)
import math


def calculate_len_c(a_len, b_len):
    c_len = math.sqrt(math.pow(a_len, 2)+math.pow(b_len, 2))
    return c_len


a = float(input("Podaj długość pierwszej przyprostokątnej:"))
b = float(input("Podaj długość drugiej przyprostokątnej:"))

result = calculate_len_c(a_len=a, b_len=b)
print(f"Długość przeciwprostokątnej wynosi {result:.1f}")
