"""
739. Daily Temperatures
Difficulty: Medium
Topics: Array, Stack, Monotonic Stack

Problem:
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature. If there is no future 
day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Use a monotonic decreasing stack to track temperatures waiting for warmer days.
        Stack stores indices of temperatures in decreasing order.
        """
        stack = []  # Monotonic stack storing indices
        n = len(temperatures)
        answer = [0] * n
        
        for i in range(n):
            # Pop all temperatures that are cooler than current temperature
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                answer[idx] = i - idx
            stack.append(i)
        
        return answer


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
    expected1 = [1, 1, 4, 2, 1, 1, 0, 0]
    assert solution.dailyTemperatures(temperatures1) == expected1
    print(f"Test 1 passed: {temperatures1} -> {expected1}")
    
    # Test case 2
    temperatures2 = [30, 40, 50, 60]
    expected2 = [1, 1, 1, 0]
    assert solution.dailyTemperatures(temperatures2) == expected2
    print(f"Test 2 passed: {temperatures2} -> {expected2}")
    
    # Test case 3
    temperatures3 = [30, 60, 90]
    expected3 = [1, 1, 0]
    assert solution.dailyTemperatures(temperatures3) == expected3
    print(f"Test 3 passed: {temperatures3} -> {expected3}")
    
    print("\nAll tests passed! ✓")


if __name__ == "__main__":
    test_solution()