mat = [[x for x in range(2)] for y in range(2)]  # Erstellt eine 2x2-Matrix
sums = 0  # Initialisiert 'sums' auf 0

for row in range(2):
    for column in range(2):
        sums += mat[row][column]  # Addiert jedes Element der Matrix zu 'sums'

print(sums * "#")  # Gibt '#' so oft aus wie der Wert von 'sums'
