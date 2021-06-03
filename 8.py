a = {1:20,2:20}
b= {3:30,4:40}
newdic  = {}
for i in (a,b): newdic.update(i)
print(newdic)