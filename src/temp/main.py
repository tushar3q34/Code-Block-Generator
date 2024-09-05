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
    separated = [[None for j in range(n)] for i in range()] 
    for i in range():
        for j in range(n):
            separated[i][j] = int(cin())
    separated = [[None for j in range(n-1)] for i in range(n)] 
    for i in range(n):
        for j in range(n-1):
            separated[i][j] = int(cin())
    


for tc in range(int(input())):
    solve()

