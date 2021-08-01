"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""

if __name__ == '__main__':
    # for i in range(100):
    #     print(i+1)
    #
    # for j in range(100):
    #     print(100-j)
    #
    # for k in range(501):
    #     if k%2 == 0:
    #         print(str(k) + ', even')
    #     else:
    #         print(str(k) + ', odd')
    #
    # for l in range(778):
    #     if l % 7 ==0:
    #         print(str(l))

    # for m in range(15):
    #      print("As of " + str(2021 - m) + ", I am " + str(15 - m))
    #
    # for n in range(3):
    #     for o in range(3):
    #         print(str(n) + " " + str(o) + " ")

    # for p in range(3):
    #     print("\n" + str(p + p + p + 1) + str(p + p + p + 2) + str(p + p + p + 3))
    #
    # for q in range(1, 101):
    #     print(str(q), end=" ")
    #     if q % 10 == 0:
    #         print("\n")

    for r in range(2, 8):
        for s in range(r):
            print("*", end=" ")
            if s % r == 0:
                print("\n")

# pass
