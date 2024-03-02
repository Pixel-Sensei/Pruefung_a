# Definieren eines Tupels mit den Elementen 'a', 'b' und 'c'
my_tuple = ('a', 'b', 'c')

# Neuzuweisung von my_tuple, wobei 'b' aus dem Tupel entfernt wird
# Dies wird erreicht, indem ein neues Tupel erstellt wird, das nur die Elemente enthält, die nicht 'b' sind.
my_tuple = tuple(x for x in my_tuple if x != 'b')

# Ausgabe des neuen Tupels, nachdem 'b' entfernt wurde
print(my_tuple)
