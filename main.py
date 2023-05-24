from LinearCongruentialGenerator import LinearCongruentialGenerator

lcg = LinearCongruentialGenerator(0, 40692, 127, 100)

lcg.generate(1000000)
lcg.doGraph()

