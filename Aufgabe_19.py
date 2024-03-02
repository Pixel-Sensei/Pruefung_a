# Definition der Funktion "func" mit zwei Parametern: x und y
def func(x, y):
    # Die Funktion gibt das Ergebnis des Ausdrucks "(y // 2 - 1) ** x" zurück.
    # "//" ist der Operator für die Ganzzahldivision in Python, der das Ergebnis der Division ohne den Rest zurückgibt.
    # "**" ist der Exponentenoperator in Python.
    # Daher teilt dieser Ausdruck zuerst y durch 2, subtrahiert 1 und erhebt das Ergebnis zur Potenz x.
    return((y // 2 - 1) ** x)

# Der Wert der Funktion "func" wird mit den Argumenten 2 und 7 berechnet und ausgegeben.
print(func(2, 7))
