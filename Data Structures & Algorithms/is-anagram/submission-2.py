class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # store s and t in hash tables, hash_s and hash_t
        # save frequencies of each char in these hashes
        # loop through c in s
        # if hash_s != hash_t, return False 
        # if make it through whole loop, return True

        hash_s = {}
        hash_t = {}

        for c in s:
            hash_s[c] = hash_s.get(c, 0) + 1
        
        for c in t:
            hash_t[c] = hash_t.get(c, 0) + 1

        if len(s) > len(t):
            for c in s:
                if c not in hash_t:
                    return False
                if hash_s[c] != hash_t[c]:
                    return False
            return True
        else:
            for c in t:
                if c not in hash_s:
                    return False
                if hash_t[c] != hash_s[c]:
                    return False
            return True
            