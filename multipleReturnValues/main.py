def format_name(f_name, l_name):
    titleFirstName = f_name.title()
    titleLastName = l_name.title()
    return f"{titleFirstName} {titleLastName}"


titleName = format_name(input("What's your first name?"), input("What's your last name? "))
print(titleName)