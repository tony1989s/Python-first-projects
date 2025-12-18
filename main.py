"""
CALCOLATRICE SEMPLICE
Autore: Antonino Spataro
"""


# Calcolatrice con variabili e tipi di dati

numero1 = 10
numero2 = 5

somma = numero1 + numero2
differenza = numero1 - numero2
prodotto = numero1 * numero2
quoziente = numero1 / numero2

print("Somma:", somma)
print("differenza:", differenza)
print("Prodotto", prodotto)
print("Quoziente:", quoziente)



"""
SISTEMA DI LOGIN BASE
Autore: Antonino Spataro
"""

# Sistema di Login Base (con boolean)
utente_corretto = "admin"
password_corretta = "password123"

# Input utente (simulato)
username_inserito = "admin"
password_inserita = "password123"

# Verifica con boolean
verifica_user = username_inserito == utente_corretto
verifica_password = password_inserita == password_corretta

accesso_autorizzato = verifica_user and verifica_password

print("Username corretto:", verifica_user)
print("Password corretta:", verifica_password)
print("Accesso autorizzato:", accesso_autorizzato)