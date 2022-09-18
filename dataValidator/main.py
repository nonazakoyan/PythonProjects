chechnum = int(input('''input the number for checking data:
                    1. Email
                    2. Website URL
                    3. Date(dd.mm.yyyy)
                    4. Number
                    5. Credit Card Number
                    6. Mobile Phone Number
>>> '''))
if not (0 < chechnum < 7):
     print("Entering number is wrong! ")
     exit()

data = input("input checking data: ")

def checkEmail(data):
    if data.count("@") == 1:
        lst1 = data.split("@")
        if not (lst1[0] != "" and lst1[1] != ""):
            return False
        if lst1[1].count(".") == 1:
            lst2 = lst1[1].split(".")
            if not (lst2[0] != "" and lst2[1] != ""):
                return False
        else:
            return False
        return True
    return False
    
def checkURL(data):
    index = data.find('.')
    if index == -1:
        return False
    if data[ : index + 1] not in ("https://www.", "http://www."):
        return False
    if data[index + 1:].count('.') == 1:
        lst1 = data[index + 1:].split(".")
        if not (lst1[0] != "" and lst1[1] != ""):
                return False
        return True
    return False

calendar = {"01" : "31", "02" : "28", "03" : "31", 
                "04" : "30", "05" : "31", "06" : "30", 
                "07" : "31", "08" : "31", "09" : "30",
                "10" : "31", "11" : "30", "12" : "31"
            }

def is_leap_year(year):

    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return 0

def chechDate(data):
    if data.count(".") == 2:
        lst = data.split(".")
        if len(lst[0]) == 2 and lst[0].isdigit() and \
                len(lst[1]) == 2 and lst[1].isdigit() and \
                len(lst[2]) == 4 and lst[2].isdigit():

            if lst[1] in calendar.keys():
                if is_leap_year(int(lst[2])):
                    calendar["02"] = "29"
                    if 0 <= int(lst[0]) <= int(calendar[lst[1]]):
                        return True
                    return False
                else:
                    if 0 <= int(lst[0]) <= int(calendar[lst[1]]):
                        return True
                    return False
    return False
        
def checkNum(data):
    return data.isdigit()

def chechCredit(data):
    lst = data.split(" ")
    if len(lst) == 4:
        for i in lst:
            if not (len(i) == 4 and i.isdigit()):
                return False
        return True
    return False

def checkPhoneNum(data):
    if data.find("+374") == 0:
        if len(data[4:]) == 8 and data[4:].isdigit():
            return True
        return False
    return False

data = data.strip()
if chechnum == 1:
    print(checkEmail(data))
elif chechnum == 2:
    print(checkURL(data))
elif chechnum == 3:
    print(chechDate(data))
elif chechnum == 4:
    print(checkNum(data))
elif chechnum == 5:
    print(chechCredit(data))
elif chechnum == 6:
    print(checkPhoneNum(data))
