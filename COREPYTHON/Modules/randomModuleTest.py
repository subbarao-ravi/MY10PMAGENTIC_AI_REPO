import random as rand

for x in range(10):
    print(rand.random())

print()
for x in range(10):
    print(rand.uniform(1,10))

print()
for x in range(5):
    print(rand.randrange(1,5))
    print(rand.randrange(5))
    print(rand.randrange(1,10,2))

print()
for x in range(20):
    print(rand.randint(1,20))

l=['sunny','bunny','chinny','munny','huny','pinny','benny']
for x in range(10):
    print(rand.choice(l))