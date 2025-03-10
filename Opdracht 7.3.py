import random


def dobbelsteen_spel():
    while True:
        getrokken_getal = random.randint(1, 6)
        print("\nEr is een getal tussen 1 en 6.")

        for poging in range(1, 4):
            try:
                gok = int(input("Raad eens welk getal het is: "))

                if gok < 1 or gok > 6:
                    print("tussen 1 en 6.")
                    continue

                if gok == getrokken_getal:
                    print("Goedzo!")
                    break
                elif poging < 3:
                    print("Raad nog eens:")
            except ValueError:
                print("tussen 1 en 6.")

        else:
            print(f"verloren, Het was {getrokken_getal}.")

        opnieuw = input("Wil je nogmaals spelen?: ").strip().lower()
        if opnieuw != "ja":
            break


dobbelsteen_spel()
