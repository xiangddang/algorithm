def timeConversion(s):
    # Write your code here
    if s[8:10] == "PM":
        if s[:2] != "12":
            s = str(int(s[:2]) + 12) + s[2:]
    else:
        if s[:2] == "12":
            s = "00" + s[2:]
    return s[:8]