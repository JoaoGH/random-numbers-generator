from datetime import datetime

class LinearCongruentialGenerator:
    def __init__(self, seed, multiplier, increment, modulo):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.numbers = []

    def generate(self, total):
        numeros = []
        current = self.seed
        numeros.append(current)

        for i in range(1, total):
            current = (self.multiplier * current + self.increment) % self.modulo

            if current < 0:
                current *= -1

            numeros.append(current)

        self.numbers = numeros

        return numeros

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
