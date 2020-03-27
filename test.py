msg = "sup world"
cpt = "FN"
print(msg + " Ya cool")
print("hello " + msg.title())
print(msg.upper())
print(cpt.lower() + " " + msg.upper())

nota1 = float (input("Nota 1: "))
nota2 = float (input("Nota 2: "))
media = (nota1 + nota2) /2

if media < 6:
    print("reproved")
else:
    print("approved")