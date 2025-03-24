def convert(string_1):
    n=len(string_1)
    count=0
    for i in range(n//2):
        count+=abs(ord(string_1[i])-ord(string_1[n-1-i]))
    return count
def times():
    string_1=input()
    a=convert(string_1)
    print(a)

def main():
    t=int(input())
    for i in range(0,t):
        times()
main()
