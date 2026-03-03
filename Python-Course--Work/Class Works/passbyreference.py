def changelist(l):
    l.append(50)
    print(f'inside:{l}')
lst=[10,20,30,40]
changelist(lst)
print(f'outside:{lst}')