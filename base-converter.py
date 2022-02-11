#num is string with digits less than inbase
#inbase and outbase from 2 to 10
def base_changer(num: str, inbase: int, outbase: int):
	#if either of these are true, it means that the inbase or outbase would be <= 1 or >= 11
    if abs(inbase-6) > 4 or abs(outbase-6) > 4:
        return "invalid inbase or outbase (needs to be more than 1 and less than 11)"
    
    BaseTenNum = 0
    for i in range(-1, -len(num)-1, -1):
        if int(int(num[i]) >= inbase):
            return "invalid digit for given inbase"
        BaseTenNum += (int(num[i]) * (inbase**(-i-1)))
    
    result = ""
    while BaseTenNum != 0:
        result = str(BaseTenNum % outbase) + result
        BaseTenNum = BaseTenNum // outbase
    return result
