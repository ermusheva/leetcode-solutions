"""
1700. Number of Students Unable to Eat Lunch
Difficulty: Easy
Topics: Array, Stack, Queue

Problem:
The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
Otherwise, they will leave it and go to the queue's end.
This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

 

Example 1:

Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0 
Explanation:
- Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
- Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
- Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
- Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
- Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
- Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
Hence all students are able to eat.
Example 2:

Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3
 

Constraints:

- 1 <= students.length, sandwiches.length <= 100
- students.length == sandwiches.length
- sandwiches[i] is 0 or 1.
- students[i] is 0 or 1.

"""

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        num_unsatistied_students=0
        while students and num_unsatistied_students < len(students):
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                num_unsatistied_students = 0
            else :
                students.append(students.pop(0))
                num_unsatistied_students +=1

        return num_unsatistied_students


def test_solution():
    """Test cases for the solution"""
    solution = Solution()
    
    # Test case 1
    students = [1,1,0,0]
    sandwiches = [0,1,0,1]
    expected1 = 0
    result1 = solution.countStudents(students.copy(), sandwiches.copy())
    assert result1 == expected1
    print(f"Test 1 passed: {students}, {sandwiches} -> {expected1}")

    
    # Test case 2
    students = [1,1,1,0,0,1]
    sandwiches = [1,0,0,0,1,1]
    expected2 = 3
    result2 = solution.countStudents(students.copy(), sandwiches.copy())
    assert result2 == expected2
    print(f"Test 2 passed: {students}, {sandwiches} -> {expected2}")
    
    
    print("\nAll tests passed! ")


if __name__ == "__main__":
    test_solution()