def get_leap_year(x:int) -> bool:
    if x % 400 ==0 or x % 100 != 0 and x % 4 == 0:       
        return True
    else:
        return False

print(get_leap_year(2000))
