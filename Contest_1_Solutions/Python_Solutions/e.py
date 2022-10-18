'''
Problem: https://codeforces.com/problemset/problem/63/A
'''

def sinkingShip(n, members): 
    ordered_crew = {
        'rat': [],
        'woman': [],
        'man': [],
        'captain': []
    }

    for name, designation in members:

        if designation == 'child':
            designation = 'woman'

        ordered_crew[designation].append(name)

    # ordered_crew['woman'].sort()
    return ordered_crew.values()

def main():
    n = int(input())
    members = []
    for _ in range(n):
        members.append(input().split())

    for items in sinkingShip(n, members):
        if items:
            print('\n'.join(items))


if __name__ == '__main__':
    main()