"""
84. Largest Rectangle in Histogram
Difficulty: Hard
Topics: Array, Stack, Monotonic Stack

Problem:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4

Constraints:
- 1 <= heights.length <= 105
- 0 <= heights[i] <= 104

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stack stores indices of heights in decreasing order
        n = len(heights)
        rightside = list(range(n, 0, -1)) # defauft value from list length to 1

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                rightside[idx] = i-idx
            stack.append(i)

        leftside = list(range(n)) # defauft value from 0 to n-1
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                leftside[idx] = idx-i-1
            stack.append(i)
        
        square = [0]*n
        max_square = 0
        for i in range(n):
            square[i] = (rightside[i]+leftside[i])*heights[i]
            if square[i] > max_square :
                max_square = square[i]


        return max_square


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    heights = [2,1,5,6,2,3]
    expected1 = 10
    assert solution.largestRectangleArea(heights) == expected1
    print(f"Test 1 passed: {heights} -> {expected1}")
    
    # Test case 2
    temperatures2 = [2, 4]
    expected2 = 4
    assert solution.largestRectangleArea(temperatures2) == expected2
    print(f"Test 2 passed: {temperatures2} -> {expected2}")
    
    print("\nAll tests passed! ✓")


if __name__ == "__main__":
    test_solution()