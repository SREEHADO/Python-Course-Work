
from collections import Counter, defaultdict,deque

n='functions concept'
n='Sree Harsha sings excellent. Iam the Original Gamer.'.split()
res = Counter(n)
print(res)

from collections import Counter, defaultdict,deque

n='functions concept'
n=[9,1,5,1,8,8,4,8,4,3,4,6,4,2]
res = Counter(n)
print(res)

from collections import Counter, defaultdict,deque

n='functions concept'
n=[9,1,5,1,8,8,4,8,4,3,4,6,4,2]
res = defaultdict(int)
for i in n:
    res[i]+=1
print(res)

#defaultdict is going to set all the datatypes like list, float, str, integer & tuple

from collections import Counter, defaultdict,deque

q= deque([])

print(q)

from collections import Counter, defaultdict,deque
q= deque([])
q.appendleft(10)
print(q)
q.appendleft(20)
print(q)
q.appendleft(30)
print(q)
q.pop()
print(q)






































