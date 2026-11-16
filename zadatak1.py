import csv
import logging
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import psycopg

logger=logging.getLogger(__name__)

HOST="localhost"
PORT=5432
USER="postgres"
DBNAME="monitoring"

'''Logging'''
def podesi_loggovanje():
    logging.basicConfig(
        level=logging.INFO,
        filename="loger.log",
        
    )
    logging.FileHandler("loger.log",mode="w")

'''Pretvaranje datuma po vremenskoj zoni'''
def konverzija_datuma(merenja,zona):
    for i in merenja:
        if i[1].isnumeric():
            dat=datetime.fromtimestamp(int(i[1]),tz=ZoneInfo(zona))
            
            i[1]=dat.strftime("%Y-%m-%dT%H:%M:%S")

'''Citanje fajla'''
def citanjeFajla(fajl):
    try:
        if fajl.endswith('.json'):
            with open(fajl,'r') as jsonFile:
                nova_lista=json.load(jsonFile)
                merenja=list()
                for i in nova_lista:
                    merenja.append(list(i.values()))
                
        else:
            with open(fajl) as csvfile:
                citac=csv.reader(csvfile) #Ovo je iterator tako da samo jednom moze da se prodje kroz for petlju
                next(citac)
                merenja=list(citac)
        
        konverzija_datuma(merenja,"Asia/Kolkata")
        print(merenja)       
        return merenja
    except:
        logger.error(f"Fajl {fajl} nije nadjen!")
        #print(f"Fajl {fajl} nije nadjen!")
        return None
         

'''Provera ispravnosti fajla'''
def provera_ispravnosti(fajl):
    rezultat=any('' in i for i in fajl)
    rezultat=False
    brojac=0
    
    for i in fajl:
        if not (i[0].startswith("router_")):
             brojac+=1
    if brojac>0:
        rezultat=True
    try:
        for i in fajl:
            float(i[3])
    except:
        rezultat=True
    return rezultat

'''Kreiranje liste uredjaja'''   
def lista_uredjaja(merenja):
        uredjaji=set()
        for i in merenja:
            uredjaji.add(i[0])
        lista_uredjaja=sorted(list(uredjaji))
        return lista_uredjaja

'''Kreiranje liste merenja i stavljanje u glavnu listu'''
def dodavanje_merenja(lista_uredjaja,merenja):
    broj_merenja=dict()
    brojac=0
    for ur in lista_uredjaja:
        for i in merenja:
            if i[0]==ur and i[2].startswith('cpu'):
                brojac+=1
        broj_merenja[ur]=brojac
        brojac=0
    #sad od disc pravim listu
    glavna_lista=list(broj_merenja.items())
    for i in range(len(glavna_lista)):
        glavna_lista[i]=list(glavna_lista[i])
    return glavna_lista

'''Kreiranje liste proseka i stavljanje u glavnu listu'''
def dodavanje_proseka(lista_uredjaja,merenja,glavna_lista):
    prosek=0
    lista_proseka=[]
    brojac=0
    for ur in lista_uredjaja:
        for i in merenja:
            if i[0]==ur and i[2].startswith('cpu'):
                brojac+=1
                i[3]=float(i[3])
                prosek+=i[3]
        prosek=round(prosek/brojac,2)
        lista_proseka.append(prosek)
        brojac=0
        prosek=0
    brojac=0
    for i in glavna_lista:
        i.append(lista_proseka[brojac])
        brojac+=1
    return glavna_lista

'''Kreiranje liste max i stavljanje u glavnu listu'''
def dodavanje_max(lista_uredjaja,merenja,glavna_lista):
    max=float(0)
    lista_max=[]
    for ur in lista_uredjaja:
        for i in merenja:
            i[3]=float(i[3])
            if i[0]==ur and i[2].startswith('cpu') and i[3]>max:
                max=i[3]
        lista_max.append(max)
        max=0
    brojac=0
    for i in glavna_lista:
        i.append(lista_max[brojac])
        brojac+=1
    return glavna_lista

'''Ucitavanje praga'''
def ucitaj_prag():
    prag=input("Unesite prag kao broj izmedju 0 i 100: ")
    try:
        prag=float(prag)
        
        if prag<0 or prag>100:
            logger.error("Prag nije dobro unet")
            print("Prag nije dobro unet! Probajte ponovo")
            return None
        return prag
    except ValueError:
        logger.error("Prag nije dobro unet")
        print("Prag nije dobro unet! Probajte ponovo")
        return None
    

'''Prekoracenje praga'''
def prekoraceni_uredjaji(prag,merenja):
    set_prekoracenja=set()
    for i in merenja:
         if i[2].startswith('cpu') and i[3]>prag:
             set_prekoracenja.add(i[0])
    return set_prekoracenja


