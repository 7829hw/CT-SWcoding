def isleapyear(y):
    return (y % 4 == 0 and y % 100 != 0) or y % 400 == 0

"""
    return 1 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 0
"""

""" 
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return 1
    else:
        return 0
"""

year = int(input())
print(isleapyear(year))
