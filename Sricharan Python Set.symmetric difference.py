if __name__ == '__main__':
    n = int(input().rstrip())
    a = set(int(x) for x in input().rstrip().split())
    m = int(input().rstrip())
    b = set(int(x) for x in input().rstrip().split())
    print(len(a.symmetric_difference(b)))
