from collections import deque
import time

for i in range(4,11):
    a_var = deque([x for x in range(10**i)])
    cur_time0 = time.time()
    a_var.popleft()
    print(f'popleft 10^{i} :',time.time()-cur_time0)

    d_var = [x for x in range(10**i)]
    cur_time3 = time.time()
    d_var.pop(0)
    print(f'pop(0) 10^{i} :',time.time()-cur_time3)
    print('-----------')