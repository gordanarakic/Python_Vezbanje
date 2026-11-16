"""
VEŽBE: liste, tuple, setovi, rečnici (dict)
============================================

Kako se radi:
  1. Svaki zadatak je jedna funkcija. Opis zadatka i primer su u docstring-u.
  2. Obriši `raise NotImplementedError` i napiši rešenje.
  3. Pokreni fajl:   python vezbe.py
     Na dnu se ispisuje koji zadaci su tačni (OK), a koji nisu (X).

Pravilo: bez importovanja bilo čega, osim tamo gde zadatak kaže drugačije.
"""

# =====================================================================
# 1. LISTE
# =====================================================================

def zad_01_parni(brojevi):
    """Vrati novu listu samo sa parnim brojevima.

    [1, 2, 3, 4, 5, 6]  ->  [2, 4, 6]
    Probaj prvo for petljom, pa list comprehension-om.
    """
    # TODO
    nova_lista=[]
    # for i in brojevi:
    #     if(i%2==0):
    #         nova_lista.append(i)
    # return nova_lista

    nova_lista = [i for i in brojevi if i%2==0]
    return nova_lista
    


def zad_02_kvadrati(n):
    """Vrati listu kvadrata brojeva od 1 do n (uključujući n).

    4  ->  [1, 4, 9, 16]
    """
    # TODO
    nova_lista=[]
    for i in range(n):
        nova_lista.append((i+1)**2)
    return nova_lista



def zad_03_drugi_najveci(brojevi):
    """Vrati drugi najveći RAZLIČIT broj u listi.

    [5, 1, 9, 9, 3]  ->  5
    Savet: sorted, set, ili dve promenljive u petlji.
    """
    # TODO
    nova_lista=sorted(brojevi,reverse=True)
    i=1
    max=nova_lista[1]
    brojac=0
    while True:
        for i in nova_lista:
            if max==i:
                brojac+=1
        if brojac==1:
            return max
        else:
            i+=1
            max=nova_lista[i]
            brojac=0

    


def zad_04_obrni_bez_reverse(lista):
    """Vrati obrnutu listu, ali BEZ .reverse() i reversed().

    [1, 2, 3]  ->  [3, 2, 1]
    Savet: slicing [start:stop:korak]
    """
    # TODO
    nova_lista=lista
    for i in range(1,len(lista)):
        poslednji=nova_lista[-1]
        nova_lista=nova_lista[:-1]
        nova_lista.insert(i-1,poslednji)
    print(nova_lista)
    return nova_lista


def zad_05_spljosti(lista_listi):
    """Pretvori listu listi u jednu listu.

    [[1, 2], [3], [], [4, 5]]  ->  [1, 2, 3, 4, 5]
    """
    # TODO
    nova_lista=[]
    for i in lista_listi:
        for j in range(len(i)):
            nova_lista.append(i[j])
    print(nova_lista)
    return nova_lista



def zad_06_podeli_na_delove(lista, velicina):
    """Podeli listu na delove zadate veličine (poslednji može biti kraći).

    [1, 2, 3, 4, 5], 2  ->  [[1, 2], [3, 4], [5]]
    Savet: range(0, len(lista), velicina) i slicing.
    """
    # TODO
    nova_lista=[]
    for i in range(0,len(lista),velicina):
        nova_lista.append(lista[i:i+velicina])
    print(nova_lista)
    return nova_lista


def zad_07_bez_duplikata_red_ostaje(lista):
    """Ukloni duplikate, ali zadrži REDOSLED prvog pojavljivanja.

    [3, 1, 3, 2, 1]  ->  [3, 1, 2]
    (set(lista) ne čuva redosled! Kombinuj listu i set.)
    """
    # TODO
    nova_lista=[]
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    return nova_lista



# =====================================================================
# 2. TUPLE
# =====================================================================

def zad_08_min_max(brojevi):
    """Vrati tuple (najmanji, najveći).

    [4, 9, 1, 7]  ->  (1, 9)
    """
    # TODO
    tup=(min(brojevi),max(brojevi))
    
    return tup


