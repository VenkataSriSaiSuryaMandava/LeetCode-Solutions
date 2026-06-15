class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        
        for i in range(len(sandwiches)):
            count = 0

            while students[0] != sandwiches[i] and count < len(students):
                students.append(students.popleft())
                count += 1

            if count == len(students):
                return len(students)
            
            students.popleft()
        
        return 0