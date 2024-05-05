import random

l1 = {"A":5,"B":12,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,
      "N":17,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

remark = ['Happy couple','Cuter together','Wonderful Match','Gorgeous Couple','Beautiful Couple','Amazing Couple','Good Together','Lovely Couple','True Lover','Perfect Match','Romeo And Juliet','Made for Each Other','the couple made in heaven','the Best couple','Beautiful lovers','Looks gorgeous','Need to understand each other','Need to spend some time with each other',]

def check(res):
    if res >= 80:
        result = round(res)
        choic = random.choice(remark[8:16])
        return result,choic

    elif res <= 80 and res >=50:
        result = round(res)
        choice = random.choice(remark[:7])
        return result, choice

    else:
        result = round(res)
        choice = random.choice(remark[16:])
        return result, choice

def lovecal(a1,a2):
    d = 0

    for i in a1.upper():
        for j,k in l1.items():
            if i == j:
                d += k

    e = 0
    for i in a2.upper():
        for j,k in l1.items():
            if i == j:
                e += k

    res = d + e
    if res > 100:
        result = res / 2
        return result
    else:

        return res

