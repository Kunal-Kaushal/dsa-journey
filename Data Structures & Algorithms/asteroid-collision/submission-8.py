class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for a in asteroids:
            if a>0 or not stack or (stack[-1]<0 and a<0):
                stack.append(a)
            else:
                while stack:
                    if stack[-1]<0 and a<0:
                        stack.append(a)
                        break
                    if abs(stack[-1])>abs(a):
                        break
                    elif stack[-1]==a:
                        stack.append(a)
                        break
                    elif abs(stack[-1])==abs(a):
                        stack.pop()
                        break
                    elif abs(stack[-1])<abs(a):
                        stack.pop()
                        if not stack:
                            stack.append(a)
                            break
        return stack