class Solution(object):
    def maxArea(self, height):
        left=0
        right=len(height)-1
        max_area=-1
        max_of_height=max(height)
        while left<right:
            area=min(height[left],height[right])*(right-left)
            if max_area<area:
                max_area=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            #we can add a check , if maximum number in height times next width still smaller than or equal to
            #our current max_area , current max_area must be the largest area
            if max_area>=(right-left)*(max_of_height):
                break
        return max_area
