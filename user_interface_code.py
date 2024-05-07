import tkinter as tk
from tkinter import filedialog


import sqlite3
import csv

class izmainas(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Stundu izmaiņu informātors")
        self.grid()
        self.pogas()
        self.rows = []

    def pogas(self):



        # Option menu for additional selection
        self.additional_var = tk.StringVar(self)
        self.additional_var.set("Diena")
        self.additional_dropdown = tk.OptionMenu(self, self.additional_var, "Pirmdiena", "Otrdiena", "Trešdiena","Ceturdiena","Piektdiena")
        self.additional_dropdown.grid(row=3, column=13)



        # ramis pogai 
        self.inputram = tk.Frame(self)
        self.inputram.grid(row=1, column=0, columnspan=12)
        
        self.skollabel = tk.Label(self.inputram, text="Skolotājs:")
        self.skollabel.grid(row=0, column=0)
        self.skolvar = tk.StringVar()
        
        # labels prieks ui
        self.klasulabels = []
        self.klasuievade = []
        for i in range(1, 11):
            label = tk.Label(self.inputram, text=f"Stunda {i}:")
            label.grid(row=0, column=i+1)
            self.klasulabels.append(label)

        # row pievienosanas poga
        self.addrowbutton = tk.Button(self, text="Pievienot līniju", command=self.add_row)
        self.addrowbutton.grid(row=2, column=0, columnspan=12)

        # save poga
        self.savebut = tk.Button(self, text="Saglabāt", command=self.save_inputs)
        self.savebut.grid(row=3, column=0, columnspan=12)
    def add_row(self):
        # row lists
        new_row = []

       
        teacher_var = tk.StringVar(self.inputram)
        teacher_var.set("Izvēlies skolotāju")

        teacher_dropdown = tk.OptionMenu(self.inputram, teacher_var, "Z.Skrastiņa", "R.Skara-Mincāne", "M.Priedītis","A.Deksne","D.Feldhūne")#šeit var mierīgi papildināt cik grib, garumzīmes nav jo programma nespēj dekodēt.
        teacher_dropdown.grid(row=len(self.rows)+1, column=0)
        new_row.append(teacher_dropdown)

        class_entries = []
        for i in range(1, 11):
            entry = tk.Entry(self.inputram)
            entry.grid(row=len(self.rows)+1, column=i+1)
            class_entries.append(entry)

        # pievieno rows 
        new_row.extend(class_entries)
        self.rows.append(new_row)

        # pievieno skolotaju
        new_row.append(teacher_var)
        


    def save_inputs(self):
        global additional
        additional = self.additional_var.get()
        print(additional)
        # save lodzins
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if not filename:
            return
        

        
        with open(filename, "w") as file:
            # header
            header = ["Skolotajs"]
            header.extend([f"Stunda {i}" for i in range(1, 11)])
            file.write(",".join(header) + "\n")
            

            
            for row in self.rows:
            # paņem inpututs
                class_entries = [entry.get() for entry in row[1:]]

                #raksta input info
                
                row_data = [class_entries[10]]
                row_data.extend(class_entries[0:10])
                file.write(",".join(row_data) + "\n")
      

        with open(filename, 'r') as csv_file:
            csv_file_reader = csv.reader(csv_file)
            next(csv_file_reader)  
            
       
            savien = sqlite3.connect("saraksti.db")
            cursor = savien.cursor()    
            cursor.execute("drop table if exists izmainas")
        
            cursor.execute("CREATE TABLE IF NOT EXISTS izmainas (Skolotaajs TEXT, Stunda_1 TEXT, Stunda_2 TEXT, Stunda_3 TEXT, Stunda_4 TEXT, Stunda_5 TEXT, Stunda_6 TEXT, Stunda_7 TEXT, Stunda_8 TEXT, Stunda_9 TEXT, Stunda_10 TEXT);")
            
        
            for row in csv_file_reader:
                
                sk, pirma, otra, tresa, ceturt, piekta, sesta, septita, astota, devita, desmit = row
                
                try:
              
                    cursor.execute("REPLACE INTO izmainas VALUES (?,?,?,?,?,?,?,?,?,?,?)", (sk, pirma, otra, tresa, ceturt, piekta, sesta, septita, astota, devita, desmit))
                    print("Values inserted successfully.")
                except sqlite3.Error as error:
                    print("Error occurred:", error)
            cursor.execute("drop table if exists diena")
            cursor.execute("CREATE TABLE diena(Diena TEXT);")
            cursor.execute("INSERT INTO diena (Diena) VALUES(?)",(additional,))

            savien.commit()
            cursor.execute("SELECT * FROM izmainas")
            savien.close()
                



        


            
        
        


 



root = tk.Tk()
app = izmainas(master=root)
app.mainloop()
