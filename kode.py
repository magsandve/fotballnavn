quiz= "skriv etternavnet på en fotballspiller"
print(quiz)
#etternavn= input()
etternavn="Dybala"

skriv="hva er fornavnet til  "
print(skriv  +  etternavn)
#fornavn=input()
fornavn="Paulo"
print(fornavn)
if etternavn== "Dybala":
    if fornavn== "Paulo":
        print("Du klarte det")
        riktig=1
    elif fornavn== "paulo":
        print("husk stor forbokstav")
    else:
        print("du klarte det ikke")
        riktig=2
elif etternavn== "Messi":
    if fornavn== "Lionel":
        print ("Du klarte det")
        riktig=1
    elif fornavn== "lionel":
        print ("husk stor bokstav")
        riktig=2
    else:
        print ("Du klarte det ikke")
elif etternavn== "Ronaldo":
    if fornavn== "Cristiano":
        print ("Du klarte det")
        riktig=1
    elif fornavn== "cristiano":
        print ("husk stor bokstav")
    else:
        print ("Du klarte det ikke")
else:
    print ("denne spilleren fins ikke på quizen")
if riktig== 1:

    print ("Du får en bonus")
    print ("hvor gammel er "  + etternavn)
    #tekstalder=input()
    tekstalder="23"
    print (tekstalder)
    print ("om et år er han ")
    tall=int(tekstalder)
    print(tall+ 1)
    ar= 2020
    print ("har han hatt burstag i år. (skriv ja eller nei)")
    #bursdag=input()
    bursdag="nei"
    print(bursdag)
    print ("da er han født i")
    if bursdag== "ja":
        print (ar-tall)
    elif bursdag== "nei":
        print (ar-tall-1)
    else:
        print ("husk å skriv ja eller nei")

print("hvilket land er " + etternavn + " fra" + "?")
land=input()
while not land== "Argentina":
    print("feil Land prøv igjen!")
    land= input()
    if land== "Argentina":
        print("Du klarte det")
