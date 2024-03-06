# Zuerst werden zwei Variablen, a und b, mit den Werten 0 und 1 initialisiert.
a = 0
b = 1

# Dann wird eine bitweise ODER-Operation auf a und b ausgeführt.
# Die ODER-Operation gibt 1 zurück, wenn mindestens eines der Bits 1 ist.
# Da b 1 ist, wird das Ergebnis der Operation auch 1 sein, unabhängig vom Wert von a.
# Daher wird a jetzt 1.
a = a | b

# Anschließend wird eine bitweise UND-Operation auf a und b ausgeführt.
# Die UND-Operation gibt 1 zurück, wenn beide Bits 1 sind.
# Da sowohl a als auch b jetzt 1 sind, wird das Ergebnis der Operation 1 sein.
# Daher wird b jetzt 1.
b = a & b

# Schließlich werden die Werte von a und b ausgegeben.
# Da sowohl a als auch b 1 sind, wird die Ausgabe (1, 1) sein.
print(a, b)
