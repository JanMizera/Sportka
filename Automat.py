import random

def nahoda(osudi : list) -> int:
    cislo_v_osudi = random.choice(osudi)
    return cislo_v_osudi

def nahoda_sance(osudi_sance : list) -> int:
    cislo_v_osudi_sance = random.choice(osudi_sance)
    return cislo_v_osudi_sance

def porovnavani(vyherni_cisla : list, vybrana_cisla : list) -> int:
    shoda = 0
    for x in vyherni_cisla:
        for y in vybrana_cisla:
            if x == y:
                shoda = shoda + 1
                pass
    return shoda

def vyhra(pocet_shod : int) -> int:
    if pocet_shod == 1:
        return 100
    elif pocet_shod == 2:
        return 1000
    elif pocet_shod == 3:
        return 10000
    elif pocet_shod == 4:
        return 100000
    elif pocet_shod == 5:
        return 1000000
    elif pocet_shod == 6:
        return 10000000
    elif pocet_shod == 7:
        return 100000000
    else:
        return 0
    
opakuj = 1
penize = 1000
celkova_vyhra = 0

print("Za schodu jednoho čísla vyhrajete 100 Kč, za dvě 1 000 Kč, za tři 10 000 Kč atd. (nezáleží na pořadí)")
print("Cena slosování je 40 Kč")

while opakuj == 1 and penize > 40:
    osudi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    sance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    seznam_cisel = []
    seznam_sance = []
    seznam_cisel_1_vyhra = []
    seznam_cisel_2_vyhra = []
    seznam_sance_vyhra = []
    porovnavani1 = 0
    porovnavani2 = 0
    porovnavani_sance = 0
    penize = penize - 40

    print("Vaše peníze jsou:",penize,"Kč")
    kombinace = int(input("Pokud si chcete vybrat vlastní čísla na slosování, stiskněte 1, pokud chcete vybrat čísla náhodně, stiskněte 2 nebo jakékoliv jiné celé číslo."))

    if kombinace == 1:
        while len(seznam_cisel) < 7:
            cislo = int(input("zadejte číslo od 1 do 49."))
            if 0 < cislo < 50 and seznam_cisel.count(cislo) < 1:      
                seznam_cisel.append(cislo)
                print("Vaše čísla:",seznam_cisel)
            else:
                print("Číslo není v rozsahu nebo už bylo použito.")
    else:
        kopie_osudi = osudi.copy()
        while len(seznam_cisel) < 7:
            cislo = nahoda(kopie_osudi)
            kopie_osudi.remove(cislo)
            seznam_cisel.append(cislo)
            print("Vaše čísla:",seznam_cisel)

    kombinace_na_sanci = int(input("Pokud si chcete vybrat vlastní čísla na šanci, stiskněte 1, pokud chcete vybrat čísla náhodně, stiskněte 2 nebo jakékoliv jiné celé číslo."))

    if kombinace_na_sanci == 1:
        while len(seznam_sance) < 6:
            cislo_sance = int(input("zadejte číslo od 0 do 9."))
            if 0 <= cislo_sance <= 9:      
                seznam_sance.append(cislo_sance)
                print("Vaše čísla:",seznam_sance)
            else:
                print("Číslo není v rozsahu.")

    else:
        while len(seznam_sance) < 6:
            cislo_sance = nahoda_sance(sance)
            seznam_sance.append(cislo_sance)
            print("Vaše čísla:",seznam_sance)


    print("Slosování začíná")
    
    kopie_osudi = osudi.copy()
    while len(seznam_cisel_1_vyhra) < 7:
            cislo = nahoda(kopie_osudi)
            kopie_osudi.remove(cislo)
            seznam_cisel_1_vyhra.append(cislo)
            print("Vylosovaná čísla v prvním tahu:",seznam_cisel_1_vyhra)
    print("Vaše čísla:", seznam_cisel)
    
    kopie_osudi = osudi.copy()
    while len(seznam_cisel_2_vyhra) < 7:
            cislo = nahoda(kopie_osudi)
            kopie_osudi.remove(cislo)
            seznam_cisel_2_vyhra.append(cislo)
            print("Vylosovaná čísla ve druhém tahu:",seznam_cisel_2_vyhra)
    print("Vaše čísla:", seznam_cisel)

    while len(seznam_sance_vyhra) < 6:
        cislo_sance = nahoda_sance(sance)
        seznam_sance_vyhra.append(cislo_sance)
        print("Vylosovaná čísla v šanci:",seznam_sance_vyhra)
    print("Vaše čísla:", seznam_sance)
    
    print("Vylosovaná čísla v prvním tahu jsou:", seznam_cisel_1_vyhra)
    print("Vylosovaná čísla ve druhém tahu jsou:", seznam_cisel_2_vyhra)
    print("Vaše čísla jsou:",seznam_cisel)
    print("Vylosovaná čísla v šanci jsou:", seznam_sance_vyhra)
    print("Vaše čísla v šanci jsou:", seznam_sance)
    
    porovnavani1 = porovnavani(seznam_cisel_1_vyhra, seznam_cisel)
    porovnavani2 = porovnavani(seznam_cisel_2_vyhra, seznam_cisel)
    porovnavani_sance = porovnavani(seznam_sance_vyhra, seznam_sance)
    
    print("Počet shod v prvním tahu je:", porovnavani(seznam_cisel_1_vyhra, seznam_cisel))
    print("Počet shod ve druhém tahu je:", porovnavani(seznam_cisel_2_vyhra, seznam_cisel))
    print("Počet shod v šanci je:", porovnavani(seznam_sance_vyhra, seznam_sance))

    vyhra_1 = vyhra(porovnavani1)
    vyhra_2 = vyhra(porovnavani2)
    vyhra_sance = vyhra(porovnavani_sance)
    
    print("Výhra v prvním tahu je:", vyhra_1, "Kč")
    print("Výhra ve druhém tahu je:", vyhra_2, "Kč")
    print("Výhra v šanci je:", vyhra_sance, "Kč")
    
    penize = penize + vyhra_1 + vyhra_2 + vyhra_sance
    
    print("Váš zůstatek je:", penize, "Kč")
    
    celkova_vyhra = celkova_vyhra + vyhra_1 + vyhra_2 + vyhra_sance
    
    opakuj = int(input("Pro opakování stiskněte 1, pro ukončení jakékoliv jiné číslo."))

print("Vaše celková výhra je:", celkova_vyhra,"Kč")