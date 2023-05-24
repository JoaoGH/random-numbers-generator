from LinearCongruentialGenerator import LinearCongruentialGenerator

seed = 0

obj = LinearCongruentialGenerator(seed, 40692, 127, 100)

obj.generate(1000000)
obj.doGraph()