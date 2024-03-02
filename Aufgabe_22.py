# Ein leeres Wörterbuch namens 'dct' wird erstellt.
dct = {}

# Dem Wörterbuch 'dct' wird ein Schlüssel 'a' mit dem Wert ('a', 'b') hinzugefügt.
dct['a'] = ('a', 'b')

# Dem Wörterbuch 'dct' wird ein weiterer Schlüssel 'b' mit dem Wert ('c', 'd') hinzugefügt.
dct['b'] = ('c', 'd')

# Eine Schleife wird gestartet, die über alle Schlüssel im Wörterbuch 'dct' iteriert.
for x in dct.keys():
    # Für jeden Schlüssel 'x' wird das zweite Element des zugehörigen Wertes (ein Tupel) ausgegeben,
    # gefolgt von der Zeichenkette "2". 'end="2"' bewirkt, dass anstelle eines Zeilenumbruchs "2" ausgegeben wird.
    print(dct[x][1], end="2")
