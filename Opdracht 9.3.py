cijfers = list(map(float, input("Voer de cijfers in, gescheiden door spaties: ").split()))
aanwezigheid = float(input("Voer het aanwezigheidspercentage in (bijv. 85 voor 85%): "))

gemiddelde = sum(cijfers) / len(cijfers)

print(f"Het gemiddelde cijfer is: {gemiddelde:.2f}")

if aanwezigheid >= 80 and gemiddelde >= 7.5:
    print("De student is excellent!")
else:
    print("De student is niet excellent.")
