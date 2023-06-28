#import io 
nombres= ["juan", "Luis"]
archivo=open("archi.txt", "w")
archivo.write("asd")
for nombre in nombres:
    archivo.write(nombre + "\n")
archivo.close()