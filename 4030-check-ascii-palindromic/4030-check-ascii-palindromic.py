class Solution:
    def isPalindromic(self, s: str) -> bool:
        
        binary_str = "".join(format(ord(ch),"08b") for ch in s)
        if binary_str == binary_str[::-1]:
            return True
        else:
            return False
        
        
        