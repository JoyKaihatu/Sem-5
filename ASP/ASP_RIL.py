import sys
import tkinter as tk



Rule = {
    "Rule 13": {"if": ["Tidak", "Ya", "Reptil", "Karnivora"], "then": "Pterosaurus"},
    "Rule 14": {"if": ["Tidak", "Tidak", "Mamalia", "Omnivora"], "then": "Beruang"},
    "Rule 15": {"if": ["Tidak", "Tidak", "Mamalia", "Herbivora"], "then": "Sapi"},
    "Rule 16": {"if": ["Tidak", "Tidak", "Mamalia", "Karnivora"], "then": "Singa"},
    "Rule 17": {"if": ["Tidak", "Tidak", "Ikan", "Omnivora"], "then": "Ikan Mas"},
    "Rule 18": {"if": ["Tidak", "Tidak", "Ikan", "Herbivora"], "then": "Pari"},
    "Rule 19": {"if": ["Tidak", "Tidak", "Ikan", "Karnivora"], "then": "Hiu"},
    "Rule 20": {"if": ["Tidak", "Tidak", "Reptil", "Omnivora"], "then": "Kadal Air"},
    "Rule 21": {"if": ["Tidak", "Tidak", "Reptil", "Herbivora"], "then": "Iguana"},
    "Rule 22": {"if": ["Tidak", "Tidak", "Reptil", "Karnivora"], "then": "Buaya"},
    "Rule 23": {"if": ["Tidak", "Tidak", "Amfibi", "Omnivora"], "then": "Katak"},
    "Rule 24": {"if": ["Tidak", "Tidak", "Amfibi", "Herbivora"], "then": "Katak Terbang"},
    "Rule 25": {"if": ["Tidak", "Tidak", "Amfibi", "Karnivora"], "then": "Salamnder"},
    "Rule 1":{"if": ["Ya","Ya","Burung","Omnivora"], "then": "Merpati"},
    "Rule 2":{"if": ["Ya", "Ya", "Burung", "Herbivora"], "then": "Kolibri"},
    "Rule 3":{"if": ["Ya", "Ya", "Burung", "Karnivora"], "then": "Elang"},
    "Rule 4":{"if": ["Ya", "Ya", "Mamalia","Karnivora"], "then": "Griffin"},
    "Rule 5":{"if": ["Ya", "Ya","Reptil", "Karnivora"], "then":"Quetzalcoatl" },
    "Rule 6":{"if": ["Ya","Tidak","Burung","Omnivora"], "then": "Ayam"},
    "Rule 7":{"if": ["Ya","Tidak","Burung","Herbivora"], "then": "Kasuari"},
    "Rule 8":{"if": ["Ya","Tidak","Burung", "Karnivora"], "then": "Pinguin"},
    "Rule 9":{"if": ["Tidak","Ya","Mamalia","-"], "then":"Kelelawar"},
    "Rule 10":{"if": ["Tidak","Ya","Ikan","-"], "then": "Ikan Terbang"},
    "Rule 11": {"if": ["Tidak","Ya","Reptil","Omnivora"], "then": "Naga"},
    "Rule 12": {"if": ["Tidak","Ya","Reptil","Herbivora"], "then": "Pterosaurus"}

}

