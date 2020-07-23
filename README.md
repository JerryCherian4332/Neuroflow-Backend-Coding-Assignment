# Neuroflow-Backend-Coding-Assignment

In order to login the username is admin and password: 123456.

The api covers the most basic functionality required in the assignment. If it were a production application, the login functionality would be way more secure and the password would be hashed and all user info would be stored in a database. I hardcoded the user and password, however this information would be pulled from a database. I would look into Flask-Login which seems like a way better option for implementing login functionality. In addition, the streak information should be stored in a database as well, along with the previousLoginDate. All of these would be pulled for each respective logged in user so the code can be reused. If it needed to handle more users or data the code would remain the same except some code would be replaced with code that accomodated with pulling the data from a database.
