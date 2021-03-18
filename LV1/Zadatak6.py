import re 

fname = input("Unesite ime datoteke: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

#find emails
emails = []
for line in fhand:
    line = line.rstrip()
    if line.startswith("From "):
        emails.append(re.findall(r'[\w\.-]+@[\w\.-]+', line))

#emails in list
rez=[]
for i in emails: 
    if i not in rez: 
        rez.append(i) 

#emails
res = [''.join(ele) for ele in rez] 

#separte hostnames and add to dictionary
dicts = {}
for i in res:
    i=i[i.index('@') + 1 : ] 
    if i not in dicts:
        dicts[i]=1
    elif i in dicts:
        dicts[i]+=1

#print out
for i in range(3):
    print(res[i])
    
print("\nPonavljanja:")
for x, y in dicts.items():
    print(x, ":", y)




