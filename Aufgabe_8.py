import pandas as pd


table1 = pd.read_csv('table1.csv')

# a) Bei Listen werden keine () verwendet
print(table1('digits', 'numbers'))

#b) Richtig,
print(table1[['digits', 'numbers']])

#c) falsch, weiss nicht wohin mit der Liste
print(table1['digits', 'numbers'])

#d) falsch, denkt das sind Variablen
print(table1(digits, numbers))



