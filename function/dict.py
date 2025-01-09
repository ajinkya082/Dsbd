

d={1:'vivek',2:'Mumbai', 3:'Patil',4:'Kakade'}

print(d.keys())
print(d.values())
d[2]='Rahul'
print(d)
d['China']=5
d.__delitem__(1)
d.pop(3)

print(d)