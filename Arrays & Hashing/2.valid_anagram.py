class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
        """
        if len(s) != len(t):
            return False
        
        char_s = {}
        char_t = {}
        for i in range (len(s)):
            char_s[s[i]] = 1 + char_s.get(s[i], 0) 
            char_t[t[i]] = 1 + char_t.get(t[i], 0) 
        
        # Check dictionary similarity
        return char_s == char_t

if __name__ == "__main__":
    print(Solution.isAnagram(None, "car", "jar"))
    print(Solution.isAnagram(None, "racecar", "carrace"))