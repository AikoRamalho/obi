#Nesse problema, ele pede para você printar S caso seja impedimento, e printar N caso nao seja.
#Problema com dificuldade facil, sem necessidade de implementação de algoritimos complicados.

l, r, d = map(int, input("").split(" ")) #Nessa linha estou passando o tipo inteiro aos input.split
if(r>50 and l<r and r>d): #Checa a condição de impedimento
    print("S")
else:
    print("N")
