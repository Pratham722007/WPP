def replace_with_loop(s, old, new):
    result = ""
    i = 0
    len_old = len(old)

    while i < len(s):
        if s[i:i+len_old] == old:
            result += new
            i += len_old
        else:
            result += s[i]
            i += 1

    return result


original = input("enter a string")
wanttoreplace=input("enter string you want to replce with")
whomtoreplace=input("enter which string to replace")
replaced_string = replace_with_loop(original, wanttoreplace,whomtoreplace )
print(replaced_string)
