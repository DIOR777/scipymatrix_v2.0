import random


def get(arr, size):
    result = []
    for i in range(size - 1):
        j = i + 1
        result.append(arr[i][j])
    return result


def to_string(arr, size):
    result = []
    for i in range(size - 1):
        a = ''
        for value in arr[i]:
            a += str(value) + ' '
        result.append(a)
    return result


def main(size):
    n = int(size)
    arr = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = random.randint(10, 99)
    diagonal = get(arr, n)
    array = to_string(arr, n)
    diagonalue = ''
    for value in diagonal:
        diagonalue += str(value) + ' '
    dictionary = {}
    dictionary['массив'] = array
    dictionary['диагональ'] = diagonalue
    return dictionary


if __name__ == '__main__':
    main()