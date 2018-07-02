#问题分析

'''
    自顶向下---分而治之，是“系统”四维的简化： 
    将一个问题表达为若干个小问题组成的形式
    使用同样的方法进一步分解小问题
    直至，小问题可以用计算机简单明了的解决

    自下向上---模块化集成
'''
from random import random

def printInfo():
    print("这是一个模拟乒乓比赛的胜率程序")
    print("比赛规则：A&B，回合制，5局3胜 \n开始时一方先发球，直至" + "判分，接下来胜者发球 \n 球员只能在发球局得分，15分胜一局")
    print("需要输入双方的能力值(以0~1之间的小数表示)")

def getInputs():
    a = eval(input("请输入选手A的能力值(0-1): "))
    b = eval(input("请输入选手B的能力值(0-1): "))
    n = eval(input("模拟比赛的场次： "))
    return a,b,n

def gameOver(a,b):
    return a == 15 or b == 15

def sinOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = 'A'
    while not gameOver(scoreA,scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = 'A'
    return scoreA,scoreB

def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = sinOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB
        

def printSummary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))

def main():
    printInfo()
    probA,probB,n = getInputs()
    winsA,winsB = simNGames(n,probA,probB)
    printSummary(winsA,winsB)

main()
