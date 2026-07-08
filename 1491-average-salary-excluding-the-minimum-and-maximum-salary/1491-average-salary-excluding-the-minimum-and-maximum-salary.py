class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = min(salary)
        maxSalary = max(salary)

        count = 0
        totalSalary = 0

        for s in salary:
            if s != minSalary and s != maxSalary:
                count += 1
                totalSalary += s
        
        return totalSalary / count