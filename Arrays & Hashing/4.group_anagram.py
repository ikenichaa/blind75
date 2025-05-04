from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            print(ord('b'))
        return list(res.values())


if __name__ == "__main__":
    print(Solution.groupAnagrams(Solution, ['eat', 'bat', 'a', 'tea', 'ate']))