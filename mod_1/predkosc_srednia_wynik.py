# Zadanie numer 1 (pakiety i moduły)
from mod_1 import average_speed

print("Witaj w programie liczącym prędkość średnią biegu.")
length = int(input("Podaj ile kilometrów przebiegłeś:"))
duration = int(input("Podaj ile godzin Ci to zajęło:"))

speed = average_speed.average_velocity(distance=length, time=duration)
print(f"Twoja prędkość średnia wynosi {speed:.2f} km/h.")
