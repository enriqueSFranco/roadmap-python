from typing import List


def counting_sort(l: List[int]) -> List[int]:
    M = max(l)
    count_list = [0] * (M + 1)

    # contar la cantidad de frecuencias de cada elemento de la lista
    for num in l:
        count_list[num] += 1

    # prefix sum
    for i in range(1, len(l)):
        count_list[i] += count_list[i - 1]

    outs = [0] * len(l)

    for i in range(len(l) - 1, -1, -1):
        outs[count_list[l[i]] - 1] = l[i]
        count_list[l[i]] -= 1

    return outs


if __name__ == "main":
    input_list = [4, 3, 12, 1, 5, 5, 3, 9]
    output_list = counting_sort(input_list)

    print(output_list)
