from LinearCongruentialGenerator import LinearCongruentialGenerator
from LinearCongruentialGenerator_V2 import LinearCongruentialGenerator_V2
from MiddleSquareMethod import MiddleSquareMethod
import time

lcg = LinearCongruentialGenerator(0, 40692, 127, 100)
msm = MiddleSquareMethod(1234)


def showNumbers():
    print("Gerando numeros aleatórios via Linear Congruential Generator")
    lcg.generate(1000000)
    lcg.doGraph()

    print("Gerando numeros aleatórios via Middle Square Method")
    msm.generate(10000)
    msm.doGraph()


def cwe331():
    print("CWE-331 - Gerado um id de sessão.")
    while True:
        print(lcg.next())
        x = input()
        if (x):
            x = int(x)
            break

    if x == lcg.next():
        print("Sessao sequestrada")


def addMoreEntropy():
    lcgv2_1 = LinearCongruentialGenerator_V2(0, 40692, 127, 100)
    print("Gerando números aleatórios via Linear Congruential Generator V2")
    lcgv2_1.generate(1000000)
    lcgv2_1.doGraph()

    time.sleep(1)

    lcgv2_2 = LinearCongruentialGenerator_V2(0, 40692, 127, 100)
    print("Gerando números aleatórios via Linear Congruential Generator V2")
    lcgv2_2.generate(1000000)
    lcgv2_2.doGraph()


def cwe338():
    message = "Texto super secreto."
    key = lcg.next()
    ciphertext = encryptMessage(message, key)

    for i in range(0, 100):
        decrypt = decryptMessage(ciphertext, i)
        if decrypt == message:
            print("Texto decriptografado \"" + decrypt + "\" usando a chave " + str(i))
            break


def encryptMessage(message, key):
    ciphertext = ""
    for char in message:
        encrypted_char = str((ord(char) + key) % 256)
        ciphertext += encrypted_char + " "
    return ciphertext.strip()


def decryptMessage(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.split()
    for encrypted_char in ciphertext:
        decrypted_char = chr((int(encrypted_char) - key) % 256)
        plaintext += decrypted_char
    return plaintext


while True:
    menu = "---\n"
    menu += "1 - Gerar numeros\n"
    menu += "2 - CWE 331 - Insufficient Entropy\n"
    menu += "3 - Adicionar mais entropia\n"
    menu += "4 - CWE-338 - Use of Cryptographically Weak PRNG\n"
    menu += "0 - Para Sair\n"
    opc = int(input(menu))

    if opc == 0:
        print("Sistema encerrado")
        break

    if opc == 1:
        showNumbers()
    elif opc == 2:
        cwe331()
    elif opc == 3:
        addMoreEntropy()
    elif opc == 4:
        cwe338()