def zad_09_zameni(par):
    """Primi tuple od dva elementa i vrati ga sa zamenjenim mestima.

    (1, "a")  ->  ("a", 1)
    Savet: raspakivanje   a, b = par
    """
    # TODO
    a,b=par
    tup=(b,a)
    return tup


def zad_10_sortiraj_po_godinama(osobe):
    """Lista tuplova (ime, godine). Vrati je sortiranu po godinama, rastuće.

    [("Ana", 30), ("Marko", 25), ("Ivan", 35)]
    ->  [("Marko", 25), ("Ana", 30), ("Ivan", 35)]
    Savet: sorted(..., key=lambda t: ...)
    """
    # TODO
    lista=sorted(osobe,key=lambda t:t[1])
    print(lista)
    return lista



def zad_11_spoji_liste(imena, poeni):
    """Spoji dve liste u listu tuplova.

    ["Ana", "Marko"], [90, 75]  ->  [("Ana", 90), ("Marko", 75)]
    Savet: zip
    """
    # TODO
    lista=list(zip(imena,poeni))
    print(lista)
    return lista


def zad_12_tuple_kao_kljuc(tacke):
    """Lista tačaka (x, y). Prebroj koliko se puta pojavljuje svaka tačka.

    [(0, 0), (1, 2), (0, 0)]  ->  {(0, 0): 2, (1, 2): 1}
    (Ovo radi samo zato što je tuple nepromenljiv; lista ne može biti ključ!)
    """
    # TODO
    brojac=0
    dc=dict()
    for i in tacke:
        for j in tacke:
            if(i==j):
                brojac+=1

        dc[i]=brojac
        brojac=0
    return dc



# =====================================================================
# 3. SETOVI
# =====================================================================

def zad_13_jedinstveni(lista):
    """Vrati broj različitih elemenata u listi.

    [1, 2, 2, 3, 3, 3]  ->  3
    """
    # TODO
    return len(set(lista))


def zad_14_zajednicki(a, b):
    """Vrati SET elemenata koji su u obe liste.

    [1, 2, 3, 4], [3, 4, 5]  ->  {3, 4}
    """
    # TODO
    return set(a) & set(b)
    


def zad_15_samo_u_prvoj(a, b):
    """Vrati SET elemenata koji su u prvoj, a nisu u drugoj listi.

    [1, 2, 3, 4], [3, 4, 5]  ->  {1, 2}
    """
    # TODO
    return set(a)-set(b)


def zad_16_tacno_u_jednoj(a, b):
    """Vrati SET elemenata koji su u TAČNO jednoj od dve liste.

    [1, 2, 3], [2, 3, 4]  ->  {1, 4}
    Savet: postoji operator za ovo (simetrična razlika).
    """
    # TODO
    return (set(a)-set(b))|((set(b)-set(a)))


def zad_17_ima_duplikata(lista):
    """Vrati True ako lista ima bar jedan duplikat, inače False.

    [1, 2, 3] -> False      [1, 2, 1] -> True
    Jedna linija koda!
    """
    # TODO
    return True if lista!=list(set(lista)) else False


def zad_18_sva_slova(recenica):
    """Da li rečenica sadrži sva slova engleske abecede (a-z)? Velika/mala slova nisu bitna.

    "The quick brown fox jumps over the lazy dog"  ->  True
    Savet: set("abcdefghijklmnopqrstuvwxyz") i operator <= (podskup)
    """
    # TODO

    s=set("abcdefghijklmnopqrstuvwxyz")
    print(s)
    return s<=set(recenica)
    


# =====================================================================
# 4. REČNICI (dict, "mape")
# =====================================================================

def zad_19_broj_reci(tekst):
    """Prebroj koliko se puta pojavljuje svaka reč (sve malim slovima).

    "Ana voli Marka Marko voli Anu ana"  ->
    {"ana": 2, "voli": 2, "marka": 1, "marko": 1, "anu": 1}
    Savet: tekst.lower().split() i dict.get(kljuc, 0)
    """
    # TODO
    dc=dict()
    brojac=0
    novi_tekst=tekst.lower().split(" ")
    for i in novi_tekst:
        for j in novi_tekst:
                if i==j:
                    brojac+=1
        dc[i]=brojac
        brojac=0
    return dc


