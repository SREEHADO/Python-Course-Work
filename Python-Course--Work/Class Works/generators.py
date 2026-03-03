
def reels():
    data= ['1..100','101..200','201..300','301..400']
    for i in data:
        yield i

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))



def reels():
    yield "First set"
    yield "Second set"
    yield "3s"
    yield "4s"
    yield "ns"

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))





















