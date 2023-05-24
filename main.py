from LinearCongruentialGenerator import LinearCongruentialGenerator
from MiddleSquareMethod import MiddleSquareMethod


print("Gerando numeros aleatórios via Linear Congruential Generator")
lcg = LinearCongruentialGenerator(0, 40692, 127, 100)

lcg.generate(1000000)
lcg.doGraph()

print("Gerando numeros aleatórios via Middle Square Method")
msm = MiddleSquareMethod(1234)
msm.generate(10000)
msm.doGraph()
