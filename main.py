from LinearCongruentialGenerator import LinearCongruentialGenerator
from LinearCongruentialGenerator_V2 import LinearCongruentialGenerator_V2
from MiddleSquareMethod import MiddleSquareMethod
import time

## Criar instancia global da classe LinearCongruentialGenerator
lcg = LinearCongruentialGenerator(0, 40692, 127, 100)
## Criar instancia global da classe MiddleSquareMethod
msm = MiddleSquareMethod(1234)


## Método realiza a geração dos números, e salva em um arquivo de texto.
def showNumbers():
    print("Gerando numeros aleatórios via Linear Congruential Generator")
    lcg.generate(1000000)
    lcg.doGraph()

    print("Gerando numeros aleatórios via Middle Square Method")
    msm.generate(10000)
    msm.doGraph()


## Método realiza a geração de um novo ID de sessão.
## Quando informado um número verifica se é o último ID gerado,
## para sequestrar a sessão
def cwe331(lcg):
    print("CWE-331 - Gerado um id de sessão.")
    while True:
        print(lcg.next())
        x = input()
        if (x):
            x = int(x)
            break

    if x == lcg.next():
        print("Sessao sequestrada")


## Método cria uma instancia da versão 2 do gerador.
## Essa segunda versão tem a adição de entropia, buscando evitar a repetição dos valores.
## São gerados 2 vezes com os mesmo valores, mas os resultados são distintos.
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


## Método cria uma instancia de LinearCongruentialGenerator.
## Essa instancia tem um módulo maior, possibilitando assim uma maior
## variabilidade de números, com isso é chamado o método 331, para mostrar
## que mesmo tendo uma boa amplitude, ainda sim é possivel sequestrar a sessão.
def cwe334():
    lcg = LinearCongruentialGenerator(0, 40692, 127, 1000)
    print("Gerando números aleatórios via Linear Congruential Generator")
    lcg.generate(1000000)
    lcg.doGraph()
    cwe331(lcg)

## Método criptografa um texto simples usando como chave o proximo
## número do objeto lcg definido globalmente.
## Como é usando um módulo de 100 é realizado um for para tentar
## quebrar a senha.
def cwe338():
    message = "Texto super secreto."
    key = lcg.next()
    ciphertext = encryptMessage(message, key)

    for i in range(0, 100):
        decrypt = decryptMessage(ciphertext, i)
        if decrypt == message:
            print("Texto decriptografado \"" + decrypt + "\" usando a chave " + str(i))
            break


## Método realiza a criptografia de um texto usando uma chave.
## A criptografia usada consiste em saltar o número gerado
## na tabela ASCII usando módulo de 256 para consistir em
## valores da tabela ASCII.
def encryptMessage(message, key):
    ciphertext = ""
    for char in message:
        encrypted_char = str((ord(char) + key) % 256)
        ciphertext += encrypted_char + " "
    return ciphertext.strip()


## Método realiza a descriptografia de um texto usando uma chave.
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
    menu += "4 - CWE-334 - Small Space of Random Values\n"
    menu += "5 - CWE-338 - Use of Cryptographically Weak PRNG\n"
    menu += "0 - Para Sair\n"
    opc = int(input(menu))

    if opc == 0:
        print("Sistema encerrado")
        break

    if opc == 1:
        showNumbers()
    elif opc == 2:
        cwe331(lcg)
    elif opc == 3:
        addMoreEntropy()
    elif opc == 4:
        cwe334()
    elif opc == 5:
        cwe338()
