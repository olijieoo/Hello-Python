# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
#a = raw_input().split()
#a = map(int, a)
#tt = tuple(a)
#print hash(tt)

print hash(tuple(map(int, raw_input().split())))