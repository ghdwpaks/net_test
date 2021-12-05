import csv
import random as r
from typing import Counter
import os


def get_problem_table(filepath) :
    #print("get_problem_table filepath :",filepath)  
    table = []
    with open(filepath,'rt',encoding="UTF8") as f :
        reader = csv.DictReader(f)
        #print("get_problem_table reader :",reader)
        for row in reader :
            #print("get_problem_table row :",row)
            table.append(row)
    return table

def get_problem_table_text(text_filepath) :
    table = []
    text_data = open(text_filepath,"r")
    while True :
        line = text_data.readline()
        if not line : break
        table.append(line)
    return table

def get_ans() :
    a = ""
    res = []
    while True :
        a = input("입력 : ")
        if a == "ㄴ" or a == "s" :
            break
        res.append(a)
    for i in range(len(res)) :
        res[i] = str(res[i]).upper()
    return res

class gen2 :
    def print_pro(pro_cont) :
        #print("gen2 print_pro pro_cont :",pro_cont)
        pro_cont = list(pro_cont)
        #print("gen2 print_pro list(pro_cont) :",pro_cont)

        for i in range(len(pro_cont)) :

            if pro_cont[i] == '/' :
                print()
            else :
                print(pro_cont[i],end="")
        print()
    
    def test_main(pro_table) :
        #print(pro_table)
        pro_table = gen2.setting_pro(pro_table)
        #print(pro_table[0]["show_pro"])
        gen2.print_pro(str(pro_table[0]["show_pro"]))
        userans = get_ans()
        res = False
        if pro_table[0]['test_type'] == 's' :
            res = gen2.check_ans_sentence(userans,pro_table)
        elif pro_table[0]['test_type'] == 'w' :
            res = gen2.check_ans_word(userans,pro_table)
        
        if res :
            print("맞았습니다.")
        else :
            print("틀렸습니다.")
            print()
            print("정답 :",end="")
            for i in range(len(pro_table)) :
                print(pro_table[i]['pro_rightans'])
            print()
        os.system("pause")

    def setting_pro(pro_table) :
        if pro_table[0]["test_type"] == 's' :
            pro_table[0]["pro_rightans"] = str(pro_table[0]["pro_rightans"]).split(".")
        return pro_table
    def check_ans_word(userans,pro_table) :
        #print( pro_table[0]["pro_rightans"])
        #print(userans)
        if userans[0] == pro_table[0]["pro_rightans"] :
            return True
        return False
    def check_ans_sentence(userans,pro_table) :
        right_ans_count = 0
        #print("gen2 check_ans_sentence userans :",userans[0])
        #print("gen2 check_ans_sentence pro_table :",pro_table)
        
        for i in range(len(pro_table[0]['pro_rightans'])) :
            #print("pro_table[0]['pro_rightans'][i] :",pro_table[0]['pro_rightans'][i])
            pro_table[0]['pro_rightans'][i] = str(pro_table[0]['pro_rightans'][i]).upper()
        for i in range(len(pro_table)) :
            temp_right_ans_count = 0
            for j in range(len(pro_table[i]['pro_rightans'])) :  
                #print("pro_table[i]['pro_rightans'][j] :",pro_table[i]['pro_rightans'][j])   
                #print("pro_table[i]['pro_rightans'][j] in userans :",pro_table[i]['pro_rightans'][j] in userans[i])
                if pro_table[i]['pro_rightans'][j] in userans[i] :
                    temp_right_ans_count += 1    
            if temp_right_ans_count == len(pro_table[i]['pro_rightans']) :
                right_ans_count += 1
        #print("right_ans_count :",right_ans_count)
        #print("len(pro_table) :",len(pro_table))
        if right_ans_count == len(pro_table) :
            return True
        return False
        pass

class gen1 :
    def test_main(pro_table) :
        right_ans = []
        for i in range(len(pro_table)) :
            right_ans.append(pro_table[i]["1"])
        #print("test right_ans =",right_ans)
        print(pro_table[0]["2"])
        
        ans = get_ans()
        if gen1.check_ans(ans,right_ans) :
            print("맞았습니다.")
        else :
            print("틀렸습니다.")
            print()
            print("정답 :",end="")
            for i in range(len(right_ans)) :
                print(right_ans[i])
            print()
        os.system("pause")


    def check_ans(userans, rightans) :
        userans = str(userans).strip()
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

startnum = 0 #i = 0의 0상태에서 추가할 숫자
i = startnum
ben_num = []
gen = 2
while True :
    os.system("cls")
    #i = r.shuffle[2,4,10,17,35,41]
    
    while True :
        choice_list = []
        for i in range(1,6) :
            choice_list.append(i)

        i = r.choice(choice_list)
        if len(choice_list) == len(ben_num) :
            ben_num.clear()

        if i in ben_num :
            continue
        else :
            break
    
            
    #i = r.randint(1,3)
    #i += 1
    #i = 1
    ProsFileNum = str(i)
    
    #network nomal
    filepath = "./pros_network_nomal/"+ProsFileNum+".txt"
    gen = 1

    #comsys
    filepath = "./pros_comsys/"+ProsFileNum+""
    gen = 1

    #network control
    filepath = "./pros_network_control/"+ProsFileNum+".txt"
    gen = 2

    filepath = "./pros_data_control/"+ProsFileNum+""
    gen = 1

    filepath = "./pros_java_classes/"+ProsFileNum+""
    gen = 1
    
    filepath = "./pros_network_nomal2/"+ProsFileNum
    gen = 1

    #print("filepath :",filepath)
    try :
        pro_table = get_problem_table(filepath)
        #print("pro_table :",pro_table)
        if gen == 1 :
            gen1.test_main(pro_table)
        elif gen == 2:
            #print("gen2 도달")
            gen2.test_main(pro_table)
        ben_num.append(i)
    except FileNotFoundError :
        i = startnum
        ben_num.append(i)
        continue
    #os.system("pause")

    print()

    