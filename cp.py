import random

random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchase = 0

for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = float(ageDecade) / 100
    totals[ageDecade] += 1
    if (random.random()<purchaseProbability):
        totalPurchase += 1
        purchases[ageDecade] +=1

print(f'totals: {totals}')
print(f'totalPurchase: {totalPurchase}')
print(f'purchases: {purchases}')
 
#probability of purchasing things at 30s E=purchase F=age30s' P(EF)

PEF = float(purchases[30])/ float(totals[30])

print(f'Probability(purchase | 30s): {PEF}')

# probability of being 30s' P(F)

PF = float(totals[30]) / 100000

print(f'Probabitity(30s): {PF}')

#probability of buying something regardless of your age P(E)

PE = float(totalPurchase) /100000

print(f'Probability(purchase): {PE}')






