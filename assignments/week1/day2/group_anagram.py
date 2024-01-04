
# group anagram problem from leetcode
def groupAnagrams(strs):
    group={}
    for i in strs:
        sorted_string="".join(sorted(i))
        if sorted_string in group:
            group[sorted_string].append(i)
        else:
            group[sorted_string]=[i]
    return group.values()


