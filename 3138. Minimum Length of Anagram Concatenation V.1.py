class Solution(object):
    def minAnagramLength(self, s):
        can=[]
        
        for i in range(len(s),1,-1):
            if len(s)%i==0:
                can.append(i)
        
        for j in range(len(can)):
            key=0
            t=len(s)//can[j]
            for k in range(1,can[j]):
                if ''.join(sorted(s[0:t]))==''.join(sorted(s[t*k:t*(k+1)])):
                    key+=1
            if key==can[j]-1:
                return t      
        return len(s)
