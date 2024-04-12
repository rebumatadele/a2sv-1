import sys

def i():
    return int(sys.stdin.readline().strip())

def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def ls():
    return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s():
    return sys.stdin.readline().strip()

def d():
    return [int(digit) for digit in input()]

