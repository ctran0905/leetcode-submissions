class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while i != j:
            sum = numbers[i] + numbers[j]
            print(sum)

            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

        
