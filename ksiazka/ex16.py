from sys import argv

script, filename = argv

print (f"Wymażemy {filename}.")
print ("Jeśli tego nie chcesz, wciśnij CTRL+C (^C).")
print ("Jeśli tego chcesz , wciśnij RETURN.")

input("?")

print ("Otwieranie pliku...")
target = open(filename, 'w')

print ("Wykasowywanie pliku. Do widzenia!")
target.truncate()

print ("Teraz poproszę Cię o wpisanie trzech linii tekstu.")

line1 = input ("linia 1: ")
line2 = input ("linia 2: ")
line3 = input ("linia 3: ")
line4 = input ("linia 4: ")
line5 = input ("linia 5: ")
line6 = input ("linia 6: ")

print ("Zapisuję je w pliku.")

target.write("line1\nline2\nline3\nline4\nline5\nline6\n")
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print ("A na koniec zamykamy plik.")
target.close()