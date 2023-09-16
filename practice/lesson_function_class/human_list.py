import sys
def ft_len(x):
    len_count = 0
    #print(x)
    for i in x:
        len_count += 1
    return len_count

# test1 = [['いちお', '170', '60', '27', 'エンジニア', '7', '非公開'], ['としお', '180', '70', '29', 'インラストレーター', '7', '公開'], ['ともお', '190', '80', '31', 'エンジニアの卵', '7', '公開'], ['たましげ', '160', '55', '40', '高校教師', '28', '非公開'], ['いたるっす', '170', '70', '29', 'プロデューサー', '7', '公開'], []]
# test2 = ['BMI', '身長', '体重', '足のサイズ', '職業', '職歴', '公開',1]
# print(ft_len(sys.argv),len(sys.argv),ft_len(sys.argv) == len(sys.argv))
# print(ft_len(test1),len(test1),ft_len(test1) == len(test1))
# print(ft_len(test2),len(test2),ft_len(test2) == len(test2))
# print(ft_len([""]),len([""]),ft_len([""]) == len([""]))
# print(ft_len([5]),len([5]),ft_len([5]) == len([5]))
# print(ft_len("hoge"),len("hoge"),ft_len("hoge") == len("hoge"))
# print(ft_len(""),len(""),ft_len("") == len(""))



if  ft_len(sys.argv) <= 1:
    print("")
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
    # 目的: ファイル入力のリスト化、行数と公開設定のカウント
    # 必要な入力: ststus, file, open_list, count,
    # 用意したい出力: ststus, open_list, count,
    while True:
        status.append(file.readline().split())

        if status[i] == []:
            break
        if status[i][6] == "公開":
            open_list += 1
        status_len = ft_len(status)
        i += 1 
    count = i

    for i in range(ft_len(status_name)):
        judge = "NO"
        for j in range(ft_len(sys.argv)):
            if status_name[i] == sys.argv[j]:
                judge = "YES"
        check_list.append(judge)
    print(status_name)

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