dct = {"one": "two", "two": "three", "three": "one"}  # Erstellen Sie ein Wörterbuch
v = dct["one"]  # Setzen Sie v auf den Wert des Schlüssels "one" im Wörterbuch (also "two")

for i in range(len(dct)):  # Starten Sie eine Schleife, die so viele Durchläufe hat wie das Wörterbuch Einträge hat
    v = dct[v]  # Setzen Sie v auf den Wert des Schlüssels im Wörterbuch, der dem aktuellen Wert von v entspricht

print(v)  # Geben Sie den endgültigen Wert von v aus
