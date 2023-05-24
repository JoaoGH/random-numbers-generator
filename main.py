from LinearCongruentialGenerator import LinearCongruentialGenerator

seed = 0

lcg = LinearCongruentialGenerator(seed, 40692, 127, 100)

lcg.generate(1000000)
lcg.doGraph()

