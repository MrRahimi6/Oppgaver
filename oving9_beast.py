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

    ##########################################################
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


#############################################################

def lag_sporsmaal():
    sporsmaalene = []

    file = open("sporsmaalsfil.txt", "r", encoding="UTF8")

    for line in file:
        stripped_line = line.strip()

        stripped_line = stripped_line.replace("[", "")
        stripped_line = stripped_line.replace("]", "")

        split_line = stripped_line.split(":")

        # print(split_line)

        question = split_line[0]

        answer = int(split_line[1])

        options = split_line[2]

        opt1 = options.split(",")

        sporsmaalene.append(Flervalgssporsmaal(question, answer, opt1))

    return sporsmaalene


class TestFlervalgssporsmaal(unittest.TestCase):

    def test_sjekk_svar(self):
        flervalgssporsmaal1 = Flervalgssporsmaal("Den delen av en datamaskin som kjører programmet kalles?:", 2,
                                                 ["RAM", "Harddisk", "CPU", "Sekundærlager"])
        self.assertEqual(flervalgssporsmaal1, True)


if __name__ == "__main__":
    unittest.main()

class Spiller:
    def __init__(self, navn, poengsum=0, svar=0):
        self.navn = navn
        self.poengsum = poengsum
        self.svar = svar


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

    ##########################################################
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


#############################################################

def lag_sporsmaal():
    sporsmaalene = []

    file = open("sporsmaalsfil.txt", "r", encoding="UTF8")

    for line in file:
        stripped_line = line.strip()

        stripped_line = stripped_line.replace("[", "")
        stripped_line = stripped_line.replace("]", "")

        split_line = stripped_line.split(":")

        # print(split_line)

        question = split_line[0]

        answer = int(split_line[1])

        options = split_line[2]

        opt1 = options.split(",")

        sporsmaalene.append(Flervalgssporsmaal(question, answer, opt1))

    return sporsmaalene


def lag_spillerne():
    spillerne = []
    antall_spillere = int(input("Antall spillere: "))
    for i in range(antall_spillere):
        navn = input(f"Navnet til spiller {i}: ")
        spilleren = Spiller(navn)
        spillerne.append(spilleren)
    return spillerne


############################################################

if __name__ == "__main__":

    sporsmaalene = lag_sporsmaal()
    spillerne = lag_spillerne()

    mest_poeng = None

    for sporsmaal in sporsmaalene:
        print(sporsmaal)
        for spiller in spillerne:
            spiller.svar = int(input(f"{spiller.navn}: "))

        for spiller in spillerne:
            if sporsmaal.sjekk_svar(spiller.svar):
                print(f"{spiller.navn}: Riktig!\n")
                spiller.poengsum += 1
            else:
                print(f"{spiller.navn}: Feil!\n")

    for spiller in spillerne:
        if (mest_poeng is None or spiller.poengsum > mest_poeng):
            mest_poeng = spiller.poengsum

            print(f"Vinner: {spiller.navn}")


