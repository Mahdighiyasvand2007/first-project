import random
javab = random.randint(1,99)
name=input("what is your name?")
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
print ("afarin hala ridam barat",name)  
bazimojadad=input ("mikhay dobarebazi koni?")
if bazimojadad == "y":
    print ("be tokhmam ")
    print ("\u1F595")
