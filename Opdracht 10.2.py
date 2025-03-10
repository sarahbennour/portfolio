def reverseString(tekst):
    return tekst[::-1]


naam = input("Voer een naam in: ")

omgedraaide_naam = reverseString(naam)
print(f"De omgekeerde naam is: {omgedraaide_naam}")
