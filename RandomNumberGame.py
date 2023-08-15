## create a random number between 0 and 100
import random
a = random.randint(0,99)

## Geef b een waarde buiten 0 t/m 99 zodat je een while loop kunt starten.
b = -1

## Creëer een loop waarbij de speler een hint krijgt bij een fout antwoord en zo opnieuw iets kan invoeren.
## Het spel eindigt wanneer de speler het juiste getal heeft geraden.
while b != a:
    b = int(input("What number between 0 and 100 would you like to chose? "))
    if b < a:
        print("Unfortunally your answer %d is too low, please try again." % b)
    elif b > a:
        print("Unfortunally your answer %d is too high, please try again." % b)
    else:
        print("Congratulations, %d is the correct number, you've won." % b)
