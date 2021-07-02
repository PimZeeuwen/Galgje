#Geef een paar variablen en lijsten alvast een standaardwaarde voor later. En importeer wat functies die we later nodig hebben
tellerD = 20
woord = []
woord_bekend = []
FouteLetters = []
woord_input = ''
AantalFouten = 0
Aantal_WoordenGeraden = 0
Gewonnen = 0
Verloren = 0
import random

#Ook importeren we wat afbeeldingen af te kunnen drukken.
woorden_4letters = [
    'tijd', 'fors', 'giga', 'cake', 'uier', 'quiz', 'chef', 'baby', 'quad',
    'open', 'accu', 'ogen', 'stuk', 'volk', 'even', 'kwik', 'vorm'
]
woorden_5letters = [
    'cavia', 'jasje', 'lepel', 'quote', 'botox', 'nihil', 'detox', 'nacht',
    'cacao', 'boxer', 'straks', 'flirt', 'stijl', 'tocht', 'broek', 'nieuw',
    'klacht', 'print'
]
woorden_6letters = [
    'krukje',
    'sambal',
    'zuivel',
    'dieren',
    'vrezen',
    'boycot',
    'cyclus',
    'gering',
    'triomf',
    'straks',
    'fysiek',
    'gammel',
    'geloof',
    'uitleg',
    'joggen',
    'oorlog',
]
woorden_7letters = [
    'winnaar', 'hierbij', 'zitting', 'cabaret', 'bewogen', 'ijverig',
    'camping', 'kloppen', 'aaibaar', 'miljoen', 'zijraam'
]
woorden_8letters = [
    'kritisch', 'picknick', 'cruciaal', 'dyslexie', 'poppetje', 'carnaval',
    'turquoise'
]
woorden_9letters = ['verzenden', 'alliantie', 'werksfeer', 'schikking']
woorden_10letters = ['chagrijnig', 'volwaardig', 'inrichting']


#Vraag speler 1 om een woord en zorg er dan voor dat het woord niet meer te zien is
def input_vragen():
    global AantalLetters
    global woord_input
    woord_input = input("Speler 1, Welk woord heeft u gekozen?")
    print("\n" * 30)
    AantalLetters = len(woord_input)


#laat een random woord gegenereerd worden
def genereren_woord():
    global random, woord, AantalLetters, woord_input
    AantalLetters = int(input("Hoeveel letters wil je dat het woord heeft?"))
    if AantalLetters < 4:
        print(
            "We hebben geen woorden met zo weinig letters, probeer het opnieuw."
        )
        genereren_woord()
    elif AantalLetters == 4:
        woord_input = random.choice(woorden_4letters)
    elif AantalLetters == 5:
        woord_input = random.choice(woorden_5letters)
    elif AantalLetters == 6:
        woord_input = random.choice(woorden_6letters)
    elif AantalLetters == 7:
        woord_input = random.choice(woorden_7letters)
    elif AantalLetters == 8:
        woord_input = random.choice(woorden_8letters)
    elif AantalLetters == 9:
        woord_input = random.choice(woorden_9letters)
    elif AantalLetters == 10:
        woord_input = random.choice(woorden_10letters)
    elif AantalLetters > 10:
        print(
            "We hebben geen woorden met zo veel letters, probeer het opnieuw.")


#Met de volgende functie wordt aan speler 1 het woord gevraagd
def woord_maken():
    global woord_input, woord
    nieuweletter = ''
    #woord_input = str(woord_input)
    tellerA = int(AantalLetters)
    tellerB = 0
    while tellerA >= 1:
        nieuweletter = woord_input[tellerB]
        woord.append(nieuweletter)
        tellerA -= 1
        tellerB += 1


#Met deze functie maken we een lijst met daarin de bekende letters, zodat speler 2 niet gelijk het woord kan zien
def woord_bekend_maken():
    global woord_bekend
    tellerC = len(woord_input)
    while tellerC > 0:
        woord_bekend.append("_")
        tellerC -= 1


#laat speler1 kiezen zelf een woord te kiezen of een woord door de computer te laten genereren
def beurt_speler1_keuze():
    global AantalLetters, woord, woord_bekend, woord_input
    Antwoord = input("Wilt u tegen de computer spelen?(Ja of Nee)")
    if Antwoord == "Ja":
        genereren_woord()
        woord_maken()
        woord_bekend_maken()
    elif Antwoord == "Nee":
        input_vragen()
        woord_maken()
        woord_bekend_maken()
    else:
        print("Je hebt geen geldige input gegeven")
        beurt_speler1_keuze()


#Laat speler 2 een letter raden
def letter_raden():
    global AantalFouten, Gewonnen, Verloren, woord, woord_bekend
    letter_gekozen = input("Speler 2, welke letter wilt u kiezen?")
    AantalGevondenLetters = woord.count(letter_gekozen)
    if AantalGevondenLetters == 0:
        AantalFouten += 1
        FouteLetters.append(letter_gekozen)
        if AantalFouten == 11:
            Verloren = 1
        elif AantalFouten == 1:
            print("Je hebt nu 1 fout")
        else:
            print("Je hebt nu ", AantalFouten, " fouten")
    elif AantalGevondenLetters > 0:
        while AantalGevondenLetters > 0:
            PlaatsGeradenLetter = woord.index(letter_gekozen)
            woord_bekend.pop(PlaatsGeradenLetter)
            woord.pop(PlaatsGeradenLetter)
            woord_bekend.insert(PlaatsGeradenLetter, letter_gekozen)
            woord.insert(PlaatsGeradenLetter, "_")
            AantalGevondenLetters -= 1
    if woord_bekend == woord:
        Gewonnen = 1


#Laat speler 2 het woord raden
def woord_raden():
    global Aantal_WoordenGeraden
    global Gewonnen
    global Verloren
    woord_geraden = input("Speler 2, wat denk je dat het woord is?")
    if woord_geraden == woord_input:
        Gewonnen = 1
    else:
        Aantal_WoordenGeraden += 1
        print("Dit was helaas niet het juiste woord.")
        if Aantal_WoordenGeraden == 3:
            Verloren = 1


#Laat controleren of speler 2 al gewonnen of verloren heeft
def controleren_gewonnen_verloren():
    if Gewonnen == 1:
        print("Gefeliciteerd, dit was het juiste woord. Je hebt nu gewonnen.")
    elif Verloren == 1:
        print("Helaas, je hebt verloren.")
        print("Het juiste woord was ", woord_input)


#Geeft speler 2 de keuze een letter of het woord te raden
def beurt_speler2_keuze():
    keuze = input("Wilt u het woord al raden?(antwoord ja of nee)")
    if keuze == "ja":
        woord_raden()
    elif keuze == "nee":
        letter_raden()
    else:
        print("U heeft geen geldige input gegeven")


#laat de verschillende functies uitgevoerd worden zodat het spel kan starten
beurt_speler1_keuze()
while Gewonnen == 0 and Verloren == 0:
    print(" ".join(woord_bekend))
    if Gewonnen == 0:
        print('Foute Letters:')
        print(','.join(FouteLetters))
    beurt_speler2_keuze()
    controleren_gewonnen_verloren()
