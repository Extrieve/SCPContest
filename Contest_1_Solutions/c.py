'''
Problem: https://codeforces.com/problemset/problem/116/A
'''

def tram(n, arr): 
    min_capacity = 0
    max_of_day = 0
    for exit, enter in arr:
        min_capacity += enter
        min_capacity -= exit

        if min_capacity > max_of_day:
            max_of_day = min_capacity

    return max_of_day

def main():
    n = int(input())
    arr = []
    for _ in range(n):

        a, b = list(map(int, input().split()))
        arr.append((a,b))

    print(tram(n, arr))



if __name__ == '__main__':
    main()
