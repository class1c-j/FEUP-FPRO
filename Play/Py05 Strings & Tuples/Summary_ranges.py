"""
Given a comma-separated string astring with sorted integers without duplicates, write a Python function summary_ranges(astring) that returns a string showing the contiguous intervals in the set.
"""

def summary_ranges(astring):
    nums = [int(x) for x in astring.split(',')]
    nums = sorted(set(nums))
    gaps = [[s, e] for s, e in zip(nums, nums[1:]) if s+1 < e]
    edges = iter(nums[:1] + sum(gaps, []) + nums[-1:])
    ranges = list(zip(edges, edges))
    for i in range(len(ranges)):
        if ranges[i][0] == ranges[i][1]:
            ranges[i] = str(ranges[i][0])
        else:
            ranges[i] = str(ranges[i][0]) + '->' + str(ranges[i][1])
    return ','.join(ranges)
print(summary_ranges('0,1,2,3,4,5,7,10,11,20,21'))
