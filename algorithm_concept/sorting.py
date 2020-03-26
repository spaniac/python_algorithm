# 1 10 5 8 7 6 4 3 2 9
from unittest import TestCase


def selection_sort(array):
    for i in range(len(array)):
        min_index, min_val = 99, 99
        for j in range(i, len(array)):
            if array[j] < min_val:
                min_index = j
                min_val = array[j]
        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp
    return array


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - (i + 1)):
            if array[j] > array[j + 1]:
                tmp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = tmp
    return array


def insertion_sort(array):
    for key in range(1, len(array)):
        index = key
        key_value = array[key]
        while index > 0 and array[index - 1] > key_value:
            array[index] = array[index - 1]
            index -= 1
        array[index] = key_value
    return array


def partition(array, left, right):
    pivot = array[left]
    low = left + 1
    high = right

    while low < high:
        while low <= right and array[low] < pivot:
            low += 1
        while high >= left + 1 and array[high] > pivot:
            high -= 1

        if low > right:
            low -= 1
        if high < left + 1:
            high += 1

        if low < high:
            temp = array[low]
            array[low] = array[high]
            array[high] = temp

    if pivot > array[high]:
        temp = array[high]
        array[high] = array[left]
        array[left] = temp
        print(array)

    return high


def quick_sort(array, left, right):
    """
    left: quick sort 범위의 시작, right: quick sort 범위의 끝
    low: 피벗의 위치 + 1, high: right
    pivot 값의 크기를 기준으로 정렬
    """
    if left < right:
        pivot_index = partition(array, left, right)

        quick_sort(array, left, pivot_index - 1)
        quick_sort(array, pivot_index, right)

    return array


def merge(array, result, left, middle, right):
    merged_index = left
    left_index = left
    right_index = middle + 1

    while left_index <= middle and right_index <= right:
        if array[left_index] <= array[right_index]:
            result[merged_index] = array[left_index]
            left_index += 1
        else:
            result[merged_index] = array[right_index]
            right_index += 1
        merged_index += 1

    if left_index <= middle:
        for i in range(left_index, middle + 1):
            result[merged_index] = array[i]
            merged_index += 1
    else:
        for i in range(right_index, right + 1):
            result[merged_index] = array[i]
            merged_index += 1

    array[left:right + 1] = result[left:right + 1]


def merge_sort(array, result, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(array, result, left, middle)
        merge_sort(array, result, middle + 1, right)
        merge(array, result, left, middle, right)

    return result


def inc_insertion_sort(array, first, last, gap):
    for key_index in range(first + gap, last + 1, gap):
        index = key_index
        key_value = array[key_index]
        while index > first and array[index - gap] > key_value:
            array[index] = array[index - gap]
            index -= gap
        array[index] = key_value


def shell_sort(array, size):
    gap = size // 2
    while gap > 0:
        if gap % 2 == 0:
            gap += 1
        for i in range(gap):
            inc_insertion_sort(array, i, size - 1, gap)
        gap //= 2

    return array


class TestSortingAlgorithm(TestCase):
    def setUp(self) -> None:
        self.array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
        self.expected_result = sorted(self.array)

    def tearDown(self) -> None:
        pass

    def test_selection_sort(self):
        self.assertEqual(self.expected_result, selection_sort(self.array))

    def test_bubble_sort(self):
        self.assertEqual(self.expected_result, bubble_sort(self.array))
        # self.assertEqual(self.expected_result, bubble_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))

    def test_insertion_sort(self):
        self.assertEqual(self.expected_result, insertion_sort(self.array))

    def test_quick_sort(self):
        self.assertEqual(self.expected_result, quick_sort(self.array, 0, len(self.array) - 1))

    def test_merge_sort(self):
        result = [0] * len(self.array)
        merge_sort(self.array, result, 0, len(self.array) - 1)
        self.assertEqual(self.expected_result, result)

    def test_shell_sort(self):
        self.assertEqual(self.expected_result, shell_sort(self.array, len(self.array)))


"""
* 선택정렬에 대한 복잡도
이중 반복문으로 인해 array의 길이가 n일 때 n + (n-1) + (n-2) + ... + 2 + 1 = n(n+1) / 2
=> O(n^2)의 시간복잡도
입력값이 커지면 커질수록 효율이 급격히 감소할 것이다.
길이가 짧은 리스트라면 뭐든 상관없겠지만, 방대한 데이터의 정렬에는 적합하지 않은 듯 하다.

* 버블정렬에 대한 복잡도
역시 이중 반복문으로 인해 array의 길이가 n일 때 (n-1) + (n-2) + ... + 2, 1 = (n-1)n / 2
=> O(n^2)의 시간복잡도
제일 큰 수가 가장 앞에 있을 때 가장 마지막 위치로 이동하면서 위치가 바뀌는 연산을 하기 때문에
구현은 가장 쉽지만 효율은 가장 좋지 않은 정렬 알고리즘이다.

* 삽입정렬에 대한 복잡도
이중 반복문 => O(n^2)의 시간복잡도
다만 삽입정렬은 어느 정도 정렬이 된 입력에 대해서는 정렬 알고리즘 중 가장 빠른 속도를 보인다.
왜냐하면 while문의 조건에 따라 필요할 경우에만 정렬을 하기 때문이다.
이 말은, 이미 정렬된 리스트에 추가로 정렬해야 하는 데이터들이 순차적으로 들어올 때 적절한 위치에 집어넣어 빠르게 정렬할 수 있다는 뜻이다.

* 퀵정렬
불안정 정렬, 비교 정렬
평균적으로 매우 빠른 정렬 속도를 자랑.
분할정복 알고리즘(divide, conquer, combine) -> 순환 호출(재귀)
비균등분할정렬 

* 병합정렬
안정정렬, 분할정복 알고리즘, 균등분할정렬 
단점: 입력을 리스트로 하면 임시 배열이 하나 필요하다 -> 제자리 정렬이 아니다
    입력이 커지면 속도가 현저히 느려진다.
장점: 입력이 링크드리스트일 때 링크 인덱스만 변경하면 되므로 데이터 이동은 무시할 수 있을 정도로 작아진다 -> 제자리 정렬이 가능해진다.


* 힙정렬


* 셸 정렬

"""
