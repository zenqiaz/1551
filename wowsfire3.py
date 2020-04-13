import numpy as np
import os
import sys

def shoot(shells,ship,time):
    if ship[1]==0:
        shells.append([1,time])
        return
    elif ship[2]==0:
        shells.append([2,time])
        return
    elif ship[0]==0:
        shells.append([0,time])
        return
    else:
        shells.append([1,time])
    return

def fly(shells,ship,damcon):
    res=[ship,damcon]
    if shells == []:
        return res
    for shell in shells:
        shell[1]-=1
    if shells[0][1]==0:
        res=hit(ship,shells[0][0],damcon)
        shells.remove(shells[0])
    return res

def catchfire(ship,position,damcon):
    if position==1:
        hits=shellnumber
    else:
        hits=shellnumber//2
    ran=np.random.random()
    #print(ran)
    if ran>((1-firerate/100)**hits):
        ship[position]=fireduration
        if damcon==0:
            ship[0]=ship[1]=ship[2]=0
            damcon=damconcd+damcondur
    return [ship,damcon]

def hit(ship,position,damcon):
    res=[ship,damcon]
    if damcon>damconcd:
        return res
    if ship[position]==0:
        res=catchfire(ship,position,damcon)
    return res

def timego(t,shells,ship,damcon,score):
    if t%reloadtime==0:
        shoot(shells,ship,flyingtime)
    res=fly(shells,ship,damcon)
    ship=res[0]
    damcon=res[1]
    for p in range(len(ship)):
        if ship[p]>0:
            ship[p]-=1
            score+=1
    if damcon>0:
        damcon-=1
    #print(score)
    #print(ship)
    #print(shells)
    #print(damcon)
    return [score,ship,damcon]

def gotrial():
    score=0
    ship=[0,0,0]
    damcon=0
    shells=[]
    for i in range(trialtime):
        res=timego(i,shells,ship,damcon,score)
        score=res[0]
        ship=res[1]
        damcon=res[2]
    print(score)
    return score



global shellnumber#一轮打几炮
shellnumber=9
global flyingtime#炮弹飞多久
flyingtime=10
global firerate#点火率
firerate=15
global reloadtime#装填时间
reloadtime=6
global damconcd#损管cd
damconcd=80
global damcondur#损管持续
damcondur=28
global fireduration#着火时间
fireduration=43
global trialtime#测试持续时间
trialtime=300
#测试时间内每个着火点着火一秒加一点score
if __name__ == '__main__':
    print('please input shell numbers of one round:')
    a=sys.stdin.readline()
    shellnumber=int(a)
    print('please input shell flying time:')
    a=sys.stdin.readline()
    flyingtime=int(a)
    print('please input shell fire rate:')
    a=sys.stdin.readline()
    firerate=int(a)
    print('please input shell reload time:')
    a=sys.stdin.readline()
    reloadtime=int(a)
    print('please input damcon cooldown time:')
    a=sys.stdin.readline()
    damconcd=int(a)
    print('please input how long damcon lasts:')
    a=sys.stdin.readline()
    damcondur=int(a)
    print('please input how long fire lasts:')
    a=sys.stdin.readline()
    fireduration=int(a)
    scores=[]
    for i in range(500):
        scores.append(gotrial())
    scores=np.array(scores)
    me=scores.mean()
    st=scores.std()
    print(scores)
    print(me)
    print(st)    
    os.system("pause")