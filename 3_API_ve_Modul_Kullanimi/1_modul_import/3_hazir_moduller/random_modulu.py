import random

print("0-9 arası random int >", random.randint(0, 9))
print("10-100 arası random int >", random.randint(10, 100))

####################################################
# random sayı listesi oluşturan program
####################################################
randomList = []

# liste 10 elemanlı olacak
for i in range(0, 10):
    # random sayılar 0-100 arası olacak
    randomList.append(random.randint(0, 100))

print(randomList)

# Listeyi Sıralama:
randomList.sort()
print(randomList)