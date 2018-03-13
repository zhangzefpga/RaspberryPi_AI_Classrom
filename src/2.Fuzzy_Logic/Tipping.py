# Name : Tipping
# Version : V1.0
# Description : 利用模糊逻辑实现对小费的计算

# 导入科学计算库numpy
# 导入模糊逻辑库skfuzzy
import numpy as np
import skfuzzy as fuzz

# 产生模糊集
# 服务和食品质量数字量化为0-10,利用一维数组表示
# 小费通常为餐费的0-25%,利用一维数组表示
# np.arange作用是生成数组,用法:np.arange(起始数字,结束数字,步长)
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip  = np.arange(0, 26, 1)

# 获取食品质量的输入量
food_qual = input ("How is the quality of food?(0-10)")
while (food_qual>10) or (food_qual<0):
    print("Input Error!")
    food_qual = input ("How is the quality of food?(0-10)")
    if(food_qual>10) or (food_qual<0):
        print("Input Error!")

# 获取服务质量的输入量  
serv_qual = input ("How is the quality of service?(0-10)")
while (serv_qual>10) or (serv_qual<0):
    print("Input Error!")
    serv_qual = input ("How is the quality of service?(0-10)")
    if(serv_qual>10) or (serv_qual<0):
        print("Input Error!")

# 产生隶属度函数
# fuzz.trimf作用为产生三角形隶属度函数
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

# 根据给定值得到对应隶属度
qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, food_qual)
qual_level_md = fuzz.interp_membership(x_qual, qual_md, food_qual)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, food_qual)

serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, serv_qual)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, serv_qual)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, serv_qual)

# 加入规则. 
# Rule 1 : or操作意味着取两个隶属函数中的最大值。我们利用np.fmax实现or操作符
active_rule1 = np.fmax(qual_level_lo, serv_level_lo)

# 应用规则1，输出相应的隶属函数，利用np.fmin实现应用规则输出
tip_activation_lo = np.fmin(active_rule1, tip_lo)  

# Rule 2
tip_activation_md = np.fmin(serv_level_md, tip_md)

# Rule 3 

active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)

# 将所有三个输出成员函数集合在一起
aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md, tip_activation_hi))

# 计算出去模糊化的结果
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')

#计算最终小费数目
print "It is more appropriate for you to pay",tip,"% of the meal as a tip."
price = input("How much is this meal?")
print tip * price * 0.01
