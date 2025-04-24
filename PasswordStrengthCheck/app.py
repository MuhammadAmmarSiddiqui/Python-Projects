import streamlit as st

st.title("Password Strength Checker")
password  = st.text_input("Enter your password")

countUpper : int = 0
countLower : int = 0
countSpace : int = 0
specialChar : list = ['!','@','#','$','%','^','&','*','<','>','/','|','+','=','`','~','-','_','{','}','[',']','(',')','?']

print(len(password))
if (len(password)) >= 8:
    for i in password:
        if i.isupper():
            countUpper += 1
        elif i.islower():
            countLower +=1
        elif i.isspace():
            countSpace +=1
            
    has_special = any(char in specialChar for char in password)
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)
    
    #st.write("Uppercase letters", countUpper, "Lowercase letters", countLower, "Spaces", countSpace)
    if countUpper == 0 or countLower == 0:
        st.error("Password must contain at least one uppercase and one lowercase letter")
    elif not has_special:
        st.error("Password must contain at least one special character")
    elif not has_letter or not has_digit:
        st.error("Password must contain atleast one alphabet and one number")
    else:
        st.success("Password is strong")

        
else:
    st.error("Minimum 8 characters are required")
