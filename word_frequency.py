file=input("Enter filename: ")
f1=open(file,"r")
counts={}
for line in f1:
    words=line.split()
    for w in words:
        if w in counts:
            counts[w]=counts[w]+1
        else:
            count[w]=1
        print(counts)