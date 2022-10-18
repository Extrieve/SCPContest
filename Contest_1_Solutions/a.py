'''
Problem: https://codeforces.com/contest/1742/problem/B
'''

def strictlyIncreasing(n, arr): 
    arr.sort()
    tmp = arr[0]
    for n in arr[1:]:
        if n <= tmp:
            return 'NO'
        tmp = n

    return 'YES' 

# Most efficent solution
def strictlyIncreasing1(n, arr):
    return 'YES' if len(set(arr)) == n else 'NO'


def main():
    n = int(input())

    for _ in range(n):
        j = int(input())
        arr = list(map(int, input().split()))
        print(strictlyIncreasing1(j, arr))



if __name__ == '__main__':
    main()