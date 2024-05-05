import random

l1 = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,
      "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

remark = ['Happy couple','Cuter together','Wonderful Match','Gorgeous Couple','Beautiful Couple','Wow Amazing','Good Together','Lovely Couple','True Love','Perfect Match','Romeo And Juliet','Made for Each Other','A match made in heaven','The Best couple','Beautiful lovers','Looks gorgeous']

def check(res,a1,a2):
    if res <= 80:
        result = round(res)
        choice = random.choice(remark[0:8])
        # print("{} and {} your love percent is {}% {} ".format(a1, a2,res, choice))
        context = {
            'a1':a1,
            'a2':a2,
            'result':result,
            'choice':choice,
        }
        return context
    else:
        result = round(res)
        choice = random.choice(remark[8:])
        # print("{} and {} your love percent is {}% {} ".format(a1, a2, round(res), choice))
        context = {
            'a1': a1,
            'a2': a2,
            'result': result,
            'choice': choice,
        }
        return context

# a1 = input("Enter the Your Name : ")
#
# a2 = input("Enter the Your Lover Name : ")
# d = 0

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
    # print("The total is {} ".format(res))

    if res >= 100:
        result = res/2
        check(result,a1,a2)
    else:
        check(res, a1, a2)