from datetime import datetime

class LinearCongruentialGenerator:
    def __init__(self, seed, multiplier, increment, modulo):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.numbers = []
        self.last = None

    def generate(self, total):
        numeros = []
        self.last = self.seed
        numeros.append(self.last)

        for i in range(1, total):
            self.last = self.gen()

            if self.last < 0:
                self.last *= -1

            numeros.append(self.last)

        self.numbers = numeros

        return numeros

    def gen(self):
        self.last = (self.multiplier * (self.last if True else 0) + self.increment) % self.modulo
        return self.last

    def next(self):
        return self.gen()

    def doGraph(self):
        json = {}

        v = "Numeros Gerados"
        v += "\n"
        v += str(self.numbers)
        v += "\n"
        v += "-"*50
        v += "\n"
        v += "Numero - Vezes gerado"
        v += "\n"

        filename = "./files/lcg_" + str(datetime.now().replace(microsecond=0).isoformat()).replace(':', '-')
        f = open(filename, "w")

        self.numbers.sort()

        for it in self.numbers:
            if it not in json:
                json[it] = 1
                continue
            json[it] += 1

        for key in range(0, self.modulo):
            value = 0
            if key in json:
                value = json[key]
            v += f"{key: >{6}}" + ' - ' + str(value)
            v += "\n"
        f.write(v)
        print("Cheque o arquivo " + filename + " para verificar os numeros gerados.\n")
