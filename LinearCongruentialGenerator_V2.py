from datetime import datetime
import os

## Classe que gera números aleatórios e salva eles em um arquivo.
## Essa classe contém entropia, que é usando os segundos da data atual.
class LinearCongruentialGenerator_V2:
    def __init__(self, seed, multiplier, increment, modulo):
        entropy = int(datetime.now().timestamp())
        self.seed = seed + entropy
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo + int(entropy/10000)
        self.numbers = []
        self.last = None

    ## Método responsável por gerar os números, a quantidade é igual ao valor do parametro total.
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

    ## Método que gera o número e salva no atributo last.
    def gen(self):
        self.last = (self.multiplier * (self.last if self.last is not None else 0) + self.increment) % self.modulo
        return self.last

    ## Método responsável por gerar somente um número.
    def next(self):
        return self.gen()

    ## Método responsável por criar um arquivo contendo todos os números gerados e a quantidade total dos números gerados.
    ## O arquivo é salvo em ./files com o nome "lcg-v2_" concatenado com a data atual no formato ISO.
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

        if not os.path.exists('./files'):
            os.makedirs('./files')

        filename = "./files/lcg-v2_" + str(datetime.now().replace(microsecond=0).isoformat()).replace(':', '-') + '.txt'
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
