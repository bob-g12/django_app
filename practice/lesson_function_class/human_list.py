san = "さん"
gobi = ""
count = 0
status_name = ["BMI","身長","体重","足のサイズ","職業","職歴","血液型"]

for i in range(4):
    count += 1
print(str(count)+"人の名簿を受け取りました。")

for i in range(4):
    status = input("名前,身長,体重,足,職業,職歴,血液型:").split()
    m = int(status[1]) / 100
    kg = int(status[2])

    print(status[0]+san+"の"+status_name[1]+"は"+str(status[1])+"(cm)"+gobi)
    print(status[0]+san+"の"+status_name[2]+"は"+str(kg)+"(kg)"+gobi)
    print(status[0]+san+"の"+status_name[0]+"は"+str(kg / m **2)+"(kg/m2)"+gobi)
    print(status[0]+san+"の"+status_name[3]+"は"+status[3]+"(kg)"+gobi)
    print(status[0]+san+"の"+status_name[4]+"は"+status[4]+gobi)
    print(status[0]+san+"の"+status_name[5]+"は"+status[5]+"年"+gobi)
    print(status[0]+san+"の"+status_name[6]+"は"+status[6]+"型"+gobi)