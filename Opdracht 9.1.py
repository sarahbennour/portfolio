def reverse_name(name):
    reversed_name = ''
    for char in name:
        reversed_name = char + reversed_name
    return ' '.join(reversed_name)

naam = input("Geef je naam: ")
omgekeerde_naam = reverse_name(naam)
print("The reversed string (using loops) is: " + omgekeerde_naam)
