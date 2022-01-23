class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = []
        for i in s:
            if i.isalnum():
                lower_s.append(i.lower())
                
        while len(lower_s)>1:
            if lower_s.pop(0) != lower_s.pop():
                return False
            
        return True