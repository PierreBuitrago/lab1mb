﻿**РОССИЙСКИЙ УНИВЕРСИТЕТ ДРУЖБЫ НАРОДОВ Факультет физико-математических и естественных наук** 

**ОТЧЕТ ПО ЛАБОРАТОРНОЙ РАБОТЕ № 7 Дисциплина: Моделирование беспроводных сетей** 

***Студент: Виллальба Буйтраго Жан Пьер Группа: НФИмд-01-22*** 

**Цель:** 

\1. Исследованиепомехприразныхтипахантенн.

**Задание 1:** 

Используя табличные значения для углов направленности (Таблица 2, для антенных решеток 64x1, 32x1)подберитекоэффициентk длямоделис основным лепестком и потерями на боковые лепестки (формула 1, для каждой антенной решетки), так чтобы получить наилучшую аппроксимацию коэффициентов 

усиления 𝐺1 , представленные в таблице 1.

Entrée [1]: 

**import** numpy **as** np ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.001.png)

**import** matplotlib.pyplot **as** plt 

Entrée [2]: 

**def** K(G1,alpha): ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.002.png)

**return** ((2**/**G1)**-**(1**-**np.cos(alpha**/**2)))**/**(1**+**np.cos(alpha**/**2)) **def** G2(G1,k): 

**return** G1**\***k 

Entrée [3]: 

*#Коэффициенты усиления основного лепестка антенны. ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.003.png)*G1\_64x1 **=** 57.51 

G1\_32x1 **=** 28.76 

*#Угол направленности основного лепестка антенны.* alpha\_64x1 **=** 1.585**\***(np.pi**/**180) 

