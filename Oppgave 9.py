class Flervalg:
    def __init__(self, spmtekst, svarene, riktigsvar):
        self.spmtekst = spmtekst
        self.svaralt = {}
        for i in range(len(svarene)):
            self.svaralt[svarene[i]] = i
        self.riktigsvar = int(riktigsvar)

    def sjekk_svar(self):
        svaret = int(input("Hvilket alternativ velger du? "))
        while svaret != self.riktigsvar:
            if svaret > 3:
                print(f"Svaralternativ {svaret} finnes ikke. Velg mellom svaralternativ 1, 2, 3 eller 4.")
                svaret = int(input("Hvilket alternativ velger du? "))
            else:
                print(f"Feil svar, prøv igjen!")
                svaret = int(input("Hvilket alternativ velger du? "))
        return print(f"Riktig! Svaret var {self.riktigsvar}")

    def __str__(self):
        streng = f"{self.spmtekst} \n"
        for key, value in self.svaralt.items():
            streng += f"{value}) {key}\n"
        return streng


def lesefil():
    spormsaalListe = []
    with open("sporsmaalsfil.txt", "r") as fil:
        for linje in fil:
            splittet = linje.split(":")
            svarene = splittet[2].split(",")
            flervalget = Flervalg(splittet[0]+"\n", svarene, splittet[1])
            print(flervalget)
            flervalget.sjekk_svar()
            spormsaalListe.append(flervalget)
    return spormsaalListe


if __name__ == "__main__":
    fil = lesefil()



