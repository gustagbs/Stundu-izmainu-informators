import tkinter as tk

from tabulate import tabulate
import sqlite3
from user_interface_code import izmainas
def process(kl_sar,izmainas_sar,dienaa,kl_index):
    skol=[]
    for sk in skol_sar:
        skol.append(sk[0])
    klasunames = {"_12a": "12a","_12b": "12b"} #tabulu nosaukumu atšifrējumi bez _
    
    for row in kl_sar:   #panem visu dotas klases sarakstu

        
        if row[0]==dienaa: #paņem tikai dotas dienas arakastu
            #print(row)
            dieena=[row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]] #parversh listaa
            
  
            for rowe in dieena: #nem pa vienam stundas
                
                #print(rowe)
                for rower in rowe.split(":"):
                    if rower in skol: #ja tas stundas skolotajai ir izmainas 
                        
                        #print(rowe)
                        for izm in izmainas_sar: #iet cauri izmainam
                            if izm[0]==rower:
                                izmainas_l=[izm[0],izm[1],izm[2],izm[3],izm[4],izm[5],izm[6],izm[7],izm[8],izm[9],izm[10]]#list ar skolotajas izmainam
                                m=0 #lai palidzetu kontrolet kura stunda

                                if izm[0]==rower: #ja stunda sobrid parskatamaa stundas skolotajai ir izmainas
                                    #print(izm)
                                    for izmainas in izm: #iet cauri atseviskam izmainam
                                        
                
                                        

                                        if klasunames.get(kl_index) in izmainas.split(":"): #ja izmaina ir vienada ar sobrid parskatamao klasi
                                            
                                            pagaidu=dieena[m].split(":")
                                            if izmainas_l[0] not in pagaidu:
                                                if dieena[m]=="-":
                                                    dieena[m]=izmainas_l[0]
                                                else:
                                                    pagaidu.append(izmainas_l[0])
                                                    delimiter=":"
                                      
                                                    dieena[m]=delimiter.join(pagaidu) #nomaina stundu saraksta uz šo skolotāju
                                        #if row[m]
                                        if izm[0] in dieena[m].split(":") and klasunames.get(kl_index) not in izmainas_l[m]: #ja seit butu jabut stundai ar šo skolotāju bet nav, ielieku brivstudnu
                                            pagaidu=dieena[m].split(":")
                                            pagaidu.remove(izmainas_l[0]) #šis viss domāts specgadījumiem kad ir vairak par 1 stundu klasei reizee utt
                                            if len(pagaidu)!=0:
                                                delimiter=":"
                                                dieena[m]=delimiter.join(pagaidu)
                                                if len(dieena[m])==0:
                                                    dieena[m]="-"
                                                ...
                                            else:
                                                dieena[m]="-"     
                                                
                                                
                                        m+=1
                if rower in skol:
                    skol.remove(rower)

    cursor.execute("DROP TABLE IF EXISTS pab_izm;")     
    cursor.execute("CREATE TABLE pab_izm(Klase TEXT,Stunda_1 TEXT, Stunda_2 TEXT, Stunda_3 TEXT, Stunda_4 TEXT, Stunda_5 TEXT, Stunda_6 TEXT, Stunda_7 TEXT, Stunda_8 TEXT, Stunda_9 TEXT, Stunda_10 TEXT);")
    cursor.execute("INSERT INTO pab_izm VALUES(?,?,?,?,?,?,?,?,?,?,?)",(klasunames.get(kl_index),dieena[1],dieena[2],dieena[3],dieena[4],dieena[5],dieena[6],dieena[7],dieena[8],dieena[9],dieena[10]))
    cursor.execute("SELECT * FROM pab_izm") #pabeigtās izmaiņas ievieto sql tabulā, lai tās smuki varētu izprintēt ārā
    rows = cursor.fetchall()
    columns = [col[0] for col in cursor.description]
    print(tabulate(rows, headers=columns, tablefmt="fancy_grid"))


root = tk.Tk()
app = izmainas(master=root) #atver UI
app.mainloop()

savien = sqlite3.connect("saraksti.db")
cursor = savien.cursor()    

cursor.execute("SELECT * from diena;")
days=cursor.fetchall()
day=days[0][0].strip()

klases=["_12a","_12b"] #šeit būtu jābūt klasēm kuras ir datubāze, tie ir nosaukumi tabulām

for klaseh in klases:
    #print(klaseh)
    az = f"SELECT * FROM {klaseh}"
    cursor.execute(az)
    klases_saraksts=(cursor.fetchall())

    cursor.execute("SELECT * FROM izmainas;")
    skol_sar=(cursor.fetchall())
    
    process(klases_saraksts,skol_sar,day,klaseh)
    

savien.close()