def zad_20_obrni_recnik(d):
    """Zameni ključeve i vrednosti.

    {"a": 1, "b": 2}  ->  {1: "a", 2: "b"}
    Savet: dict comprehension i d.items()
    """
    # TODO
    dc=dict()
    for k,v in d.items():
        dc[v]=k

    return dc


def zad_21_spoji_recnike(d1, d2):
    """Spoji dva rečnika. Ako ključ postoji u oba, SABERI vrednosti.

    {"a": 1, "b": 2}, {"b": 3, "c": 4}  ->  {"a": 1, "b": 5, "c": 4}
    """
    # TODO
    dc=dict()
    brojac=0
    for k1,v1 in d1.items():
        #k1=a v1=1
        brojac=v1
        for k2,v2 in d2.items():
            #k2=b v2=3
            if k1==k2: #a==b
                brojac+=v2
        dc[k1]=brojac
        brojac=0
    for k in d2:
        if k not in dc:
            dc[k]=d2.get(k)
    print(dc)
    return dc




def zad_22_najbolji_student(ocene):
    """Rečnik ime -> lista ocena. Vrati IME studenta sa najvećim prosekom.

    {"Ana": [10, 9], "Marko": [7, 8], "Ivan": [9, 9]}  ->  "Ana"
    Savet: max(ocene, key=lambda ime: ...)
    """
    # TODO
    Ime=max(ocene.items(), key=lambda p:sum(p[1]))
    m, ocena=Ime
    return m



def zad_23_grupisi_po_duzini(reci):
    """Grupiši reči po dužini: dužina -> lista reči (redosled kao u ulazu).

    ["ja", "ti", "sto", "on", "kuca"]  ->  {2: ["ja", "ti", "on"], 3: ["sto"], 4: ["kuca"]}
    Savet: dict.setdefault ili `if kljuc not in d`
    """
    # TODO
    dc=dict()
    for i in reci:
        if len(i) not in dc:
            dc[len(i)]=[i]
        else:
            dc[len(i)].append(i)
    return dc



def zad_24_filtriraj_cene(cene, limit):
    """Rečnik proizvod -> cena. Vrati NOV rečnik samo sa proizvodima jeftinijim od limita.

    {"hleb": 80, "sir": 900, "mleko": 150}, 200  ->  {"hleb": 80, "mleko": 150}
    """
    # TODO
    dc=dict()
    for k,v in cene.items():
        if v<limit:
            dc[k]=v
    return dc



def zad_25_ugnjezdeni(korisnici):
    """Lista rečnika. Vrati rečnik grad -> broj korisnika iz tog grada.

    [{"ime": "Ana", "grad": "BG"}, {"ime": "Iva", "grad": "NS"}, {"ime": "Pera", "grad": "BG"}]
    ->  {"BG": 2, "NS": 1}
    """
    # TODO
    dc_grad=dict()
    for i in korisnici:
        for k,v in i.items():
            if k=='grad' and v not in dc_grad:
                dc_grad[v]=1
                continue
            elif k=='grad':
                dc_grad[v]=dc_grad.get(v)+1

    return dc_grad



# =====================================================================
# 5. KOMBINOVANO (malo teže)
# =====================================================================

def zad_26_anagrami(reci):
    """Grupiši reči koje su anagrami (ista slova, drugi redosled).

    Vrati listu grupa (listi). Grupe idu redom kojim se prvi put pojave.
    ["sat", "tas", "kuca", "ast", "acuk", "mir"]
    ->  [["sat", "tas", "ast"], ["kuca", "acuk"], ["mir"]]
    Savet: ključ rečnika može biti "".join(sorted(rec)) ili tuple(sorted(rec)).
    """
    # TODO
    nova_lista=[]
    brojac=-1
    for i in reci:
        if not any(i in j for j in nova_lista):
            nova_lista.append([i])
            brojac+=1
            for j in reci[1:]:
                if sorted(i)==sorted(j) and not any(j in k for k in nova_lista):
                    nova_lista[brojac].append(j)
    return nova_lista





