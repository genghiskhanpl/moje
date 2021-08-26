#definiuje ile jest aut
cars = 100

#definiuje ile jest miejsc w samochodzie
space_in_a_car = 4

#określam ilośc kierowców
drivers = 30

#określam ilośc pasażerów
passangers = 90 

#ile dziś będzie pustych aut
cars_not_driven = cars - drivers

#ile dziś aut pojedzie
cars_driven = drivers

#łączna ilosc miejsc w autach
carpool_capacity = cars_driven * space_in_a_car

#ile musimy umieścić pasażerów aby
average_passangers_per_car = passangers / cars_driven


print("Dostępnych jest", cars, "samochodów.")
print("Dostępnych jest tylko", drivers, "kierowców.")
print("Dziś będzie", cars_not_driven, "pustych samochodów.")
print("Dziś możemy przetransportować", carpool_capacity, "osób.")
print("Mamy dziś do przewiezienia", passangers, "pasażerów.")
print("Musimy umieścić średnio", average_passangers_per_car, "osoby w każdym aucie.")
