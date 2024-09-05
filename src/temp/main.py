from collections import deque

input_buffer = deque()
def cin():
    if input_buffer:
        return input_buffer.popleft()
    else:
        input_buffer.extend(input().split())
        return input_buffer.popleft()


def solve():
    l = int(cin())
    r = int(cin())



for tc in range(int(input())):
    solve()