def zad_27_dva_broja_zbir(brojevi, cilj):
    """Nađi dva RAZLIČITA indeksa čiji brojevi daju zbir `cilj`. Vrati tuple (i, j), i < j.

    Ako ne postoji, vrati None.
    [2, 7, 11, 15], 9  ->  (0, 1)
    Bonus: reši u jednom prolazu kroz listu pomoću rečnika (broj -> indeks).
    """
    # TODO
    for i in brojevi:
        for j in brojevi[brojevi.index(i)+1:]:
            if i + j==cilj and i<j:
                return (brojevi.index(i),brojevi.index(j))
            elif i + j==cilj and i>j:
                return (brojevi.index(j),brojevi.index(i))

               



def zad_28_inventar(stanje, transakcije):
    """Rečnik proizvod -> količina i lista transakcija (proizvod, promena).

    Primeni sve transakcije. Proizvodi čija količina padne na 0 ili manje se BRIŠU.
    Novi proizvodi se dodaju. Ne menjaj originalni rečnik, nego vrati novi!
    {"jabuka": 5, "kruska": 2}, [("jabuka", -2), ("kruska", -2), ("sljiva", 4)]
    ->  {"jabuka": 3, "sljiva": 4}
    """
    # TODO
    dsc=dict()
    for k,v in stanje.items():
        for i in transakcije:
            if k==i[0] and v+i[1]>0:
                dsc[k]=v+i[1]
    for i in transakcije:
        if i[0] not in dsc and i[1]>0:
            dsc[i[0]]=i[1]
    return dsc




# =====================================================================
# PROVERA: ne menjaj ništa ispod ove linije
# =====================================================================

