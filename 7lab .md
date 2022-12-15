import numpy as np
import matplotlib.pyplot as plt

def K(G1,alpha):
    
return ((2/G1)-(1-np.cos(alpha/2)))/(1+np.cos(alpha/2))
def G2(G1,k):
return G1*k

#Коэффициенты усиления основного лепестка антенны.
G1_64x1 = 57.51
G1_32x1 = 28.76
#Угол направленности основного лепестка антенны.
alpha_64x1 = 1.585*(np.pi/180) alpha_32x1 = 3.171*(np.pi/180)

#k для решетки 64x1
k_64x1=K(G1_64x1, alpha_64x1) k_64x1

#k для решетки 32x1
k_32x1=K(G1_32x1, alpha_32x1) k_32x1

#G2 для для решетки 64x1
G2_64x1= G2(G1_64x1,k_64x1) G2_64x1

#G2 для для решетки 32x1
G2_32x1= G2(G1_32x1,k_32x1) G2_32x1


#Задание 2

h_A = 10 #высота базовой станции
h_U = 1.4 #высота приемника
h_B = 1.7 #высота человека (блокатора)
radius_block = 0.5 #радиус блокатора
distance = 3 #дистанция между передатчиком и приемником

lambda_B = np.linspace(0.1,5,100)	#Интенсивность блокаторов

#вероятность для двухмерного сценария
def probability_2D(distance,lambda_B,radius_block):
return 1-np.exp(-lambda_B*2*radius_block*distance)

#Вычислаем вероятность в зависимости от роста интенсивности поступающий блокатор
probability_2D_array=[]
for i in lambda_B:
probability_2D_array.append(probability_2D(distance,i,radius_block))
