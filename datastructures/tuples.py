#same as list but inmutable
(x,y) = (4,'fred')
#print(y)

#sort tupples by value

d={'b':1, 'c':22, 'a':10}
t=sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)

tmpp = list()
for k, v in d.items():
    tmpp.append((v,k))
tmpp=sorted(tmpp,reverse=True)
print(tmpp)

#shor version

print(sorted([(v,k) for k,v in d.items()]))