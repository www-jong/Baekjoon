from collections import deque
q=deque()
q.append((1,2))
q.append((3,4))
q2=q.copy()
print(q)
q.popleft()
print(q)
print(q2)