#removes <> from the string

x= "<kjbhjbvjhvghfa> coffee <skjdbksjbfkjsbkm f,msd ,sm ,s><sdjbkjsbfkjdb> is good <hjdbsbdksbdksb>"
y = ""
iswriting = 1

for i in range(len(x)):
    if x[i-1] == ">":
        iswriting = 1
    if x[i] == "<":
       iswriting = 0
    
    if iswriting == 1:
        y += x[i]

print(y)
