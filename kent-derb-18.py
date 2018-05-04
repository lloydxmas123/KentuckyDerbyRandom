import random

#10 three number combos
#15 four number combos
#5 two number combos
#5 three number combos separate from the others

ten_trifecta = []
fifteen_superfecta = []
five_exacta = []
five_trifecta = []

def createBets():

    for t in range(0,10):
        ten_trifecta.append(random.sample(range(1,22),3))

    for t in range(0,15):
        fifteen_superfecta.append(random.sample(range(1,22),4))

    for t in range(0,5):
        five_exacta.append(random.sample(range(1,22),2))

    for t in range(0,5):
        five_trifecta.append(random.sample(range(1,22),3))

bets = createBets()

with open("kent-derb-18.txt", 'w') as f:
    f.write("Ten Trifectas\n")
    for t in ten_trifecta:
        f.write(str(t) + '\n')
    f.write("\n")

#with open("kent-derb-18.txt", 'a') as f:
    f.write("Fifteen Superfectas\n")
    for t in fifteen_superfecta:
        f.write(str(t) + '\n')
    f.write("\n")

    f.write("Five Exactas\n")
    for t in five_exacta:
        f.write(str(t) + '\n')
    f.write("\n")

    f.write("Five Separate Trifectas\n")
    for t in five_trifecta:
        f.write(str(t) + '\n')
    f.write("\n")
