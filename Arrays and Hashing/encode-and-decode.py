class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        # write your code here

        ret = ""

        for word in strs:
            ret += "#" + str(len(word)) + ":" + word

        return ret

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        # write your code here

        n = len(str)
        i = 0
        ret = []

        while i < n:
            if str[i] == "#":
                _len = ""
                word = ""
                while str[i] != ":":
                    _len += str[i]
                    i += 1
                _len = int(_len)
                for j in range(_len):
                    word += str[i]
                    i += 1
                ret.append(word)

        return ret
