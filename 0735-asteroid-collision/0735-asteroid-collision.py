class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                collide = stack[-1] + a

                if collide > 0:
                    a = 0
                elif collide < 0:
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            
            if a:
                stack.append(a)
        
        return stack