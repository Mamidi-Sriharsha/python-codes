di={'stid':100,'sname':'harsha','marks':30,'phno':9876543210}
print('no of elements in dictionary:',len(di))
print("retrieving student id:",di.get('stid'))
print("retrieving address:",di.get('addr','no record found'))
print("accessing student id =",di["stid"])
di.pop('stid')
print('dict after popping student id:',di)
print(di.keys())
print('keys in dictionary')
for i in di.keys():
    print(i)
print('values in dictionary')
for j in di.values():
    print(j)
print('keys','\t','values')
for k,v in di.items():
    print(k,'\t',v)
print("updating student name")
di["sname"]="sri"
print("updated dictionary=",di)
di.clear()
print('dictionary after removing all elements',di)
