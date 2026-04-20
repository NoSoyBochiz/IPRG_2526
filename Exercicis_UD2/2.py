print("Classificador d'alumnes per edat i assistència")

n = int(input("Quants alumnes vols processar? "))
i = 0 #Començaba per 1, per tant el ultim element no el tractaba

while i < n:
    nom = input("Nom: ")
    edat = input("Edat: ")
    assist = input("Assistència (S/N): ").lower()

    if edat < 12:
        categoria = "infantil"
    elif edat > 12 and edat < 18:
        categoria = "adolescent"
    elif edat >= 19 and edat < 65: #he cambiat el 18 per 19 per evitar erorrs amb la categoria Adolescent
        categoria = "adult"
    else:
        categoria = "jubilat"

    if assist == "S": #He cambiat les opcions de s/si per S per a que s'execute el codi
        estat = "present"
    else:
        estat = "absent"

    print(nom, "-", categoria, "-", estat)
    i = i + 1