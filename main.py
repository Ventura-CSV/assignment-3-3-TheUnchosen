def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    result = True
    if email[0].isalpha() != True:
        result = False
    if len(email) < 5 or len(email) > 30:
        result = False
    if email.find("@") == -1:
        result = False
    if email.find(".") == -1 or (email.find(".") < email.find("@")):
        result = False
  
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
