a=input("ingresa input: \n")
parametros=a.split("}")

spli1=parametros[0].split(',')
spli2=parametros[1].split(',')
print(spli1)
print(spli2)

veces=[]
for i in range (0,len(spli1)):
    palabra="EQUIPO {}".format(i+1)
    suma=sum(palabra in string for string in spli2)
    veces.insert(i,suma) 

max=0
indices=[]
for i in range(0,len(veces)):
    if veces[i]>=max:
        max=veces[i]
        
for i in veces:
    if i==max:
        print("a",i)
        indices.insert(i,len(indices))
print(max)
print(veces)
print(indices)