
# coding: utf-8

# In[2]:

#Скачайте train (обучающий) набор данных о пассажирах Титаника.
#С использованием кода на Python найдите ответы на вопросы.


# In[2]:

import pandas as pd #импорт библиотеки pandas (высокоуровневая Python библиотека для анализа данных.)
Res = pd.read_csv('train.csv') #считываем csv-файл


# In[10]:

#1.Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

Port = (Res.groupby(['Embarked'])['PassengerId'].count()) #группировка по портам и пассажирам
for pas in list(Port):
    print (pas, end = ' ')


# In[21]:

#или так...Здесь уже видно название портов:C,Q,S
print(Res.groupby(['Embarked'])['PassengerId'].count())


# In[41]:

#2.Какие доли составляли пассажиры первого, второго, третьего класса?

def Dolya (x):
    k=0
    for pr in x:
        k = k + pr
    for ls in x:
        print ("%.2f" % (ls/k), end = ' ')

ls = list((Res.groupby(['Pclass'])['PassengerId'].count())) #группировка по классам и пассажирам и в список
Dolya (ls)


# In[120]:

#или так...всего одна строчка
Res.groupby('Pclass').size() / len(Res)


# In[130]:

#3.Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
#-возрастом и параметром survival;
#-полом человека и параметром survival;
#-классом, в котором пассажир ехал, и параметром survival.

#Корреляционная связь, означает, что изменения одного показателя сопровождаются изменениями другого показателя.
#абсолютные значения k < 0.3 свидетельствуют о слабой связи,
#значения k от 0.3 до 0.7 - о связи средней тесноты,
#значения k > 0.7 - о сильной связи.

sex = list(Res['Sex']) #превращаем все значения 'Sex' из таблицы в список
dlina = len(sex) #получаем количество элементов списка

for i in range(dlina): #проходимся по каждому элементу списка
    if sex[i] == 'male': #если пол человека мужской, то приравниваем к 1, если женский, то к 0
        sex[i] = 1
    else:
        sex[i] = 0

pol = pd.DataFrame({'Sex':sex})

a1 = (pol['Sex'].corr(Res['Survived'])) #коэффициент коррелляции между полом и выжившими
b1 = (Res['Pclass'].corr(Res['Survived'])) #коэффициент корреляции между классом кабин и выжившими
c1 = (Res['Age'].corr(Res['Survived'])) #коэффициент корреляции между возрастом и выжившими
print("%.2f" % a1)
print("%.2f" % b1)
print("%.2f" % c1)


# In[167]:

#4.Посчитайте среднюю цену за билет и медиану.

#Медиана
ls2 = list(Res['Fare'])

def median(lst):
    n = len(lst)
    if n < 1:
            return None
    if n % 2 == 1:
            return sorted(lst)[n//2]
    else:
            return sum(sorted(lst)[n//2-1:n//2+1])/2.0

median(ls2)


# In[168]:

#Cредняя цена за билет
def my_mean(values):
    n = 0
    Sum = 0.0
    for v in values:
        Sum += v
        n += 1
    return Sum / n


my_mean(ls2)


# In[169]:

#или так =)
md = Res['Fare'].median() #медиана
mn = Res['Fare'].mean() #средняя цена билета
print(md)
print(mn)


# In[211]:

#5.Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?

Vozr = Res[Res.Age > 15][['Sex', 'Name', 'Age']] #отберём тех, у кого возраст больше 15 и добавим пол, имя
Pol = Vozr[Vozr.Sex == 'female'][['Name', 'Age']] #теперь из тех, кто старше 15 выберем женщин
Lop = Vozr[Vozr.Sex == 'male'][['Name', 'Age']] #а тут мужчин

Lop = pd.DataFrame(Lop.Name.str.split(' ', 1).tolist()) #Разбивает строку на части, используя разделитель,
                                                     #и возвращает эти части списком.
Pol = pd.DataFrame(Pol.Name.str.split(' ', 1).tolist())

print(Pol[0].value_counts().index[0]) #метод value_counts() выдаёт самые популярные имена людей на параходе  
                                      #от большего к меньшему. Нам нужно самое популярное, поэтому мы берём только первую строку
print(Lop[0].value_counts().index[0])


# In[ ]:




# In[ ]:




# In[ ]:



