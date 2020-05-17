def bs_rs(li, start, end, target):
    li.sort()
    mid = (start + end) // 2
    if li[mid] == target:
        return mid

    if start >= end:
        return -1

    if target < li[mid]:
        return bs_rs(li, start, mid - 1, target)
    else:
        return bs_rs(li, mid + 1, end, target)


def bs(li, target):
    li.sort()
    start = 0
    end = len(li) - 1

    while start <= end:
        mid = (start + end) // 2
        if li[mid] == target:
            return mid
        elif target < li[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return -1


if __name__ == '__main__':
    # li = [3, 9, 21, 4, 7, 11, 28, 16]
    # print(sorted(li))
    # result = bs_rs(li, 0, len(li) - 1, 0)
    # print(result)

    li = [3, 9, 21, 4, 7, 11, 28, 16]
    print(sorted(li))
    result = bs(li, 4)
    print(result)