def _provere():
    return {
        "zad_01_parni": lambda: (
            zad_01_parni([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
            and zad_01_parni([1, 3]) == []),
        "zad_02_kvadrati": lambda: (
            zad_02_kvadrati(4) == [1, 4, 9, 16] and zad_02_kvadrati(0) == []),
        "zad_03_drugi_najveci": lambda: (
            zad_03_drugi_najveci([5, 1, 9, 9, 3]) == 5
            and zad_03_drugi_najveci([2, 1]) == 1),
        "zad_04_obrni_bez_reverse": lambda: (
            zad_04_obrni_bez_reverse([2,4,6,7,8]) == [8,7,6,4,2]),
        "zad_05_spljosti": lambda: (
            zad_05_spljosti([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]),
        "zad_06_podeli_na_delove": lambda: (
            zad_06_podeli_na_delove([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
            and zad_06_podeli_na_delove([1, 2, 3], 3) == [[1, 2, 3]]),
        "zad_07_bez_duplikata_red_ostaje": lambda: (
            zad_07_bez_duplikata_red_ostaje([3, 1, 3, 2, 1]) == [3, 1, 2]),
        "zad_08_min_max": lambda: (
            zad_08_min_max([4, 9, 1, 7]) == (1, 9)),
        "zad_09_zameni": lambda: (
            zad_09_zameni((1, "a")) == ("a", 1)),
        "zad_10_sortiraj_po_godinama": lambda: (
            zad_10_sortiraj_po_godinama([("Ana", 30), ("Marko", 25), ("Ivan", 35)])
            == [("Marko", 25), ("Ana", 30), ("Ivan", 35)]),
        "zad_11_spoji_liste": lambda: (
            zad_11_spoji_liste(["Ana", "Marko"], [90, 75]) == [("Ana", 90), ("Marko", 75)]),
        "zad_12_tuple_kao_kljuc": lambda: (
            zad_12_tuple_kao_kljuc([(0, 0), (1, 2), (0, 0)]) == {(0, 0): 2, (1, 2): 1}),
        "zad_13_jedinstveni": lambda: (
            zad_13_jedinstveni([1, 2, 2, 3, 3, 3]) == 3),
        "zad_14_zajednicki": lambda: (
            zad_14_zajednicki([1, 2, 3, 4], [3, 4, 5]) == {3, 4}),
        "zad_15_samo_u_prvoj": lambda: (
            zad_15_samo_u_prvoj([1, 2, 3, 4], [3, 4, 5]) == {1, 2}),
        "zad_16_tacno_u_jednoj": lambda: (
            zad_16_tacno_u_jednoj([1, 2, 3], [2, 3, 4]) == {1, 4}),
        "zad_17_ima_duplikata": lambda: (
            zad_17_ima_duplikata([1, 2, 1]) is True
            and zad_17_ima_duplikata([1, 2, 3]) is False),
        "zad_18_sva_slova": lambda: (
            zad_18_sva_slova("The quick brown fox jumps over the lazy dog") is True
            and zad_18_sva_slova("Zdravo svete") is False),
        "zad_19_broj_reci": lambda: (
            zad_19_broj_reci("Ana voli Marka Marko voli Anu ana")
            == {"ana": 2, "voli": 2, "marka": 1, "marko": 1, "anu": 1}),
        "zad_20_obrni_recnik": lambda: (
            zad_20_obrni_recnik({"a": 1, "b": 2}) == {1: "a", 2: "b"}),
        "zad_21_spoji_recnike": lambda: (
            zad_21_spoji_recnike({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}),
        "zad_22_najbolji_student": lambda: (
            zad_22_najbolji_student({"Ana": [10, 9], "Marko": [7, 8], "Ivan": [9, 9]}) == "Ana"),
        "zad_23_grupisi_po_duzini": lambda: (
            zad_23_grupisi_po_duzini(["ja", "ti", "sto", "on", "kuca"])
            == {2: ["ja", "ti", "on"], 3: ["sto"], 4: ["kuca"]}),
        "zad_24_filtriraj_cene": lambda: (
            zad_24_filtriraj_cene({"hleb": 80, "sir": 900, "mleko": 150}, 200)
            == {"hleb": 80, "mleko": 150}),
        "zad_25_ugnjezdeni": lambda: (
            zad_25_ugnjezdeni([{"ime": "Ana", "grad": "BG"}, {"ime": "Iva", "grad": "NS"},
                               {"ime": "Pera", "grad": "BG"}]) == {"BG": 2, "NS": 1}),
        "zad_26_anagrami": lambda: (
            zad_26_anagrami(["sat", "tas", "kuca", "ast", "acuk", "mir"])
            == [["sat", "tas", "ast"], ["kuca", "acuk"], ["mir"]]),
        "zad_27_dva_broja_zbir": lambda: (
            zad_27_dva_broja_zbir([2, 7, 11, 15], 9) == (0, 1)
            and zad_27_dva_broja_zbir([3, 2, 4], 6) == (1, 2)
            and zad_27_dva_broja_zbir([1, 2], 10) is None),
        "zad_28_inventar": lambda: _provera_inventar(),
    }


def _provera_inventar():
    original = {"jabuka": 5, "kruska": 2}
    rezultat = zad_28_inventar(original, [("jabuka", -2), ("kruska", -2), ("sljiva", 4)])
    return rezultat == {"jabuka": 3, "sljiva": 4} and original == {"jabuka": 5, "kruska": 2}


if __name__ == "__main__":
    tacno = 0
    provere = _provere()
    for ime, provera in provere.items():
        try:
            ok = provera()
            poruka = "" if ok else "  <- pogrešan rezultat"
        except NotImplementedError:
            ok, poruka = False, "  <- još nije urađeno"
        except Exception as e:
            ok, poruka = False, f"  <- GREŠKA: {type(e).__name__}: {e}"
        tacno += ok
        print(f"[{'OK' if ok else ' X'}] {ime}{poruka}")
    print(f"\nUrađeno: {tacno}/{len(provere)}")
