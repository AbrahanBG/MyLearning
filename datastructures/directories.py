#List

cards=list()
cards.append(21)
cards.append(3) 
cards.append(75)
#print(cards)
#print(cards[2]) #slect elemt from a list
cards[1]= cards[1]+5 #using value from a list to operation
#print(cards)
#print(cards[1])

#directorie has a key-value

cabinet = dict()
cabinet['abrahan']=27
cabinet['ever']=25
cabinet['aaron']=23
cabinet['danna']=17

#print(cabinet) 
# empty dictr using curlu brace ooo = {}

#counting  with a dict

ccc =dict()
ccc['pepe']=1
ccc['ana']=1
#print (ccc)
ccc['pepe']= ccc['pepe'] + 1 #adding a moke to the value from the key
#print (ccc)
#print (ccc['ana']) #print value from the key "ana"

#adding new name to the dict
names = ['angel','monica','cristi','pepe','ana']

#r name in names:
#    if name not in ccc:
 #       ccc[name] = 1
  #  else: 
   #     ccc[name]= ccc[name] + 1
#print(ccc)
#get method for dict

#for name in names:
   # ccc[name]= ccc.get(name,0)+1
#print(ccc)

#texto="""Este es un ejemplo de texto de prueba.
#Este texto contiene palabras repetidas para probar el conteo de palabras en Python.
#Python es un lenguaje de programación popular.
#El conteo de palabras en Python es una tarea común en el procesamiento de texto."""
#sentence = dict()
#print('Enter sentence')
#line=texto

#words=line.split()
#print('Words in the sentence are:',words)

#print('awantaaaa')
#for word in words:
#    sentence[word]=sentence.get(word,0)+1
#print (sentence)

karcher = {'angel': 24,'monica':25,'cristi':30,'pepe':26,'ana':28}

karcheremployees = list(karcher.keys())
karcherages = list(karcher.values())
print(karcheremployees, karcherages)
print(karcher.items())
for aaa,bbb in karcher.items():
    print(aaa,bbb)
#new code
name = input("EnterFile:")
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word]= counts.get(word,0)+1
bigcount = None
bigword = None

for word,count in words.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigcount,bigword)

# mbox-short.txt