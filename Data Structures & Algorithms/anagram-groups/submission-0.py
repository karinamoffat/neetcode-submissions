class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # make a dictionary of lists by default so we don't have to handle edge case

        for s in strs:
            count = [0] * 26 # every string starts with a fresh count
            for c in s:
                count[ord(c) - ord("a")] += 1 # create the key (encoding for the string)
            res[tuple(count)].append(s) # if empty just return an empty string, otherwise add the string to the end of the list for this key
        return list(res.values())
            