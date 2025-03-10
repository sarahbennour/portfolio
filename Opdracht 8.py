def generate_pyramid(rows):
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)

aantal_rijen = int(input("Hoeveel rijen wil je? "))
generate_pyramid(aantal_rijen)
