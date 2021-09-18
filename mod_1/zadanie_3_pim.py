# Zadanie numer 3 (pakiety i moduły)
import mod_1.calculations.capital_value

print("Kalkulator obliczający wartość lokaty po pewnym czasie")
initial_capital = int(input("Podaj wpłaconą kwotę:"))
percentage = float(input("Podaj wysokość oprocentowania (%):"))
duration_time = int(input("Podaj czas trwania inwestycji w latach:"))

effect = mod_1.calculations.capital_value.final_value(capital=initial_capital, percentage=percentage, time=duration_time)
print(f"Po {duration_time} latach wartość twojej lokaty będzie wynosić {effect:.2f}")
