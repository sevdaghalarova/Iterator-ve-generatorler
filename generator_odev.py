def asal(sayi):
    j=2
    while (j<sayi):
        if sayi%j==0:
            return False
        j+=1
    return True
def asal_generator():
    i=2
    while True:
        if asal(i):
            yield i
        i+=1

for i in asal_generator():
    if i>1000:
        break
    print(i)