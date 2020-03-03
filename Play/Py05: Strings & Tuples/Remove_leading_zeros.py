"""
Write a Python function remove_leading(ip) that, given a string with an IPv4 address ip, returns a new string with all leading zeros removed from ip. An IPv4 address is an address in the format N.N.N.N, where N is an integer in the interval [0, 255].
"""
def remove_leading(ip):
    parts = ip.split('.')
    result = []
    for i in parts:
        if i.count('0') > 0 and len(i) > 1 and i.count('0') != len(i):
            i = i.lstrip('0')
        elif i.count('0') == len(i):
            i = '0'
        result.append(i)
    return '.'.join(result)
