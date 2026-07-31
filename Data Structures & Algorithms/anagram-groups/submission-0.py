class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {} # {sorted(str) : [str, str_2, str_3]}

        for word in strs:
            if "".join(sorted(word)) in anagram_dict:
                anagram_dict["".join(sorted(word))].append(word)
            else:
                anagram_dict["".join(sorted(word))] = [word]

        result = []

        for anagram in anagram_dict:
            result.append(anagram_dict[anagram])

        return result