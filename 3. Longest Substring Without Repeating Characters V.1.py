def longestPalindrome(self, s):    
        l=len(s)
        max='0'
        key=0
        for i in range(1,l+1):
            for j in range(i):
                if j==0:
                    z=None
                else:
                    z=j-1
                y=j+l-i    +1 #j=1,i=4,
                if s[j:y]==s[y-1:z:-1]:
                    if len(max)<len(s[j:y]):
                        max=''
                        max=''.join(s[j:y])
                        key=1
                    break
            if key==1:
                break               
        if max=='0':
            return s[0]
        return max
