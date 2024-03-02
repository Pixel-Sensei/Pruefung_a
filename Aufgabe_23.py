# Der Code beginnt mit einem 'try'-Block. Dieser Block enthält Code, der eine Ausnahme (einen Fehler) auslösen könnte.
try:
    # Der Code versucht, 7 durch 0 zu teilen, was in Python zu einem ZeroDivisionError führt.
    print(7/0)

# Wenn im 'try'-Block ein ZeroDivisionError auftritt, wird der Code im 'except'-Block ausgeführt.
except (ZeroDivisionError):
    # Wenn ein ZeroDivisionError auftritt, wird die Nachricht "Zero division error" ausgegeben.
    print("Zero division error")

# Der 'else'-Block wird nur ausgeführt, wenn im 'try'-Block keine Ausnahme auftritt.
else:
    # Da im 'try'-Block immer eine Ausnahme auftritt (weil die Division durch Null nicht erlaubt ist), wird dieser Code nie ausgeführt.
    print("Infinity")
