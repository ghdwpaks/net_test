import csv
import random as r
from typing import Counter

def get_problem_table(filepath) :
    table = []
    with open(filepath,'rt',encoding="UTF8") as f :
        reader = csv.DictReader(f)
        for row in reader :
            table.append(row)
    return table

def test(pro_table) :
    right_ans = []
    for i in range(len(pro_table)) :
        right_ans.append(pro_table[i]["1"])
    #print("test right_ans =",right_ans)
    print(pro_table[0]["2"])
    
    ans = get_ans()
    if check_ans(ans,right_ans) :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
        print()
        print("정답 :",end="")
        for i in range(len(right_ans)) :
            print(right_ans[i])
        print()


def check_ans(userans, rightans) :
    i = 0 
    right_count = 0
    right_nums = []
    while i < len(userans) and i < len(rightans) :
        if userans[i] in rightans :
            right_count += 1
            
        i += 1
    if right_count == len(rightans) :
        return True
    else :
        return False

def get_ans() :
    a = ""
    res = []
    while True :
        a = input("입력 : ")
        if a == "ㄴ" or a == "s" :
            break
        res.append(a)
    return res
startnum = 8 #i = 0의 0상태에서 추가할 숫자
i = startnum
den_num = []
while True :
    #i = r.shuffle[2,4,10,17,35,41]
    '''
    while True :
        choice_list = [2,10,17,35,41,51]
        i = r.choice(choice_list)
        if len(choice_list) == len(den_num) :
            den_num.clear()

        if i in den_num :
            continue
        else :
            break
    '''
            
    i = r.randint(1,10)
    #i += 1
    #i = 35
    ProsFileNum = str(i)
    
    #network
    filepath = "./pros_network/"+ProsFileNum+".txt"

    #comsys
    filepath = "./pros_comsys/"+ProsFileNum+""

    try :
        pro_table = get_problem_table(filepath)
    except FileNotFoundError :
        i = startnum
        continue
    test(pro_table)
    den_num.append(i)

    print()

    