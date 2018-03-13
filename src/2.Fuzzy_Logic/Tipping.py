# Name : Tipping
# Version : V1.0
# Description : ����ģ���߼�ʵ�ֶ�С�ѵļ���

# �����ѧ�����numpy
# ����ģ���߼���skfuzzy
import numpy as np
import skfuzzy as fuzz

# ����ģ����
# �����ʳƷ������������Ϊ0-10,����һά�����ʾ
# С��ͨ��Ϊ�ͷѵ�0-25%,����һά�����ʾ
# np.arange��������������,�÷�:np.arange(��ʼ����,��������,����)
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip  = np.arange(0, 26, 1)

# ��ȡʳƷ������������
food_qual = input ("How is the quality of food?(0-10)")
while (food_qual>10) or (food_qual<0):
    print("Input Error!")
    food_qual = input ("How is the quality of food?(0-10)")
    if(food_qual>10) or (food_qual<0):
        print("Input Error!")

# ��ȡ����������������  
serv_qual = input ("How is the quality of service?(0-10)")
while (serv_qual>10) or (serv_qual<0):
    print("Input Error!")
    serv_qual = input ("How is the quality of service?(0-10)")
    if(serv_qual>10) or (serv_qual<0):
        print("Input Error!")

# ���������Ⱥ���
# fuzz.trimf����Ϊ���������������Ⱥ���
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

# ���ݸ���ֵ�õ���Ӧ������
qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, food_qual)
qual_level_md = fuzz.interp_membership(x_qual, qual_md, food_qual)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, food_qual)

serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, serv_qual)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, serv_qual)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, serv_qual)

# �������. 
# Rule 1 : or������ζ��ȡ�������������е����ֵ����������np.fmaxʵ��or������
active_rule1 = np.fmax(qual_level_lo, serv_level_lo)

# Ӧ�ù���1�������Ӧ����������������np.fminʵ��Ӧ�ù������
tip_activation_lo = np.fmin(active_rule1, tip_lo)  

# Rule 2
tip_activation_md = np.fmin(serv_level_md, tip_md)

# Rule 3 

active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)

# ���������������Ա����������һ��
aggregated = np.fmax(tip_activation_lo, np.fmax(tip_activation_md, tip_activation_hi))

# �����ȥģ�����Ľ��
tip = fuzz.defuzz(x_tip, aggregated, 'centroid')

#��������С����Ŀ
print "It is more appropriate for you to pay",tip,"% of the meal as a tip."
price = input("How much is this meal?")
print tip * price * 0.01
