# Test Cases for Login and Registration

## Prerequisites

```
URL:        https://www.mytheresa.com/en-de/customer/account/login
First Name: FirstName
Last name:  LastName
E-Mail:     test@user.com
Password:   P@ssw0rd
```

# User Interface Test Cases

## Registration

---
### GUIT-1: Basic registration scenario

New user can register on the site

1. Open registration URL
2. Use data from prerequisites to input in a fields
3. Click Register button

**Expected Result:**

User will be registered correctly and will be able to see his profile page

---
### GUIT-2: Try to register already registered user

Already registered users cannot register again with same credentials

1. Open registration URL
2. Use same data from prerequisites to input in a fields
3. Click Register button

**Expected Result:**

User will be prompted that user with given email is already registered

---
### GUIT-3: Invalid E-Mail

When the user enters an invalid email that doesn't have '@' symbol or .com

1. Open registration URL
2. Use names and password from prerequisites to input in the fields
3. In the email, field enter invalid email (for example invalidemail.com or invalid@email)
4. Click Register button

**Expected Result:**

User will be prompted that email should contain '@' symbol and ends with .com or any other type of domain

---
### GUIT-4: Incorrect password

The user enters correct and valid email but the password is too short or simple

1. Open login URL
2. Use names and login email from prerequisites to input in a fields
3. In the password field enter an invalid password (for example wrongPassword)
4. Click Register button

**Expected Result:**

User will be prompted that password should contain more that 6 characters excluding leading or trailing spaces

---
### GUIT-5: User didn't enter some of the fields

User can try to register without entering any of the required fields

1. Open login URL
2. Don't enter anything in email, password or names fields, or leave them empty
3. Click Register button

**Expected Result:**

In any case, user will be prompted that both names, email and password are required

---
### GUIT-6: Size restriction to input fields

User can't input names or password, that contains more than 50 symbols

1. Open registration URL
2. In all input fields, try to enter more than 50 symbols
3. Use data from prerequisites to input in a fields
4. Click Register button

**Expected result:**

User will get this warning:
```
"first name" length must be equal or less than 20 characters.
"last name" length must be equal or less than 25 characters.
"Email" exceeds the allowed length.
```

---
### GUIT-7: Check information after registration

Confirm that all information about user, like names and title are saved correctly

1. Open registration URL
2. Use data from prerequisites to input in a fields
3. Click Register button
4. Open user profile page (https://www.mytheresa.com/en-de/customer/account/)

**Expected result:**

In a Account Information section should be stored correct values of name and e-mail

---
### GUIT-8: Switch between input fields with Tab key

User should be able to switch between input fields with Tab key to fill form without using mouse

1. Open registration URL
2. Place cursor on one of the fields (for example first name)
3. Press Tab

**Expected result:**

Cursor should move to the next field below (to the last name)

---
### GUIT-9: Submit form by pressing Enter

After filling all forms, user should be able to submit form with Enter button

1. Open registration URL
2. Use data from prerequisites to input in a fields
3. Press Enter to submit form

**Expected result:**

If all fields was filled correctly and this user doesn't exist, form will submit and new user will be created

---
### GUIT-10: Password field is encrypted

Symbols in password field should be hidden with stars

1. Open registration URL
2. Enter anything in password field

**Expected result:**

All symbols in password field should be masked as stars and protected from copying 

---
### GUIT-11: Password and Confirm Password comparison

Symbols in password and confirm password fields should be the same and validated before submit

1. Open registration URL
2. Enter some symbols in password field (for example: Password)
3. Enter other symbols in confirm password field (for example: notSamePassword)

**Expected result:**

User will get warning that passwords don't match and will not be able to register