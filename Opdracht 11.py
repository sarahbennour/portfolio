def lineaire_hypotheek():
    hypotheekbedrag = float(input("Wat is het hypotheekbedrag? "))
    rente = float(input("Wat is het jaarlijkse rentepercentage (bijv. 4 voor 4%)? "))
    looptijd = int(input("Wat is de looptijd in jaren? "))
    maanden = int(input("Hoeveel maanden wil je berekenen? "))

    totale_maanden = looptijd * 12
    maandelijkse_aflossing = hypotheekbedrag / totale_maanden

    resterend_bedrag = hypotheekbedrag
    for maand in range(1, maanden + 1):
        rente_bedrag = (rente / 100 / 12) * resterend_bedrag
        bruto_maandlast = rente_bedrag + maandelijkse_aflossing
        resterend_bedrag -= maandelijkse_aflossing

        print(f"Maand: {maand}")
        print(f"Rente: {rente_bedrag:.2f}")
        print(f"Aflossing: {maandelijkse_aflossing:.2f}")
        print(f"Resterend bedrag: {resterend_bedrag:.2f}")
        print(f"Bruto maandlast: {bruto_maandlast:.2f}")
        print("---")

        if resterend_bedrag <= 0:
            print("De hypotheek is volledig afgelost.")
            break

lineaire_hypotheek()
