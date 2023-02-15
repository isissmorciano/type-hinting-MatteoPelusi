import random
#Pelusi Matteo
#ese 1

#Creare una funzione descrizione() con due parametri nome ed eta.
#La funzione restituisce una stringa formattata nel seguente modo:
#"nome ha eta anni." descrizio ("Pippo",23)

def descrizione(nome:str , eta:int)-> int:
    return f"{nome} ha {eta} anni."
print(descrizione("Pippo",23))
print("-------------------------------------------------------------------")

#ese 2

#Creare una funzione(?) numero_casuale() che restituisce un numero casuale tra 0 e 99.
#La funzione restituisce il numero generato numero_casuale()

def numero_casuale()-> int:
    return random.randint(0,99)
print(numero_casuale())
print("-------------------------------------------------------------------")

#ese 3

#Creare una funzione descrizione_eta_casuale() con un parametro nome.
#L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo:
#"nome ha eta anni." descrizione_eta_casuale("Pippo")

def descrizione_eta_casuale(nome:str)-> str:
    eta=numero_casuale()
    return descrizione(nome,eta)
print(descrizione_eta_casuale("Pippo"))
print("-------------------------------------------------------------------")

#ese 4

#Creare una funzione(?) descrizione_casuale(). 
#Il nome e' scelto in modo casuale da una lista di nomi interna alla fuzione.
#L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo:
#"nome ha eta anni." descrizione_casuale()

def descrizione_casuale()-> str:
    nomi=["Paolo","Davide","Fiulio","Marco","Francesco"]
    nome=random.choice(nomi)
    eta=numero_casuale()
    return descrizione(nome,eta)
print(descrizione_casuale())
print("-------------------------------------------------------------------")