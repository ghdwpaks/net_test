import csv


def get_problem_table(filepath) :
    table = []
    with open(filepath,'rt',encoding="UTF8") as f :
        reader = csv.DictReader(f)
        for row in reader :
            table.append(row)
    return table

def test(pro_table) :
    print(pro_table[0]["1"])
    ans = input("입력 : ")
    if ans == pro_table[0]["2"] :
        print("맞았습니다.")
    else :
        print("틀렸습니다.")
        print("정답 :"+str(pro_table[1]))


i = 0
while True :
    i += 1
    ProsFileNum = str(i)
    filepath = "./pros/"+ProsFileNum+".txt"

    try :
        pro_table = get_problem_table(filepath)
    except FileNotFoundError :
        break
    test(pro_table)


    