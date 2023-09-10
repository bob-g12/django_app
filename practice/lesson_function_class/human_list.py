import sys

if  len(sys.argv) <= 1:
    print("")
elif sys.argv[1] == "-h":
    print("Hello")

elif  sys.argv[1] == "-m":
    
    san = "さん"
    gobi = ""
    status_name = ["BMI","身長","体重","足のサイズ","職業","職歴","公開"]
    file = open('input.txt','r', encoding="utf-8")
    status = []
    status_len = 0
    counter = 0
    i = 0
    open_list = 0
    check_list =[]

    while True:
        status.append(file.readline().split())

        if status[i] == []:
            break
        if status[i][6] == "公開":
            open_list += 1
        status_len = len(status)
        i += 1
        
    count = i


    for i in range(len(status_name)):
        judge = "NO"
        for j in range(len(sys.argv)):
            if status_name[i] == sys.argv[j]:
                judge = "YES"
        check_list.append(judge)
    if sys.argv[1] != "-m":
        print(str(open_list)+"人の名簿を受け取りました。")

    for i in range(count):
        m = int(status[i][1]) / 100
        kg = int(status[i][2])

        if status[i][6] == "公開":
            if check_list[1] == "YES":
                print(status[i][0]+san+"の"+status_name[1]+"は"+str(status[i][1])+"(cm)"+gobi)
            if check_list[2] == "YES":
                print(status[i][0]+san+"の"+status_name[2]+"は"+str(kg)+"(kg)"+gobi)
            if check_list[0] == "YES":
                print(status[i][0]+san+"の"+status_name[0]+"は"+str(kg / m **2)+"(kg/m2)"+gobi)
            if check_list[3] == "YES":
                print(status[i][0]+san+"の"+status_name[3]+"は"+status[i][3]+"(kg)"+gobi)
            if check_list[4] == "YES":
                print(status[i][0]+san+"の"+status_name[4]+"は"+status[i][4]+gobi)
            if check_list[5] == "YES":
                print(status[i][0]+san+"の"+status_name[5]+"は"+status[i][5]+"年"+gobi)

    file.close()
