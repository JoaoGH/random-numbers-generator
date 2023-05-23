from LinearCongruentialGenerator import LinearCongruentialGenerator

obj = LinearCongruentialGenerator(0, 40692, 127, 100)

obj.generate(1000000)
obj.doGraph()