# Definition der Funktion 'func' mit einem Parameter 'n'
def func(n):
    # Wenn 'n' modulo 2 gleich 0 ist (d.h., 'n' ist gerade), geben wir 'n' zurück
    if n % 2 == 0:
        return n
    # Wenn 'n' modulo 2 nicht gleich 0 ist (d.h., 'n' ist ungerade), geben wir 5 zurück
    else:
        return 5

# Wir rufen die Funktion 'func' mit dem Argument 'func(7)' auf und drucken das Ergebnis
# Da 'func(7)' gleich 5 ist (weil 7 ungerade ist), ist dies dasselbe wie 'func(5)'
# Da '5' ungerade ist, gibt die Funktion 5 zurück
print(func(func(7)))  # Ausgabe: 5

