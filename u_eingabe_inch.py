# Eingabe in Inch
print("Bitte eine Zahl eingeben:")
z = input()

# Eingabe in Zahl umwandeln
zahl = float(z)

# Ausgabe der Eingabe
print("Ihre Eingabe:", z)

# Umrechnung von Inch in Zentimeter
umrechnungsfaktor = 2.54
ergebnis = zahl * umrechnungsfaktor

# Ausgabe des Ergebnisses
print("Das entspricht", ergebnis, "Zentimetern.")

