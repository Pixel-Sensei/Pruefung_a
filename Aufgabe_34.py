# Eine Funktion namens 'func' wird definiert, die eine Liste als Parameter nimmt
def func(list):
    # Eine Variable namens 'value' wird initialisiert und auf 0 gesetzt
    value = 0
    # Eine for-Schleife wird gestartet, die drei Durchläufe hat
    for i in range(3):
        # In jedem Durchlauf der Schleife wird der Wert des i-ten Elements der Liste zu 'value' addiert
        value += list[i]
    # Nachdem alle Elemente der Liste addiert wurden, wird 'value' zurückgegeben
    return value

# Die Funktion 'func' wird mit einer Liste von zwei Elementen [5, 7] als Argument aufgerufen
# Da die Funktion versucht, auf das dritte Element der Liste zuzugreifen (was nicht existiert), wird ein IndexError ausgelöst
print(func([5, 7]))
