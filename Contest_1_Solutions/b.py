'''
Problem: https://codeforces.com/problemset/problem/4/C
'''

def registrationSystem(n, arr): 
    my_dict = dict()

    for item in arr:
        if item not in my_dict:
            my_dict[item] = 1
            print("OK")
        else:
            print(f"{item}{my_dict[item]}")
            my_dict[item] += 1

    return my_dict


def main():
    n = int(input())
    arr = list()
    for _ in range(n):
        arr.append(input())

    registrationSystem(n, arr)




if __name__ == '__main__':
    main()





