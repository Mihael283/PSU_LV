import re 

fname = input("Unesite ime datoteke: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

s = []
for line in fhand:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        for i in line.split():
            try:
                s.append(float(i))
            except ValueError:
             pass
suma=sum(s)
average=suma/len(s)

print("Ime datoteke: ", fname)
print("Average X-DSPAM-Confidence: ",average)
