from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    dic = {}
    for w in strs:
        sw = "".join(sorted(w))
        if sw in dic:
            dic[sw].append(w)
        else:
            dic[sw] = [w]
    gp = []
    for m in dic.values():
        gp.append(m)
    return gp


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs2 = [""]
strs3 = ["a"]
print(groupAnagrams(strs1))
print(groupAnagrams(strs2))
print(groupAnagrams(strs3))