'''Ispis merenja koja imaju duplikate'''
def ispis_losih_merenja(losa_merenja): 
    rezultat=open('rezultati.txt','w')
    brojac=1
    for i in losa_merenja:
        for j in losa_merenja[brojac:]:
            if i[0]==j[0] and i[1]==j[1] and i[2]==j[2]:
                rezultat.write(f"Lose merenje ima ruter {i[0]} gde je za datum {i[1]} i merenje {i[2]} vrednost u jednom merenju {i[3]} a u drugom {j[3]}")
        brojac+=1


'''Ispis u fajl'''
def ispis_fajl(glavna_lista,merenje):
    rezultat=open('rezultati.txt','w')
    for i in glavna_lista:
        ruter,mera,prosek,max=i
        rezultat.write(f"{ruter}     {mera}      {prosek}    {max}\n")
    prag=None
    while prag is None:
        prag=ucitaj_prag() 

    set_prekoracenja=prekoraceni_uredjaji(prag,merenje)
    rezultat.write(f"Ruteri koji su prekoracili prag ({prag}) su:{set_prekoracenja}")

'''KONEKCIJA SA BAZOM'''
def povezivanje_sa_bazom():
    lozinka=input("Unesite lozinku: ")
    try:
        conn=psycopg.connect(host=HOST,user=USER, dbname=DBNAME,port=PORT, password=lozinka)
    except psycopg.OperationalError as e:
        logger.error("Povezivanje sa bazom nije uspelo")
        return None
    logger.info("Povezano sa bazom")
    return conn

'''ISPIS SQL upita'''
def ispis_upita(upit):
    rez=open("rezultati.txt","w")
    for i in upit:
        for j in range(len(i)):
            rez.write(f"{i[j]}\t\t")
        rez.write("\n")
            


'''SQL: Pregled uredjaja'''
def pregled_uredjaja(conn):
    upit="""select d.device_id,d.name,d.location,d.device_type,count(m.id) as broj_merenja
    from devices d
    left join measurements m on d.device_id=m.device_id
    group by d.device_id
    order by d.device_id asc
    """

    with conn.cursor() as cur:
        cur.execute(upit)
        ispis_upita(cur.fetchall())

'''Maksimalno CPU opterecenje po uredjaju'''  
def max_cpu_po_uredjaju(conn):
    upit="""select d.device_id,MAX(m.value)
    from devices d
    inner join measurements m on d.device_id=m.device_id
    where metric_name LIKE 'cpu%'
    group by d.device_id
    order by d.device_id"""  

    with conn.cursor() as cur:
        cur.execute(upit)
        ispis_upita(cur.fetchall())

'''Broj merenja po satu'''
def merenja_po_satu(conn):
    upit="""select date_trunc('hour',timestamp_utc) as vreme_po_satu, count(*) as broj_merenja
    from measurements
    group by vreme_po_satu
    order by vreme_po_satu"""

    with conn.cursor() as cur:
        cur.execute(upit)
        ispis_upita(cur.fetchall())

'''Uredjaji bez zabelezenih merenja'''
def uredjaji_bez_merenja(conn):
    upit="""select d.device_id,d.name,d.location,d.device_type
    from devices d
    left join measurements m on d.device_id=m.device_id
    group by d.device_id
    having count(m.id)=0
    order by d.device_id asc"""

    with conn.cursor() as cur:
        cur.execute(upit)
        ispis_upita(cur.fetchall())

def main():
    podesi_loggovanje()
    conn=povezivanje_sa_bazom()
    if conn is None:
        return
    with conn:
        pregled_uredjaja(conn)
        max_cpu_po_uredjaju(conn)
        merenja_po_satu(conn)
        uredjaji_bez_merenja(conn)

    
    # merenje=citanjeFajla('measurements_initial 1.csv')
    # #merenje=citanjeFajla('measurements_initial.json')
    # if merenje is None:
    #     return
    # if provera_ispravnosti(merenje)==True:
    #     logger.error("Podaci nisu ispravni")
    #     return
   
    # uredjaji=lista_uredjaja(merenje)
    # glavna_lista=dodavanje_merenja(uredjaji,merenje)
    # glavna_lista=dodavanje_proseka(uredjaji,merenje,glavna_lista)
    # glavna_lista=dodavanje_max(uredjaji,merenje,glavna_lista)

    # ispis_fajl(glavna_lista,merenje)

    #provera ponavljanja merenja
    # merenje2=citanjeFajla('measurements_edge_cases.csv')  
    # if merenje2 is None:
    #     return
    # if provera_ispravnosti(merenje2)==True:
    #     logger.error("Podaci nisu ispravni")
    #     return
    # ispis_losih_merenja(merenje2)

main()
    

