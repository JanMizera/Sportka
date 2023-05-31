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
    return shoda

def sance_porovnavani(vyherni_cisla : list, vybrana_cisla : list) -> int:
    pocet_shod = 0
    index = 0
    while index < 10:
        cislo_A = vyherni_cisla.count(index)
        cislo_B = vybrana_cisla.count(index)
        pocet_shod = pocet_shod + pocitani_shod(cislo_A, cislo_B)
        if cislo_A != 0:
            for h in range(cislo_A):
                vyherni_cisla.remove(index)
        if cislo_B != 0:
            for g in range(cislo_B):
                vybrana_cisla.remove(index)
        index = index + 1
    return pocet_shod

def pocitani_shod(A : int, B : int) -> int:
    shody = 0
    if A > B:
        shody = B
    elif B > A:
        shody = A
    else:
        shody = A
    return shody        

def vyhra(pocet_shod : int) -> int:
    if pocet_shod != 0:
        return 10 ** (pocet_shod + 1)
    else:
        return 0

def vyhra_sance(pocet_shod : int) -> int:
    if pocet_shod != 0:
        return 10 ** pocet_shod
    else:
        return 0
    
opakuj = 1
penize = 1000
celkova_vyhra = 0

print("Za schodu jednoho čísla vyhrajete 100 Kč, za dvě 1 000 Kč, za tři 10 000 Kč atd. (nezáleží na pořadí)")
print("Cena slosování je 40 Kč")

while opakuj == 1 and penize > 40:
    osudi = list(range(1,50))
    sance = list(range(0,10))
    seznam_cisel = []
    seznam_sance = []
    seznam_cisel_1_vyhra = []
    seznam_cisel_2_vyhra = []
    seznam_sance_vyhra = []
    porovnavani1 = 0
    porovnavani2 = 0
    porovnavani_sance = 0
    penize = penize - 40
    vyhra_1 = 0
    vyhra_2 = 0
    vyhra_v_sanci = 0

    print("Vaše peníze jsou:",penize,"Kč")
    kombinace = int(input("Pokud si chcete vybrat vlastní čísla na slosování, stiskněte 1, pokud chcete vybrat čísla náhodně, stiskněte 2 nebo jakékoliv jiné celé číslo."))

    if kombinace == 1:
        while len(seznam_cisel) < 7:
            cislo = int(input("zadejte číslo od 1 do 49."))
            if 0 < cislo < 50 and seznam_cisel.count(cislo) < 1:      
                seznam_cisel.append(cislo)

            else:
                print("Číslo není v rozsahu nebo už bylo použito.")
        print("Vaše čísla:",seznam_cisel)
        
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
                
            else:
                print("Číslo není v rozsahu.")
        print("Vaše čísla:",seznam_sance)
        
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
    
    kopie_osudi = osudi.copy()
    while len(seznam_cisel_2_vyhra) < 7:
        cislo = nahoda(kopie_osudi)
        kopie_osudi.remove(cislo)
        seznam_cisel_2_vyhra.append(cislo)
    print("Vylosovaná čísla ve druhém tahu:",seznam_cisel_2_vyhra)

    while len(seznam_sance_vyhra) < 6:
        cislo_sance = nahoda_sance(sance)
        seznam_sance_vyhra.append(cislo_sance)
    print("Vylosovaná čísla v šanci:",seznam_sance_vyhra)
    
    print("Vaše čísla jsou:",seznam_cisel)
    print("Vaše čísla v šanci jsou:", seznam_sance)
    
    porovnavani1 = porovnavani(seznam_cisel_1_vyhra, seznam_cisel)
    porovnavani2 = porovnavani(seznam_cisel_2_vyhra, seznam_cisel)
    porovnavani_sance = sance_porovnavani(seznam_sance_vyhra, seznam_sance)
    
    print("Počet shod v prvním tahu je:", porovnavani1)
    print("Počet shod ve druhém tahu je:", porovnavani2)
    print("Počet shod v šanci je:", porovnavani_sance)

    vyhra_1 = vyhra(porovnavani1)
    vyhra_2 = vyhra(porovnavani2)
    vyhra_v_sanci = vyhra_sance(porovnavani_sance)
    
    print("Výhra v prvním tahu je:", vyhra_1, "Kč")
    print("Výhra ve druhém tahu je:", vyhra_2, "Kč")
    print("Výhra v šanci je:", vyhra_v_sanci, "Kč")
    
    penize = penize + vyhra_1 + vyhra_2 + vyhra_v_sanci
    
    print("Váš zůstatek je:", penize, "Kč")
    
    celkova_vyhra = celkova_vyhra + vyhra_1 + vyhra_2 + vyhra_v_sanci
    
    opakuj = int(input("Pro opakování stiskněte 1, pro ukončení jakékoliv jiné číslo."))

print("Vaše celková výhra je:", celkova_vyhra,"Kč")