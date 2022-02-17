class Solution:
    def reverseWords(self, s: str) -> str:
        # get rid of extra spaces 
        s= list(s)
        slow = 0
        while s[slow] == ' ':
            slow += 1
        start = slow
                
        last = len(s)-1
        while s[last] == ' ':
            last -= 1
        last += 1
        
        for fast in range(start, last):
            if s[fast] == ' ' and s[fast] == s[fast-1]:
                continue
            else:
                s[slow] = s[fast]
                slow += 1
        s = s[start:slow]
        
        # reverse the string and words 
        def reversing(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        reversing(0, len(s)-1)
        
        last = 0
        for i in range(0, len(s)):
            if s[i] == " ":
                reversing(last, i-1)
                last = i+1
            elif i == len(s)-1:
                reversing(last, i)   
        
        return ''.join(s)
            
''' previous solution '''
# class Solution:
#     def reverseWords(self, s: str) -> str:
        
#         list_s = s.split(" ")
        
#         lst = [x for x in list_s if x != ""]
        
#         return " ".join(reversed(lst))