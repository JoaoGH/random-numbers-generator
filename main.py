from LinearCongruentialGenerator import LinearCongruentialGenerator


print("Gerando numeros aleatórios via Linear Congruential Generator")
lcg = LinearCongruentialGenerator(0, 40692, 127, 100)

lcg.generate(1000000)
lcg.doGraph()

