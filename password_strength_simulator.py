def check_password(password):
    if len(password) < 8:
        return "length"
    if not any(char.isupper() for char in password):
        return "uppercase"
    if not any(char.islower() for char in password):
        return "lowercase"
    if not any(char.isdigit() for char in password):
        return "digit"
    if not any(char in "!@#$" for char in password):
        return "symbol"
    return "valid"

def main():
    while True:
        s = input('Generate the password: ')
        error_type = check_password(s)
        if error_type == "valid":
            print("Password accepted! Strong password.")
            break
        match error_type:
            case "length":
                print("Too short! Aim for 8+ characters.")
            case "uppercase":
                print("Missing an uppercase letter!")
            case "lowercase":
                print("Missing a lowercase letter!")
            case "digit":
                print("Missing a digit!")
            case "symbol":
                print("Missing a symbol! Use one of: !, @, #, $")

main()
