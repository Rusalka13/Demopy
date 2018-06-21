#coding:utf-8


edad=input("Indica tu edad:")
if int(edad) >= 18 :
    print ("pasa")
else: 
    print ("No pasa")

primera= input ("Escriba un número:")
segunda= input("Escriba un número mayor" + str(primera)+".")

# #bucle
# while int(segunda) > int(primera):
#     primera = segunda
#     segunda = int(input("Escribe un número mayor")+str(primera)+"."))

print("NO es mayor")
print("Final")

#te dice el radio
radio = input("indica un radio:")
diametro = int(radio) * int(radio)
#siempre con punto los decimales
Pi = 3.1415
area = Pi * diametro
print (area)
