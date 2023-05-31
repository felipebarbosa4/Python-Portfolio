def format_name(f_name, l_name):
    titleFirstName = f_name.title()
    titleLastName = l_name.title()
    # print(f"{titleFirstName} {titleLastName}")
    return f"{titleFirstName} {titleLastName}"


firstName = "FeliPE"
lastName = "FigueIra"

# The return keyword will make the variable keep the values
titleName = format_name(f_name=firstName, l_name=lastName)
print(titleName)
