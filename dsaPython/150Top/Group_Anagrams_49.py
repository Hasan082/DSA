from typing import List


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
