from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stack = sandwiches[:]
        unable = 0
        j = 0
        for student in students:
            if stack and student == stack[j]:
                stack.pop(j)
                j = 0
            else:
                stack.append(student)
                j+=1
            
            unable += 1 if j >= len(stack) else 0
        print (stack)
        
        return unable


sol = Solution()
students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
print(sol.countStudents(students, sandwiches))
