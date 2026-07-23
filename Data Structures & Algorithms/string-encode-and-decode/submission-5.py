class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        count = [0] * len(strs)

        for i, string in enumerate(strs):
            count[i] = len(string)
        
        combined = "".join(strs)

        new = []

        for char in combined:
            if ord(char) > 245:
                new.append(chr(ord(char) % 5))
            new.append(chr(ord(char) + 10))
        new = "".join(new) + str(count)
        
        return new

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        new = s.split('[', 1)
        count = new[1]
        new = new[0]
        count = count.split(']', 1)[0]
        print(count)
        print(new)

        temp = []
        for char in new:
            if ord(char) < 10:
                temp.append(chr(ord(char) + 245))
            temp.append(chr(ord(char) - 10))
        print(temp)

        count = count.strip('[]')
        count = list(map(int, count.split(',')))
        print(count)

        beginning = 0
        res = []
        for val in count:
            v = temp[beginning:beginning + val]
            res.append("".join(v))
            beginning += val
        return res
