import random
javab = random.randint(1,99)
hads = input( "what is your hads?")
javab=int(javab)
hads=int(hads)
while hads !=javab:
    if hads>javab:
        print("smaller")
    else:
        print("bigger")
    hads= input ("what is your hads?")
    hads= int(hads)
    

print ("afarin hala ridam barat")   
    