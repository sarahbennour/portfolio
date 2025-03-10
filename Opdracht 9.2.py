tekst = input("Geef een tekst op: ")

lengte = len(tekst)
eerste, laatste = tekst[0], tekst[-1]
middelste = tekst[len(tekst) // 2 - 1: len(tekst) // 2 + 1] if len(tekst) % 2 == 0 else tekst[len(tekst) // 2]
spaties = tekst.count(" ")
klinkers = sum(1 for letter in tekst if letter in "aeiouAEIOU")

print("\nResultaten:")
print(f"1. Lengte: {lengte}")
print(f"2. Eerste: '{eerste}', Laatste: '{laatste}'")
print(f"3. Middelste: '{middelste}'")
print(f"4. Spaties: {spaties}")
print(f"5. Klinkers: {klinkers}")
