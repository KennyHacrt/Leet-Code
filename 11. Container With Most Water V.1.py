class Solution(object):
    def maxArea(self, height):
        max=0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                if i==j:
                    continue
                if height[i]>height[j]:
                    a=height[j]
                else:
                    a=height[i]
                if a*(j-i)>max:
                    max=a*(j-i)
        return max
