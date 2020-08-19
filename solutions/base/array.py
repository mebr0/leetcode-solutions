from typing import List


# noinspection PyMethodMayBeStatic,PyPep8Naming,PyRedeclaration
class Solution:
    # id26 _Array _TwoPointers
    # Todo: see tp
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Iterate nums:
        If current element is equal to next ->
            Iterate with j for all equal elements:
            If they are equal -> delete first one
        Increment i
        Return new length of nums
        """
        i = 0

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                j = i
                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    del nums[j]

            i += 1

        return len(nums)

    # id27 _Array _TwoPointers
    # Todo: see tp
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Iterate nums:
        If element equal to val -> delete it
        Otherwise -> increment i (In case of delete, same i will point to next element)
        Return new length of nums
        """
        i = 0

        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1

        return len(nums)

    # id35 _Array _BinarySearch
    # Todo: see binary search solution
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Iterate nums
        If num is greater or equal to target -> i
        Otherwise -> length of nums (i.e. target must be at the end of nums)
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)

    # id66 _Array
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Start from the last element and increment it
        If number is 10 -> zero it and increment left digit (cycle)
        If left most digit incremented is 10 -> zero it and append 1 as first element
        """
        right = len(digits) - 1

        while True:
            if right < 0:
                digits.insert(0, 1)
                break
            else:
                digits[right] += 1

            if digits[right] != 10:
                break

            digits[right] = 0
            right -= 1

        return digits

    # id80 _Array _TwoPointers
    # Todo: see tp
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                j = i
                while j < len(nums) - 2 and nums[j] == nums[j + 1] == nums[j + 2]:
                    del nums[j]

            i += 1

        return len(nums)

    # id118 _Array
    def generate(self, numRows: int) -> List[List[int]]:
        """
        For each row:
        Create row with first number 1
        If it is first row -> append row to result and continue
        Otherwise -> iterate through previous row pairs and append sum of pair to current row
        Append last 1 to row
        Append row to result
        Return result with rows
        """
        result = []

        for i in range(numRows):
            row = [1]

            if i == 0:
                result.append(row)
                continue

            previous = result[i - 1]

            for j in range(len(previous) - 1):
                row.append(previous[j] + previous[j + 1])

            row.append(1)

            result.append(row)

        return result

    # id119 _Array
    def getRow(self, rowIndex: int) -> List[int]:
        """
        For every value within [0, rowIndex]:
        Append to result combination of rowIndex and i
        Return result
        """
        result = []
        i = 0

        while i != rowIndex + 1:
            result.append(self._combination(rowIndex, i))
            i += 1

        return result

    # Todo: check how it works (copy pasted from stackoverflow)
    def _combination(self, n, r):
        import operator as op
        from functools import reduce

        r = min(r, n - r)

        numerator = reduce(op.mul, range(n, n - r, -1), 1)
        denominator = reduce(op.mul, range(1, r + 1), 1)

        return numerator // denominator

    # id121 _Array _DynamicProgramming
    # Todo: see dp solution
    def maxProfit(self, prices: List[int]) -> int:
        """
        Iterate over the list:
        If price is less than min_price -> override min_price
        If difference between price and min_price is greater profit than max_profit -> override max_profit
        Return max_profit
        """
        min_price, max_profit = 100000000000, 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    # id122 _Array _Greedy
    # Todo: determine whether this greedy
    def maxProfit(self, prices: List[int]) -> int:
        """
        Iterate over the list
        If price is less than min_price -> override min_price
        If difference between price and min_price is greater profit than max_profit ->
            check next nums till they decreasing
        After finding longest increasing sequence, add max_profit to _sum
        Set i to j - 1 (previous number while searching end of increasing sequence)
        """
        _sum, min_price, max_profit = 0, 100000000000, 0
        i = 0
        size = len(prices)

        while i != size:
            if prices[i] < min_price:
                min_price = prices[i]

            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

                j = i + 1

                while j != size and prices[j] > prices[j - 1]:
                    max_profit = prices[j] - min_price
                    j += 1

                _sum += max_profit
                min_price, max_profit = 100000000000, 0
                i = j - 1

            i += 1

        return _sum

    # id169 _Array _DivideAndConquer _BitManipulation
    # Todo: see d&c and bm solutions
    def majorityElement(self, nums: List[int]) -> int:
        """
        Count all elements
        Iterate counter:
        If count greater than half of length of nums -> num
        """
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            if count > len(nums) // 2:
                return num

    # id229 _Array
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Count all elements
        Iterate counter:
        If count greater than thirds of length of nums -> append num to result
        Return result
        """
        counter, result = {}, []

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, count in counter.items():
            if count > len(nums) // 3:
                result.append(num)

        return result

    # id414 _Array
    def thirdMax(self, nums: List[int]) -> int:
        """
        Create three variables for first, second and third maximums
        Iterate over all numbers:
        If first not set or current number greater than first -> make second maximum third, first second, number first
        If current number equal to first -> ignore it
        If second not set or current number greater than second -> make first second, number first
        If current number equal to second -> ignore it
        If third not set or current number greater than third -> make number third
        If third not set -> return first maximum
        Otherwise -> return third maximum

        """
        first, second, third = None, None, None

        for num in nums:
            if first is None or num > first:
                third = second
                second = first
                first = num
            elif num == first:
                continue
            elif second is None or num > second:
                third = second
                second = num
            elif num == second:
                continue
            elif third is None or num > third:
                third = num

        if third is None:
            return first
        else:
            return third

    # id509 _Array
    # Todo: see matrix exponential and golden ratio solutions
    def fib(self, N: int) -> int:
        """
        If N <= 1 -> N
        If N == 2 -> 1
        Create variables for two previous values, current value and index 3
        Iterate till N + 1:
        Override current value by sum of two previous
        Update previous values
        Return current
        """
        if N <= 1:
            return N

        if N == 2:
            return 1

        first, second, current, i = 1, 1, 0, 3

        while i < N + 1:
            current = first + second
            first = second
            second = current

            i += 1

        return current

    # id643 _Array
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return 0

        _max = -1000000000000

        for i in range(0, len(nums) - k + 1):
            _max = max(_max, sum(nums[i:i + 5]))

        return _max

    # id674 _Array
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        If nums is empty -> return 0
        Create longest sequence size and current sequence size
        For every number compare with next number:
        If next one is greater -> increment current
        Otherwise -> sequence ended, override longest if current is greater and set current to 1
        After left from for override longest again (for last element)
        Return longest
        """
        if len(nums) == 0:
            return 0

        longest, current = 1, 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                current += 1
            else:
                longest = max(current, longest)
                current = 1

        longest = max(current, longest)

        return longest

    # id989 _Array
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        """
        Add each digit from K to A (If no digit -> insert)
        Start from the last element
        Set number to remainder to 10
        Set transfer to quotient to 10
        Repeat for each left digit
        """
        i = 1

        while K != 0:
            if i > len(A):
                A.insert(0, K % 10)
            else:
                A[-i] += K % 10
            K //= 10
            i += 1

        transfer = 0

        right = len(A) - 1

        while True:
            if right < 0:
                if transfer != 0:
                    A.insert(0, transfer)
                break
            else:
                A[right] += transfer

            transfer = A[right] // 10
            A[right] = A[right] % 10
            right -= 1

        return A

    # id1051 _Array
    # Todo: find better solution
    def heightChecker(self, heights: List[int]) -> int:
        """
        Create copy of heights and sort it
        Iterate over two lists
        If there is no matching -> increment count
        Return count
        """
        right_order = sorted(heights[:])
        count = 0

        for i in range(len(right_order)):
            if right_order[i] != heights[i]:
                count += 1

        return count

    # id1470 _Array
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        Iterate over the half of list:
        Append num itself and num shifted from i by n
        Return result
        """
        result = []

        for i in range(len(nums) // 2):
            result.append(nums[i])
            result.append(nums[i + n])

        return result