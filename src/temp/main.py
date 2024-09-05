from collections import deque

input_buffer = deque()
def cin():
    if input_buffer:
        return input_buffer.popleft()
    else:
        input_buffer.extend(input().split())
        return input_buffer.popleft()


def solve():
    n = int(cin())
    k = int(cin())
    a = [None for i in range(n)] 
    for i in range(n):
        a[i] = int(cin())
    


for tc in range(int(input())):
    solve()

