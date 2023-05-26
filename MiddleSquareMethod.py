from datetime import datetime

## Classe que gera números aleatórios e salva eles em um arquivo.
class MiddleSquareMethod:
    def __init__(self, seed):
        self.seed = seed
        self.numbers = []

    ## Método responsável por gerar os números, a quantidade é igual ao valor do parametro total.
    def generate(self, total):
        numeros = []
        current = self.seed

        for i in range(total):
            current = current ** 2

            seed_str = str(current).zfill(8)

            middle_digits = seed_str[2:6]

            current = int(middle_digits)

            numeros.append(current)

        self.numbers = numeros

        return numeros


    ## Método responsável por criar um arquivo contendo todos os números gerados e a quantidade total dos números gerados.
    ## O arquivo é salvo em ./files com o nome "msm_" concatenado com a data atual no formato ISO.
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

        filename = "./files/msm_" + str(datetime.now().replace(microsecond=0).isoformat()).replace(':', '-')
        f = open(filename, "w")

        self.numbers.sort()

        for it in self.numbers:
            if it not in json:
                json[it] = 1
                continue
            json[it] += 1

        for key, value in json.items():
            v += f"{key: >{4}}" + ' - ' + str(value)
            v += "\n"
        f.write(v)
        print("Cheque o arquivo " + filename + " para verificar os numeros gerados.\n")
