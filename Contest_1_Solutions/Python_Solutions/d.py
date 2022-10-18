'''
Problem: https://codeforces.com/problemset/problem/208/A
'''

def dubstep(string): return string.replace('WUB', ' ').lstrip()


def main():
    print(dubstep(input()))


if __name__ == '__main__':
    main()