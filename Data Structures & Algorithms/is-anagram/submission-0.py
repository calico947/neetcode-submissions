class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(nlogn) approach involves sorted() which is an expensive process
        # return sorted(s) == sorted(t)

        # Compare this to Counter(), which only requires a linear (O(n)) search
        # This is because it utilizes hash tables AKA dictionaries, keeping track
        # of a char and it's # of appearacnes as a key-pair
        return Counter(s) == Counter(t)
