# Full Stack Idea: Macro Tracker App

# Overview
This is a simple application to help users keep track of their daily diet and macros. Users will have the ability to create a daily list of the foods they have consumed,
and add the total protein, carbohydrates, fats, and calories of each meal and then
receive a cumulative score for the day.
The purpose of this application is to enable users to more seamlessly
track their day-to-day diet habits and progress towards improving nutrition. 

# Technologies used:
- HTML5
- CSS
- Javascript
- React
- Node
- PostgreSQL
- Python
- Django
- Bootstrap

# User Stories
- As a user, I want the ability to sign up for the application with a distinct username.
- As a user, I want the ability to log in after signing up.
- As a user, I want the ability to log out after being logged in.
- As a user, I want the ability to view all past daily macro trackers created by me.
- As a user, I want the ability to view my own user created trackers on a separate page from all trackers.
- As a user, I want the ability to create new tracker objects.
- As a user, I want the ability to delete tracker objects created by me.
- As a user, I want the ability to edit tracker objects created by me.
- As a user, I want the ability to click the App Logo and be redirected to my current daily tracker page.
- As a user, I want the ability to click "Your Tracker" and then be directed to a page where I can create my own tracker object (if a daily tracker has not been created yet)
- As a user, I want the ability to add individual meal objects to my daily tracker.
- As a user, I want the ability to edit individual meal objects in my daily tracker.
- As a user, I want the ability to delete individual meal objects in my daily tracker.
- As a user, I want the ability to see each individual meal object created by me listed in my daily tracker.
- As a user, I want the ability to see a cumulative sum and score for each macro and calories on my daily tracker.
- As a user, I want the ability to only create, view, edit, and delete tracker and meal objects while logged in. 
- As a user, I want the ability to be redirected to the sign-in page when trying to access other pages while logged out. 



# Wireframe/Screenshots
![Full-Stack-Project](Wireframes/Macro%20Tracker%20Wireframes.drawio.png)

# ERD
![Full-Stack-Project](Wireframes/Macro%20Tracker%20ERD.drawio.png)

# Weekly Plan
Monday - Create all data models, get Django backend server and settings setup, organize backend files and directories. Get React boilerplate code into repo.

Tuesday - Set up PostgreSQL database, test on localhost to make sure backend data functionality is up to speed. Continue testing basic backend infrastructure. Connect React to backend via Axios, and then compose basic JSX rendering to test backend connection.

Friday - Continue working on React views. Build out login, signup, and sign out pages first. Build first iteration of basic add and view tracker page, and then build basic add meal and edit meal pages.

Monday - Begin user profile page with React. Upon completion, circle back to Tracker and Meal pages to begin refactoring and adding more engaging design features.

Tuesday/Wednesday/Thursday - Continue refactoring design and test different themes and branding.
