---
interact_link: content/begynneropplaring/input.ipynb
title: 'Input'
prev_page:
  url: /begynneropplaring/tall_variable
  title: 'Tall og variable'
next_page:
  url: /begynneropplaring/tester
  title: 'Beslutninger'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Input

Input er en funksjon i Python som muliggjør brukerinteraksjon med en bruker av programmet i konsollen/terminalen som programmet kjøres i. Input tar kun ett argument. Dette argumentet kan være tomt, men det kan også være en streng, f.eks. et spørsmål. Dette er bare en veiledning til brukeren av programmet, så det har ingenting med hva det vi skriver inn tolkes som. Vi starter med et eksempel:



{:.input_area}
```python
navn = input("Hva heter du? ")
```


{:.output .output_stream}
```
Hva heter du? Arne

```

I konsollen vil spørsmålet dukke opp, og du vil måtte skrive inn noe etter spørsmålet. Når du trykker Enter, lagres det du skrev inn i variabelen navn. Hvis vi skriver inn f.eks. "Arne", vil koden ovenfor bli det samme som å skrive:



{:.input_area}
```python
navn = "Arne"
```


Uansett hva vi skriver inn i konsollen, vil det vi skriver inn tolkes som en streng (tekst). Hvis vi da f.eks. tar skriver et tall, vil datamaskinen tolke dette som en tekst. Dette kan vi se hvis vi prøver å legge sammen tallene:



{:.input_area}
```python
tall1 = input("Skriv inn et tall: ")
tall2 = input("Skriv inn et tall til: ")

print("Summen av tallene er:", tall1+tall2)
```


{:.output .output_stream}
```
Skriv inn et tall: 1
Skriv inn et tall til: 2
Summen av tallene er: 12

```

Den legger altså sammen strengen "1" og strengen "2". Dette blir "12", altså bare den ene strenger etterfulgt av den andre. Hvis vi istedenfor ønsker å legge dem sammen matematisk, må vi konvertere dem til tall. Dette gjør vi med funksjonen float() for desimaltall eller int() for heltall:



{:.input_area}
```python
tall1 = input("Skriv inn et tall: ")
tall2 = input("Skriv inn et tall til: ")

tall1 = float(tall1)
tall2 = float(tall2)

print("Summen av tallene er:", tall1+tall2)
```


{:.output .output_stream}
```
Skriv inn et tall: 1
Skriv inn et tall til: 2
Summen av tallene er: 3.0

```

Vi ser altså at det er viktig å vite hva slags variabeltyper vi har med å gjøre her. Merk også at input er en fin måte å ta inn variabler på, men dersom du skriver lange programmer som du ønsker å teste underveis, kan det bli plagsomt å måtte skrive inn input hver gang du tester. Bruk derfor heller enkle variabler med verdier først, og legg inn input til slutt når du vet at programmet fungerer.
