# Definition der Funktion 'recurs' mit einem Parameter 'n'
def recurs(n):
    # Wenn 'n' modulo 3 gleich 1 ist, rufen wir die Funktion 'recurs' erneut auf und reduzieren 'n' um 1
    if n % 3 == 1:
        return recurs(n-1)
    # Wenn 'n' modulo 3 nicht gleich 1 ist, geben wir 3 zurück
    else:
        return 3

# Wir rufen die Funktion 'recurs' mit dem Argument 9 auf und drucken das Ergebnis
# Da 9 modulo 3 gleich 0 ist, gibt die Funktion sofort 3 zurück, ohne sich selbst aufzurufen
print(recurs(9))  # Ausgabe: 3
