print("はろわ")
# BMI 肥満指数を表す
# 体重（kg）÷｛身長（m）の2乗｝
# 体重＝60　身長＝　170の場合のBMIを算出するプログラム
print(60 / 1.7 **2)

#　BMIを算出するプログラムの入力を可変可能にする
debu = int(input("体重:"))
tibi = float(input("身長:"))
print(debu / tibi **2)