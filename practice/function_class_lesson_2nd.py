san = "くん"
gobi = "。"
for i in range(4):
    status = input("名前,身長,体重,足:").split()
    m = int(status[1]) / 100
    kg = int(status[2])
    print(status[0]+san+"の身長は"+str(status[1])+"(cm)"+gobi)
    print(status[0]+san+"の体重は"+str(kg)+"(kg)"+gobi)
    print(status[0]+san+"のBMIは"+str(kg / m **2)+"(kg/m2)"+gobi)
    print(status[0]+san+"の足のサイズは"+status[3]+"(kg)"+gobi)

#お題9 出力している身長、体重、BMI、足のサイズの部分を、後で変えたい可能性があるので全部変数に格納してください

san = "くん"
gobi = "。"
status_name = ["BMI","身長","体重","足のサイズ"]
for i in range(4):
    status = input("名前,身長,体重,足:").split()
    m = int(status[1]) / 100
    kg = int(status[2])
    print(status[0]+san+"の"+status_name[1]+"は"+str(status[1])+"(cm)"+gobi)
    print(status[0]+san+"の"+status_name[2]+"は"+str(kg)+"(kg)"+gobi)
    print(status[0]+san+"の"+status_name[0]+"は"+str(kg / m **2)+"(kg/m2)"+gobi)
    print(status[0]+san+"の"+status_name[3]+"は"+status[3]+"(kg)"+gobi)