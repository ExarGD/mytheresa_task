# Test Cases for Login and Registration

## Prerequisites

URL: https://www.mytheresa.com/en-de/customer/account/login

First Name: FirstName

Last name: LastName

E-Mail: test@user.com

Password: P@ssw0rd

# User Interface Test Cases

## Registration

### GUIT-1: Basic registration scenario

New user can register on the site

1. Open registration URL
2. Use data from prerequisites to input in a fields
3. Click Register button

Expected Result:

User will be registered correctly and will be able to see his profile page

### GUIT-2: Try to register already registered user

Already registered users cannot register again with same credentials

1. Open registration URL
2. Use same data from prerequisites to input in a fields
3. Click Register button

Expected Result:

User will be prompted that user with given email is already registered

### GUIT-3: Invalid E-Mail

When the user enters an invalid email that doesn't have '@' symbol or .com

1. Open registration URL
2. Use names and password from prerequisites to input in the fields
3. In the email, field enter invalid email (for example invalidemail.com or invalid@email)
4. Click Register button

Expected result:

User will be prompted that email should contain '@' symbol and ends with .com or any other type of domain

### GUIT-4: Incorrect password

The user enters correct and valid email but the password is too short or simple

1. Open login URL
2. Use names and login email from prerequisites to input in a fields
3. In the password field enter an invalid password (for example wrongPassword)
4. Click Register button

Expected result:

User will be prompted that password should contain more that 6 characters excluding leading or trailing spaces

### GUIT-5: User didn't enter some of the fields

User can try to register without entering any of the required fields

1. Open login URL
2. Don't enter anything in email, password or names fields, or leave them empty
3. Click Register button

Expected result:

In any case, user will be prompted that both names, email and password are required
