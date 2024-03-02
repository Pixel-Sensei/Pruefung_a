# Initialisiere die Liste var1 mit den Elementen 0, 1 und 2
var1 = [0, 1, 2]

# Die for-Schleife läuft von 0 bis 1 (da range(2) die Zahlen 0 und 1 erzeugt)
for i in range(2):
    # In jedem Durchlauf der Schleife wird der aktuelle Wert von i am Anfang der Liste eingefügt
    var1.insert(0, i)

# Drucke die endgültige Liste
print(var1)
