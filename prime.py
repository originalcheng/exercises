from functools import lru_cache
import datetime

@lru_cache(maxsize=None)
def prime(n):
    #print(datetime.datetime.now())
    if n==1: return False
    if int(n**0.5) <2: return True
    for i in range(2,int(n**0.5)+1):
        if prime(i) is True:
            if n%i==0: return False
    return True

def compare(list1, list2):
    start = datetime.datetime.now()
    res = []
    list1 = sorted(set(list1))
    list2 = sorted(set(list2))

    j = 0
    for i in range(len(list1)):
        while len(list2) > j and list1[i] >= list2[j]:
            if list1[i]==list2[j]:
                res.append(list2[j])
            j= j+1
    print(datetime.datetime.now()-start)
    return res

def compare2(list1, list2):
    start = datetime.datetime.now()
    dict = {}
    res=[]
    for i in range(len(list1)):
        dict[list1[i]]= True
    for i in range(len(list2)):
        if list2[i] in dict.keys():
            res.append(list2[i])
    print(datetime.datetime.now()-start)
    return res

if __name__ == "__main__":
    # for i in (1, 2, 25334334331, 133, 211, 121):
    #     print(i, prime(i))

    list1=[100, 12, 1,2,3,4,5,6,7,8]
    list2=[2,5,8,10,12]

    print(compare(list1,list2))
    print(compare2(list1,list2))