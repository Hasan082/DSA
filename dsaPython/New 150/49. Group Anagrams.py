from collections import defaultdict


def groupAnagrams(strs):
    maps = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - 97] += 1
        maps[tuple(count)].append(s)
    return list(maps.values())


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs1))  # [["bat"],["nat","tan"],["ate","eat","tea"]]
