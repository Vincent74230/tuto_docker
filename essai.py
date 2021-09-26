print ('Bienvenue sur le générateur de Fibonnacci')

print('entrez un nombre : ')

n = input()

try:
    n = int(n)
except ValueError:
    print("J'ai dit un nombre, trou d'cul!")

print (type(n), n)


l = [1,1]
for i in range (1,n):
    x = l[i] + l[i-1]
    l.append(x)

print(l)
