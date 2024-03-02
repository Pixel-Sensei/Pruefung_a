# Der Text "internet" wird in der Variable 'text' gespeichert.
text = "internet"

# Eine Schleife wird gestartet, die über jedes Zeichen im Text iteriert.
for i in text:
    # Wenn das aktuelle Zeichen 'i' gleich "e" ist, wird die Schleife mit 'break' abgebrochen.
    if i == "e":
        break
    # Wenn 'i' nicht gleich "e" ist, wird das Zeichen gedruckt. 'end=""' bewirkt, dass kein Zeilenumbruch nach dem Drucken erfolgt.
    print(i, end="")
