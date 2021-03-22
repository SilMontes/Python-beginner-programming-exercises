# print "Hello World!" on the 

#print("Hello World!")
#birth_year=input("What is your birth year?\n")
#age=2021-int(birth_year)
#print("Hello "+str(age))


#first=input("Firs number ")
#second=input("Second number ")

#total=int(first)+int(second)
#print(total)


first=int(input("Firs number "))
second=int(input("Second number "))

total=first+second
print(total)

#Manipulando strings, los strings son casi inmutables en python
name="Silvia Caro Montes "
print(name.upper(), name.lower(), name.find("l"))
print(name.find("caro")) #imprime -1 porque es python es sensible  a las minúsculas y las mayúsculas
print(name.find("Caro")) #imprime el indedx de la palabra
print(name.replace("Caro Montes", "is my name"))
print("Silvia" in name) #esto devuelve falso o verdadero


# Arithmetic Operations

x=10
x += 3
y=10
y -= 3
m=10
m *= 3
s=10
s /= 3 #devuelve decimales
k=10
k //=3 #devuelve entero
print(x, y, m, s, k)

#Operator Precedence

x = 10 + 3 * 2
print(x)

#si queremos que se realice primero la suma, debemos agregarla entre parentisis

y= (10+3) * 2
print(y)

#Comparison Operators   <, >, ==, !=, <=, >=

x = 3 > 2 #true

#Logical Operators     and, or, not

price = 25
print( price > 10 and price < 30) #true

price = 25
print(price >30) #false

price = 25
print(not price >30) #true

#if statement

temperature = 25
if temperature > 30:
    print("It's a hot day")
elif temperature > 20: #(20, 30]
    print("It's a nice day")
elif temperature > 10: #(10, 20]
    print("It's a bit cold")
else:
    print("It's cold")

#excersice if
weight=int(input("Weight: "))
unit="KG"
if unit.lower()=="kg":
   converted=int(weight/0.45)
   print("Weight in kg: "+ str(converted))
else:
    converted=int(weight*0.45)
    print("Weight in pounds: "+ str(converted))


#while loop
number_colors=1
while number_colors<=50:
    print(number_colors)
    number_colors+=1
#second example whilw loop
number_colors=1
while number_colors<=10:
    print(number_colors * '*') #el asterisco se multiplicará según el valor de number_colors, no aparecerá el valor de i
    number_colors+=1

#third example while loop
numbers=[1,2,3,4,5,6]
i=0
while i<len(numbers):
    print(numbers[i])
    i+=1

#list
names = ["John", "Sil", "Ana", "Lily", "Joshua", "Martha"]
print(names) #everythin will be printed, even the square braquets
print(names[0]) #the name in the position 0 will be printed
print(names[-1]) #-1 represents the last element of the list
print(names[-2]) # represents the second element from the end of the list
names[1]="Silvia" #the element at the given position will be change
print(names)
print(names[0:3]) #to print a range of elements, the element at the last positon given will be excluded, in this case position 3

#list methods

numbers=[1,2,3,4,5,6,7,8,9,11,12,13,14]
#numbers.append(15) #añade al final el elemento 15
numbers.insert(4,6) #esto recibe como parametros: index=dónde se agregará el nuevo elemento y object:_T = el valor del elemento Este metodo no elimina el elemento en esa posición
print(numbers)
numbers.remove(9) #remueve ese elemento,  no importa en qué index esté
print(numbers)
numbers.clear() #elimina todo los elementos
print(numbers)


numbers2=[1,2,3,4,5,6,7,8,9,11,12,13,14]
# para saber si un elemento existe en la lista, realizamos lo siguiente.
print(6 in numbers2)
#saber cuátos elementos hay en una lista
print(len(numbers2))

#for loops
numbers=[1,2,3,4,5,6]
for number in numbers:
    print(number)

#the range() function TO GENERATE A SEQUENCE OF NUMBERS

numbers = range(5) #obtenemos los numeros 0 a 5, pero excluimos 5. Par ver los números, tenemos que itinerar por la lista
for number in numbers:
    print(number)

# si proveemos dos valores, el primer valor va a ser el inicial y el segundo en final y será excluido
numbers2=range(7,20)
for number in numbers2:
    print(number)

#si proveemos un tercer número, saltaremos segun ese número. 
print("los numeros aumentaran de dos en dos, iniciando con el 20 y excluyendo el 40")
numbers3=range(20,40,2)
for number in numbers3:
    print(number)

#podemos usar el range directamente en el for
for item in range(0,11,3):
    print(item)


#TUPLES: are inmutable, we cannot change them. We use square brackets to declare a list, but parenthesis to declare a tuple
#we can only count them (how many times an element is repeated)
names=("Sil","Ana","Sil","Oscar","Lily")
print(names.count("Sil")) 

#and we can also know the index of the first ocurrence of the given item
numbers=(1,2,3,4,5)
print(numbers.index(2)) #the index of 2 is 1




