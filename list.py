list=[1,'wo',3,True]
print(list[0]);
print(list[1]);
print(list[2]);
print(list[3]);

list.append(2);
print(list[4])
print(list[-1])
list.insert(0,'tom')
print(list)
list.remove('tom')
print(list)
list.reverse()
print(list)

num=[1,5,2,4,7,9,6,5]
num.sort()
print(num)

for number in num:
    print(number)

print(num[0:8])
print(num[0:8:3])
print(num)

for i in range (len(num)):
    print(num[0:i+1])

window_size=4
for i in range(len(num)-(window_size-1)):
    print(num[i:i+window_size])

problems='broke,pale,shoort,nerdy'
l=problems.split(",");
print(l)

joined=' and '.join(l)
print(joined);

#tuple you can not change delete or add
person1=("Nacy-pants",25,'pizza')
person2=("jack",12,'pizza')
people=(person1,person2)
# name,age,favfood=person
# print(age)
for name,age, favfood in people:
    print(name)
    print(age)
    print(favfood)
    print()

#sets do not have duplicates

berry={'blueberry','raseberry'}
berry.add('strawberry')
berry.add('blueberry')
print(berry)

listnum=[1,2,3,3,4,4,4,5]
no_duplicates=set(listnum);
print(no_duplicates)

library1={'harry potter','game of thrones','beast quest'}
library2={'atrixs','tom and jerry'}
both_library=library1.union(library2)
print(both_library)

groceries={'banana':1,'pot':2}

print(groceries['banana'])
#avoid error when value is not found
print(groceries.get('b'))
print(groceries.items())
print(groceries.keys())
print(groceries.values())
groceries.pop('pot')
print(groceries)

t=(1,2,[1,2,3])
t[2][0]=7
print(t)
l=[]
names=['tom','jerry','bob','rex']
for person in names:
    l.append(person)

print(l)

print([person+' dump me ' for person in names ])

l=[]
moives_and_rateings={"monster university":5,"game of throwns":3,"fire bid":3,'it':4}

for moive in moives_and_rateings:
    if moives_and_rateings[moive]>3:
        l.append(moive)


print(l)
l=[]
print(l for movie in moives_and_rateings if moives_and_rateings[moive]>3)