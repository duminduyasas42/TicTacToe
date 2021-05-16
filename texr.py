import re
text='A random string. duminduyasas42@gmail.com    dumindu20191068@iit.ac.lk'
# pattern=re.compile("A random string.")
# result=pattern.search(text)

patern=re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+")
# result=patern.search(text)

result=patern.findall(text)



print(result)