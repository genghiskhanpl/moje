types_of_people = 10
x = f"Istnieje {types_of_people} rodzajów ludzi."

binary = "binarny"
do_not = "nie znają"
y = f"Ci, którzy znają system {binary} i ci, którzy go {do_not}."

print(x)
print(y)

print(f"Powiedziałem: {x}")
print(f"Powiedziałem również: '{y}'")
#definiujemy jedną zmienną bool oraz drugą która jest ciągiem znaków
hilarious = True
joke_evaluation = "Czyż to nie jest przezabawny dowcip?! {} "
#
print(joke_evaluation.format(hilarious))
#definiujemy nowe zmienne
w = "To jest lewa strona..."
e = "łańcucha znaków z prawą stroną."
#drukuje zmienną 'w' oraz zmienną 'e' ale nie są to liczby więc dodaje oba ciągi znaków do siebie
print(w + e)