alpha\_32x1 **=** 3.171**\***(np.pi**/**180) 

Entrée [4]: 

*#k для решетки 64x1 ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.004.png)*k\_64x1**=**K(G1\_64x1, alpha\_64x1) k\_64x1 

Out[4]: 0.017341281249737394 

Entrée [5]: 

*#k для решетки 32x1 ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.005.png)*k\_32x1**=**K(G1\_32x1, alpha\_32x1) k\_32x1 

Out[5]: 

0.034585709804094526 Entrée [6]: 

*#G2 для для решетки 64x1 ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.005.png)*G2\_64x1**=** G2(G1\_64x1,k\_64x1) G2\_64x1 

Out[6]: 0.9972970846723975![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.006.png)

*#G2 для для решетки 32x1* G2\_32x1**=** G2(G1\_32x1,k\_32x1) G2\_32x1 

Out[7]: 0.9946850139657586 

Input [ ]: 

![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.007.png)

**Задание 2:** 

Рассчитайте вероятностьблокировкив двухмернойи трехмерноймоделидлявысотыбазовойстанции10м,высотыприемника1.4м, высотычеловека1.7м. В случае двухмерного сценария высоту базовой станции взять равной высоте приемника. Построить график зависимости вероятностей от интенсивности блокирующих объектов, оценить и сравнить полученные результаты.

Entrée [8]: 

h\_A **=** 10 *#высота базовой станции ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.008.png)*

h\_U **=** 1.4 *#высота приемника* 

h\_B **=** 1.7 *#высота человека (блокатора)* 

radius\_block **=** 0.5 *#радиус блокатора* 

distance **=** 3 *#дистанция между передатчиком и приемником* 

Entrée [9]: 

lambda\_B **=** np.linspace(0.1,5,100)  *#Интенсивность блокаторов ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.009.png)*

Entrée [10]: 

*#вероятность для двухмерного сценария ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.010.png)*

**def** probability\_2D(distance,lambda\_B,radius\_block): 

**return** 1**-**np.exp(**-**lambda\_B**\***2**\***radius\_block**\***distance) 

Entrée [11]: 

*#Вычислаем вероятность в зависимости от роста интенсивности поступающий блокатор ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.011.png)*probability\_2D\_array**=**[] 

**for** i **in** lambda\_B: 

probability\_2D\_array.append(probability\_2D(distance,i,radius\_block)) 

Input [12]: probability\_2D\_array ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.012.png)

Out[12]: Probability\_3D\_array.append(probability\_3D(distance,I,radius\_block,h\_A,h\_U,h\_B)) 

0.34268456492869914, ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.013.png)

ppll00tt....33ft68ii20gt08ul67re43e(74'(17Зd81аp33вi52и**=**80с157и036м045о)82с,,ти вероятностей от интенсивности блокирующих объектов ') pl0t..3p9l9o1t2(7l6a7m0b8d6a9\_5B4,58p,r obability\_2D\_array, label**=**'Вероятность 2D сценарий') 

pl0t..4p1l6o8t4(3l6a6m7b3d4a3\_9B4,45p,r obability\_3D\_array, label**=**'Вероятность 3D сценарий' ) ppppllll0000tttt........4444xyls3568lleh4062aago0796bbew3213een(7486lld)3070(((2595'')9652ЛВ0253яе1828мр2814бо9938дя8044ат5686'н8548о)65,6с,,,ть') 

![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.014.png)

[0.2591817793182821,

0.3614050128519999, 

0.44952277599856505, 

0.5254814393428724, 

0.5909587997640295, 

0.6474011400970685, 

0.6960551750456306, 

0.7379955889761682, 

0.7741487738564038, 

0.8053132916684899, 

0.8321775132765504, En0t.r8é5e53[31438]2:3361005, 

0.9311453539795141, En0t.r9é4e064[61349]5:3463916, 

0.9488364171630668, 

0.9790084722604424, 0.9819050287738279, 0.9844018983402064, 0.9865542325352057, 0.9884095727377306, 0.990008900237662, 0.9913875414424157, 0.9925759481768252, 0.9936003703118376, 0.9944834355792392, 0.9952446493795266, 0.9959008256228215, 0.9964664581193713, 0.9969540407230123, 0.9973743432990196, 0.9977366496119997, 0.9980489623883624, 0.9983181800828516, 0.9985502492536046, 0.9987502959114447, 0.9989227387446877, 0.9990713867204047, 0.9991995232179861, 

0.999309978553373, 0.9994051924958931, 0.9994872681585893, 0.9995580184523881, 0.9996190061301986, 0.9996715783054507, 0.9997168962075247, 0.9997559608313211, 0.9997896350475253, 0.9998186626619437, 0.9998436848449018, 0.9998652542935983, 0.9998838474402416, 0.999899874975621, 0.999913690920564, 0.9999256004456498, 0.999935866611906, 0.9999447161813759, 0.999952344625904, 0.9999589204447747, 0.9999645888865732, 0.9999694751574781, 0.9999736871868513, 0.9999773180112133, 0.9999804478292604, 0.9999831457733172, 0.9999854714363504, 0.9999874761882767, 0.9999892043106349, 0.9999906939746905, 

0.9999919780845732, 0.9999930850040727, 0.9999940391831463, 0.999994861697977, 0.9999955707165095, 0.9999961818997498, 0.9999967087476899, 0.999997162897499, 0.9999975543805693, 0.9999978918440916, 0.9999981827420579, 0.9999984334999061, 0.9999986496564484, 0.9999988359862123, 

0.9999989966049039, En0t.r9é9e99[91951]3:50603149, 

0.9999994459775381, 0.9999995224253979, 0.9999995883244521, 

0.999999645130298, 0.9999996940976795] 

Out[15]: 

[0.058673394579717986, 

0.08642727508710724, 

0.11336286587572819, 

0.13950429323176516, 

0.16487497210693003, 

0.1894976270913028, 

0.2133943127678115, 

0.23658643346658625, 

0.25909476243687846, 

0.2809394604537212, 

0.3021400938759924, ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.015.png)En0t.r3é2e27[1156]5:21720591, 

0.49788990487160545, 0.5126940159011937, 0.527061645558464, 0.5410056629706472, 0.5545385578342672, 0.5676724516021983, 0.5804191083408845, 0.5927899452674492, 0.6047960429761278, 0.616448155363189, 0.6277567192592302, 0.6387318637774766, 0.6493834193864572, 0.659720926715184, 0.6697536450987204, 0.6794905608717944, 0.6889403954178848, 0.698111612980989, 0.7070124282470711, 0.7156508137019797, 0.7240345067724258, 0.7321710167564193, 0.7400676315493679, 0.7477314241718664, 0.7551692591050215, ![](Aspose.Words.7f877679-ae09-4064-aeba-0a5c7bb1a37a.016.png)En00t..r77é66e2933[8973]75:908748348092817836,, 0.776192662342787, 

0.7827913519689471, 0.7891954871839864, 0.7954108041902468, 0.8014428700650571, 0.8072970877471805, 0.8129787008762419,