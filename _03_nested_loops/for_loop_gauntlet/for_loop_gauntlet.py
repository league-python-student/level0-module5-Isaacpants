"""
Create algorithms and use to solve
https://central.jointheleague.org/levels/Level0/Recipes/ForLoopGauntlet.html
"""


if __name__ == '__main__':
    for i in range(100):
        print(i+1)
    for j in range(100):
        print(100-j)
    for k in range(501):
        if k%2 == 0:
            print(str(k) + ', even')
        else:
            print(str(k) + ', odd')
    for l in range(778):
        if l % 7 ==0:
            print(str(l))
    # for m in range(15):
    #     print("As of " + 2021 - m+ ", I am " + 15 - m)


    #pass
