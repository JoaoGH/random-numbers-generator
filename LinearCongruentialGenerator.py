class LinearCongruentialGenerator:
    def __init__(self, seed, multiplier, increment, modulo):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulo = modulo
        self.numeros = []

    def generate(self, total):
        numbers = []
        current = self.seed
        numbers.append(current)

        for i in range(1, total):
            current = (self.multiplier * current + self.increment) % self.modulo

            if current < 0:
                current *= -1

            numbers.append(current)

        self.numeros = numbers

        return numbers

    def showGraph(self):
        json = {}

        self.numeros.sort()

        for it in self.numeros:
            if it not in json:
                json[it] = 1
                continue
            json[it] += 1

        print("Numero - Vezes gerado")
        for key in range(0, self.modulo):
            value = 0
            if key in json:
                value = json[key]
            print(f"{key: >{6}}" + ' - ' + str(value))