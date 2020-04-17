def solution(numbers, target):
    if not numbers:
        if target == 0:
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


# def dfs(nums, target, current):
#     sub_count = 0
#     if not nums:
#         if current == target:
#             return 1
#         else:
#             return 0
#     else:
#         sub_count += dfs(nums[1:], target, current + nums[0])
#         sub_count += dfs(nums[1:], target, current - nums[0])
#     return sub_count


import unittest


class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.input = [1, 1, 1, 1, 1], 3
        self.result = 5

    def tearDown(self) -> None:
        pass

    def test_solution(self):
        result = solution(*self.input)
        self.assertEqual(self.result, result)