class ASP_UI:

    def __init__(self,root):

        self.root = root
        self.root.geometry('800x600')
        self.root.title('ASP_UI')
        self.WorkingRule = Rule.copy()
        self.WorkingRule2 = Rule.copy()

        self.ketemu = False

        self.label = tk.Label(self.root, text="Welcome to expert system", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.buttonframe0 = tk.Frame(self.root)
        self.buttonframe0.columnconfigure(0, weight=1)
        self.buttonframe0.columnconfigure(1, weight=1)
        self.buttonframe0.columnconfigure(2, weight=1)
        self.buttonframe0.columnconfigure(3, weight=1)
        self.buttonframe0.columnconfigure(4, weight=1)

        self.buttonframe1 = tk.Frame(self.root)
        self.buttonframe1.columnconfigure(0, weight=1)
        self.buttonframe1.columnconfigure(1, weight=1)
        self.buttonframe1.columnconfigure(2, weight=1)
        self.buttonframe1.columnconfigure(3, weight=1)
        self.buttonframe1.columnconfigure(4, weight=1)

        self.buttonframe2 = tk.Frame(self.root)
        self.buttonframe2.columnconfigure(0, weight=1)
        self.buttonframe2.columnconfigure(1, weight=1)
        self.buttonframe2.columnconfigure(2, weight=1)
        self.buttonframe2.columnconfigure(3, weight=1)
        self.buttonframe2.columnconfigure(4, weight=1)

        self.buttonframe3 = tk.Frame(self.root)
        self.buttonframe3.columnconfigure(0, weight=1)
        self.buttonframe3.columnconfigure(1, weight=1)
        self.buttonframe3.columnconfigure(2, weight=1)
        self.buttonframe3.columnconfigure(3, weight=1)
        self.buttonframe3.columnconfigure(4, weight=1)

        self.buttonframe4 = tk.Frame(self.root)
        self.buttonframe4.columnconfigure(0, weight=1)
        self.buttonframe4.columnconfigure(1, weight=1)
        self.buttonframe4.columnconfigure(2, weight=1)
        self.buttonframe4.columnconfigure(3, weight=1)
        self.buttonframe4.columnconfigure(4, weight=1)

        ## START BUTTON
        self.btn0 = tk.Button(self.buttonframe0, text="START", font=('ARIAL',18), command=self.TanyaUnggas)
        self.btn0.grid(row=0,column=2,sticky=tk.W + tk.E)
        self.buttonframe0.pack(fill='x')

        ## Tipe Burung? Yes/No
        self.btn11 = tk.Button(self.buttonframe1, text="Yes", font=('Arial', 18))
        self.btn11.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.btn12 = tk.Button(self.buttonframe1, text="No", font=('Arial',18))
        self.btn12.grid(row=0, column=3, sticky=tk.W + tk.E)

        ## Bisa terbang? Yes/No
        self.btn21 = tk.Button(self.buttonframe2, text="Yes", font=('Arial', 18))
        self.btn21.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.btn22 = tk.Button(self.buttonframe2, text="No", font=('Arial',18))
        self.btn22.grid(row=0, column=3, sticky=tk.W + tk.E)


        ## Burung/Mamalia/Ikan/Reptil/Amfibi
        self.btn31 = tk.Button(self.buttonframe3, text="Burung", font=('Arial', 18))
        self.btn31.grid(row=0, column=0,sticky = tk.W + tk.E)
        self.btn32 = tk.Button(self.buttonframe3, text="Mamalia", font=('Arial', 18))
        self.btn32.grid(row=0, column=1, sticky = tk.W + tk.E)
        self.btn33 = tk.Button(self.buttonframe3, text="Ikan", font=('Arial',18))
        self.btn33.grid(row=0,column=2, sticky = tk.W + tk.E)
        self.btn34 = tk.Button(self.buttonframe3, text="Reptil", font=('Arial', 18))
        self.btn34.grid(row=0, column=3, sticky = tk.W + tk.E)
        self.btn35 = tk.Button(self.buttonframe3, text="Amfibi", font=('Arial', 18))
        self.btn35.grid(row=0, column=4, sticky = tk.W + tk.E)


        ## Omnivora/Herbivora/Karnivora
        self.btn41 = tk.Button(self.buttonframe4, text="Omnivora", font=('Arial',18))
        self.btn41.grid(row=0, column=1, sticky = tk.W + tk.E)
        self.btn42 = tk.Button(self.buttonframe4, text="Herbivora", font=('Arial', 18))
        self.btn42.grid(row=0 , column=2, sticky = tk.W + tk.E)
        self.btn43 = tk.Button(self.buttonframe4, text="Karnivora", font=('Arial', 18))
        self.btn43.grid(row=0, column=3, sticky = tk.W + tk.E)

    def TanyaUnggas(self):
        self.buttonframe0.pack_forget()
        self.label.config(text="Unggas kah?")
        self.buttonframe1.pack(fill='x')
        self.btn11.config(command=lambda m="Ya": self.TanyaTerbang(m))
        self.btn12.config(command=lambda m="Tidak": self.TanyaTerbang(m))

    def TanyaTerbang(self,jawaban_unggas):

        print(jawaban_unggas)


        self.WorkingRule2.clear()

        for rule_name, rules in self.WorkingRule.items():
            if rules["if"][0] == jawaban_unggas:
                self.WorkingRule2.update(rule_name=self.WorkingRule[rule_name])
                self.WorkingRule2[rule_name] = self.WorkingRule2.pop('rule_name')



        self.WorkingRule.clear()
        self.CekSatu()

        print(self.WorkingRule2)
        print(self.WorkingRule)


        self.buttonframe1.pack_forget()

        self.label.config(text="Terbang Kah?")
        self.buttonframe2.pack(fill='x')
        self.btn21.config(command=lambda m="Ya": self.TanyaGolongan(m))
        self.btn22.config(command=lambda m="Tidak": self.TanyaGolongan(m))

    def TanyaGolongan(self,jawaban_terbang):

        print(jawaban_terbang)

        self.WorkingRule.clear()

        for rule_name, rules in self.WorkingRule2.items():
            if rules["if"][1] == jawaban_terbang:
                self.WorkingRule.update(rule_name=self.WorkingRule2[rule_name])
                self.WorkingRule[rule_name] = self.WorkingRule.pop('rule_name')

        self.WorkingRule2.clear()

        self.CekSatu()

        print(self.WorkingRule2)
        print(self.WorkingRule)

        if not self.ketemu:
            self.buttonframe2.pack_forget()
            self.label.config(text="Golongan Hewan Apa?")
            self.buttonframe3.pack(fill='x')
            self.btn31.config(command=lambda m="Burung": self.TanyaMakanan(m))
            self.btn32.config(command=lambda m="Mamalia": self.TanyaMakanan(m))
            self.btn33.config(command=lambda m="Ikan": self.TanyaMakanan(m))
            self.btn34.config(command=lambda m="Reptil": self.TanyaMakanan(m))
            self.btn35.config(command=lambda m="Amfibi": self.TanyaMakanan(m))

    def TanyaMakanan(self, jawaban_Golongan):


        print(jawaban_Golongan)


        self.WorkingRule2.clear()

        for rule_name, rules in self.WorkingRule.items():
            if rules["if"][2] == jawaban_Golongan:
                self.WorkingRule2.update(rule_name=self.WorkingRule[rule_name])
                self.WorkingRule2[rule_name] = self.WorkingRule2.pop('rule_name')

        self.WorkingRule.clear()

        print(self.WorkingRule2)

        self.CekSatu()

        print(self.WorkingRule2)
        print(self.WorkingRule)

        if not self.ketemu:
            self.buttonframe3.pack_forget()
            self.label.config(text="Makan Apa?")
            self.buttonframe4.pack(fill='x')
            self.btn41.config(command=lambda m="Omnivora": self.End(m))
            self.btn42.config(command=lambda m="Herbivora": self.End(m))
            self.btn43.config(command=lambda m="Karnivora": self.End(m))

    def End(self, jawaban_makanan):



        print(jawaban_makanan)

        self.WorkingRule.clear()

        for rule_name, rules in self.WorkingRule2.items():
            if rules["if"][3] == jawaban_makanan:
                self.WorkingRule.update(rule_name=self.WorkingRule2[rule_name])
                self.WorkingRule[rule_name] = self.WorkingRule.pop('rule_name')

        self.WorkingRule2.clear()

        print(self.WorkingRule2)

        self.CekSatu()

        print(self.WorkingRule2)
        print(self.WorkingRule1)



    def EndAlter(self,Pilih:int):

        self.buttonframe1.pack_forget()
        self.buttonframe2.pack_forget()
        self.buttonframe3.pack_forget()
        self.buttonframe4.pack_forget()

        self.ketemu = True

        Akhir = "Jawaban adalah "
        if Pilih == 1:
            Depan, Ambil = self.WorkingRule.popitem()
            Answer = Ambil['then']
            Akhir = Akhir + Answer

            self.label.config(text=Akhir)

        elif Pilih == 2:
            Depan, Ambil = self.WorkingRule2.popitem()
            Answer = Ambil['then']
            Akhir = Akhir + Answer
            self.label.config(text=Akhir)

        elif Pilih == 0:
            self.label.config(text="Jawaban Tidak Tersedia")


    def CekSatu(self):
        if len(self.WorkingRule2) == 1:
            self.EndAlter(2)

        elif len(self.WorkingRule) == 1:
            self.EndAlter(1)

        elif len(self.WorkingRule) == 0 and len(self.WorkingRule2) == 0:
            self.EndAlter(0)







if __name__ == "__main__":
    root = tk.Tk()
    ASP_UI(root)
    root.mainloop()
