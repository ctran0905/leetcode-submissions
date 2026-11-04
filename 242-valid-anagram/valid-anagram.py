class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def sortString(s: str) -> dict:
            freq = {}
            sorted_str = sorted(s)

            for letter in sorted_str:
                if letter in freq:
                    freq[letter] = freq[letter] + 1
                else:
                    freq[letter] = 1
            return freq
        
        s_freq = sortString(s)
        t_freq = sortString(t)

        return list(s_freq.keys()) == list(t_freq.keys()) and list(s_freq.values()) == list(t_freq.values())

