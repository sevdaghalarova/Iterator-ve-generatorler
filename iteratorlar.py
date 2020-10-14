# iterable object - uzerinde gezine bildigimiz bir objedir
liste=[1,2,3,4,5]
iterator=iter(liste)
# print(next(iterator))
# print(next(iterator))

# kendimiz iterable obje yaratmak istersek iki fonksiyon olusturmamiz gerekir
# __iter__ , __next__
class Kumanda():
    def __init__(self,kanallar):
        self.kanallar=kanallar
        self.index=-1
    def __iter__(self):
        return self
    def __next__(self):
        self.index+=1
        if len(self.kanallar)>self.index:
            return self.kanallar[self.index]
        else:
            self.index=-1
            raise StopIteration

kumanda=Kumanda(["ATV","KANALD","TV8"])
ITERATOR=iter(kumanda)
print(next(ITERATOR))
for i in kumanda:
    print(i)
