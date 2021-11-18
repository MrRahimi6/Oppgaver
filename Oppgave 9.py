


def er_tenaaring(alder):
     if alder >= 13 and alder < 18:
         return True
     else:
         return False

class Flervalg:
    def __init__(self, spmtekst, svarene, riktigsvar):
        self.spmtekst = spmtekst
        self.svaralt = {}
        for i in range(len(svarene)):
            self.svaralt[svarene[i]] = i
        self.riktigsvar = int(riktigsvar)
        self.svarliste = []
        self.ant_riktige = [0, 0]

    def svar(self):
        svaret_spiller1 = int(input(f"Hvilket alternativ velger du spiller {1}? \n"))
        svaret_spiller2 = int(input(f"Hvilket alternativ velger du spiller {2}? \n"))
        self.svarliste = [svaret_spiller1, svaret_spiller2]

    def korrekt_svar_tekst(self):
        for j in range(len(self.svarliste)):
            if self.svarliste[j] != self.riktigsvar:
                if self.svarliste[j] > 3 or self.svarliste[j] < 0:
                    print(f"Svaralternativ {self.svarliste[j]} fantes ikke. Se hvilke tall du kan velge mellom på neste spørsmal.")
                else:
                    print(f"Spiller {j+1} svarte feil. \n")
            else:
                self.ant_riktige[j] += 1
                print(f"Spiller {j+1} svarte riktig. \n")

    def antall_riktige(self):
        return self.ant_riktige

    def __str__(self):
        streng = f"{self.spmtekst} \n"
        for key, value in self.svaralt.items():
            streng += f"{value}) {key}\n"
        return streng


def lesefil():
    spormsaalliste = []
    with open("sporsmaalsfil.txt", "r") as fil:
        for linje in fil:
            splittet = linje.split(":")
            svarene = splittet[2].split(",")
            flervalget = Flervalg(splittet[0]+"\n", svarene, splittet[1])
            spormsaalliste.append(flervalget)
    return spormsaalliste


if __name__ == "__main__":
    klasse_objekter = lesefil()
    ant_riktige = [0, 0]
    for objekt in klasse_objekter:
        print(objekt)
        objekt.svar()
        objekt.korrekt_svar_tekst()
        riktige = objekt.antall_riktige()
        for i in range(len(riktige)):
            ant_riktige[i] += riktige[i]
    for i in range(len(ant_riktige)):
        print(f"Spiller {i+1} har {ant_riktige[i]} antall riktige svar.")


import unittest
  
class Flervalgssporsmaal:
    
    def __init__(self, sporsmaal, riktig_svar, valg):
        self.__sporsmaal = sporsmaal
        self.__valg = valg
        self.__riktig_svar = riktig_svar
        
        
    @property
    def sporsmaal(self):
        return self.__sporsmaal
    @property
    def valg(self):
        return self.__valg
    @property
    def riktig_svar(self):
        return self.__riktig_svar
  
 
    def sjekk_svar(self, svaret):
        if svaret == self.riktig_svar:
            return True
        else:
            return False
        
    def __str__(self):
        tekst = "Spørsmål:  " 
        tekst += self.sporsmaal + "\n"
        
        for valg_nr, svar in enumerate(self.valg):
            tekst += f"{valg_nr}: {svar} \n"
            
        return tekst
    
    def korrekt_svar_tekst(self):
        tekst = f"Korrekt svar: {self.valg[self.__riktig_svar]}"
        
        return tekst
    


def lag_sporsmaal():
    sporsmaalene = []
        
    file = open("sporsmaalsfil.txt", "r", encoding="UTF8")
    
    for line in file:
        
        stripped_line = line.strip()
        
        stripped_line = stripped_line.replace("[","")
        stripped_line = stripped_line.replace("]","")
                
        split_line = stripped_line.split(":")
                
        print(split_line)
                    
            
        question = split_line[0]
            
        answer = int(split_line[1])
            
        options = split_line[2]
        
        opt1 = options.split(",")
        
        
        sporsmaalene.append(Flervalgssporsmaal(question, answer, opt1))
    
    return sporsmaalene


            
            
    
class TestFlervalgssporsmaal(unittest.TestCase):
    
    def test_sjekk_svar(self):
        flervalgssporsmaal1 = Flervalgssporsmaal("Den delen av en datamaskin som kjører programmet kalles?:", 2, ["RAM", "Harddisk", "CPU", "Sekundærlager"])
        self.assertEqual(flervalgssporsmaal1, True)
    
    
    

    
    






if __name__ == "__main__":
    unittest.main()