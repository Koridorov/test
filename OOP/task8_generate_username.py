def generate_username(f_name:str, l_name:str, email:str) -> str:
    if check_email(email)==False:
        print("Please enter a valid email. ")
        return ""
    elif email[-10:]=="@gmail.com":
        return f"{email[:-10].lower()}.{l_name[2::-1].lower()}"        
    else:
        return f"{f_name[:5].lower()}_{l_name[-5:].lower()}"



def check_email(email:str) -> bool:
    if "@" in email and len(email)<254:
        templist=email.split("@")
        if len(templist)==2:
            if (1<=len(templist[0])<=64 and
                not templist[0].startswith(".") and
                not templist[0].endswith(".") and
                not ".." in templist[0] and
                "." in templist[1]):

                return True
    return False


print(generate_username("Nikita", "Koridorov", "koridoroff1@abv.bg"))