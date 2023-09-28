def twoNumberSum(array, targetSum):
    sett = set()
    for i in array:
        if targetSum-i not in sett:
            sett.add(i)
        else:
            return [i,targetSum-i]
    return []
