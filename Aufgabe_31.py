x = 1       # x wird als Ganzzahl (int) mit dem Wert 1 initialisiert
y = "1"     # y wird als Zeichenkette (string) mit dem Wert "1" initialisiert
z = 1.0     # z wird als Gleitkommazahl (float) mit dem Wert 1.0 initialisiert

# Erste Bedingung: x ist gleich y (numerischer Vergleich mit Zeichenkette)
if x == y:
    print("one")    # Wird nicht ausgeführt, da x und y verschiedene Datentypen haben (int vs. string)

# Zweite Bedingung: y wird in eine Ganzzahl umgewandelt und mit z verglichen
if y == int(z):
    print("two")    # Wird ausgeführt, da die Zeichenkette "1" in die Ganzzahl 1 umgewandelt wird und mit z (1.0) übereinstimmt

# Da die vorherige if-Bedingung nicht mit dieser elif-Bedingung verbunden ist, wird diese Bedingung als Teil eines neuen if-elif-else Blocks betrachtet
elif x == y:
    print("three")  # Wird nicht ausgeführt, da x und y verschiedene Datentypen haben (int vs. string)

# Diese else-Bedingung wird ausgeführt, da keine der vorherigen Bedingungen in diesem if-elif-else Block erfüllt ist
else:
    print("four")   # Wird ausgeführt und "four" ausgegeben
