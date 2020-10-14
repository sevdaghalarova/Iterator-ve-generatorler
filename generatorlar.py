# Generatorlar bellekdeyer kaplamiyorlar
def kare(sayilar):
    for i in sayilar:
        yield i**2

generator=kare(range(1,10))
iterator=iter(generator)
# print(next(iterator))
# print(next(iterator))

# list compherenshionu generatora cevirmek icin sadece () parantez kullaniyoruz
generator1=(i*3 for i in range(1,6))
iterator1=iter(generator1)
print(next(iterator1))
print(next(iterator1))


# carpim tablosu ornegi
def carpim():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)

for i in carpim():
    print(i)
