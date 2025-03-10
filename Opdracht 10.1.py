def isSchrikkelJaar(jaar):
    if (jaar % 4 == 0 and jaar % 100 != 0) or (jaar % 400 == 0):
        return True
    else:
        return False

print("Jaren 2000 t/m 2010:")
for jaar in range(2000, 2011):
    if isSchrikkelJaar(jaar):
        print(f"{jaar} is een schrikkeljaar.")
    else:
        print(f"{jaar} is geen schrikkeljaar.")
