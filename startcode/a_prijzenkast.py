prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!\n")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")
doos = int(input("welke doos wil je"))

if doos == 1:
    print(prijzenkast[0])
elif doos == 2:
    print(prijzenkast[1])
elif doos ==  3:
    print(prijzenkast[2])
else:
    print("deze doos bestaat niet")
