Assignment: Login and Registration

Objectives:

Build an application that requires login and registration
Practice connecting a Flask application to a MySQL database
Become familiar with the logic that is required to validate a user's registration to a website
Become familiar with the logic that is required to validate a user logging in to a website
Process a user logging out of an application
Practice using session


In this assignment, you're going to build a Flask application that allows login and registration. We've learned about how we can connect to the database, insert records posted from a form, retrieve records from a database and set a session/flash for any error or success messages that we get along the way. One of the major components to every website is login and registration.

Registration

The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page 

Login

When the user initially registers we would log them in automatically, but for logging in, we need to validate in a different way:

Check whether the email provided is associated with a user in the database
If it is, check whether the password matches what's saved in the database
But how do we keep track of them once they've logged in? I think you might already know...session! We can create a session variable that holds the user's id. From our study in database design, we know that if we have the id of any table we can gather the rest of the information that is associated with that id. Storing a single session variable with the user's id is all we need to access all the information associated with that user.

Logout

On the success page, have a logout button or link. When a user logs out, their session should be cleared. If the user attempts to access the success page (i.e. making a GET request by typing in the url), redirect them back to the login and registration page.