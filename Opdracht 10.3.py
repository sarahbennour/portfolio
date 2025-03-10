def telSpaties(tekst):
    return tekst.count(" ")

def telKlinkers(tekst):
    klinkers = "aeiouAEIOU"
    return sum(1 for letter in tekst if letter in klinkers)

string = input("Voer een string in: ")

print(f"Aantal spaties: {telSpaties(string)}")
print(f"Aantal klinkers: {telKlinkers(string)}")
