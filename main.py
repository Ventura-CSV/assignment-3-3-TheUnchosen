def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = True
    if email[0].isalpha:
        result = False
    if email.len < 5 or email.len > 30:
        result = False
    if email.find("@") == -1:
        result = False
    if email.find(".") == -1 or (email.find("@") > email.find(".")):
        result = False
    
    
    if result == False:
        print("this is for testing, delete before submission")
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
