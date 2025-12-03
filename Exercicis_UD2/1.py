temperatura= float(input("Passam la temperatura"))
nuvolat = input("Esta nuvolat? (si/s)")

if nuvolat.lower() == "si" or nuvolat.lower() == "s":
    nuvolat = True
else:
    nuvolat = False

if(temperatura<=0):
     if (nuvolat):
        print("Fa un fred polar!")
elif temperatura >=0 and temperatura <=15:
     if (nuvolat):
        print("Fa fred i el dia està trist.")
     else:
        print("Fa fresquet pero el sol alegra el dia")
elif temperatura >=16 and temperatura <=25:
     if (nuvolat):
        print("Temperatura agradable, pero potser ploga")
     else:
        print("Dia perfecte per a passejar")
elif temperatura >35:
    if (nuvolat):
        print("Calor i humitat... combinació infernal!")
    else:
         print("Fa un calor que fon les pedres")