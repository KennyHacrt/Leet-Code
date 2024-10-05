def lengthOfLongestSubstring(self, s):
        char=[]
        max=0
        for i in range(len(s)):
            while s[i] in char:
                char.pop(0)
            char.append(s[i])
            if len(char)>max:
                    max=len(char)
        return max
