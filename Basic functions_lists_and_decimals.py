

############### Functions ####################

# Returning a print as the product isnt always a good idea, but it does work in this simple case. 

def min_gange_funksjon(a,b):
    resultat=a*b
    return print(resultat)

def min_dele_funksjon(a,b):
    resultat=a/b
    return print(resultat)

min_gange_funksjon(1,2)
min_dele_funksjon(1,2)

# Here I rather print the result

def min_gange_funksjon(a,b):
    resultat=a*b
    return resultat

def min_dele_funksjon(a,b):
    resultat=a/b
    return resultat

print(min_gange_funksjon(1,2))
print(min_dele_funksjon(1,2))


############### Nesting a for loop within a function #######################

# Creating a fibbonaci code. Adding a for loop to give it a min value (or else it wont work as the function works backwards)

def fib(n):
    if n<=2: 
        return 1
    resultat = fib(n-1)+fib(n-2)
    return resultat

fib(1)



######################### Some easy list work ###############

my_list= [1, 4, 9, 6,6, 7, 2,3]
my_list.append(5)
my_list.append(8)
my_list.remove(6)
my_list.sort()
my_list.pop() # (to extricate a value from the list)



################## F-string and decimals ####################

var=3.1415
print("%.2f"%var)
print("%.0f"%var)
print("%.1f"%var)
print("%.3f"%var)
print(f"denne koden printer denne variablen {var}")


########################### .zfill() ###########################

# zfill fyller inn 0er før celleverdien til antall elementer er 3 (i dette tilfellet). zfill er sensitiv Nan så de vil ikke bli fylt

df['var2'] = df['var1'].str.zfill(3)

# Om vi derimot ønsker å fylle alle cellene med en string verdi ('0' i dette tilfellet) så bruker vi koden under

df['var2'] = ('0' + df['var1'].astype(str))












