class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        # enumerate() - tracks both index & value of items
        for index, value in enumerate(nums):
            # value that is needed to be added ip
            complement = target - value

            if complement in seen:
                return [index, seen[complement]]

            seen[value] = index