# Introduction

Rooms at The Castle is a room booking website designed to advertise rooms in a pub in the Devonshire countryside to potential customers. Customers are able to learn about the pub's location and history as well as view the individual rooms on offer. Testimonials written by authorised user's are visible on the homepage and can be edited and deleted by users if they wish. In order to make a booking the user must sign up to the website, after which they can book through an interactive calendar. 

## Project Goals

Design and build an engaging and straight-forward website advertising The Castle to potential guests.
Create a fully functional booking system where availability is updated each time a booking is made or the admin has blocked a time-period. 
Allow users to book through a calendar that is simple and intuative, providing clear user feedback.
Ensure that the admin has full control over all bookings and user information, as well as the ability to create, edit and update room details.
Ensure that the user can create, edit, read and delete testimonials in order to give feedback on their experience to the owner and other guests.

## Target Audience

The target audience for the website is broad, targetting any member of the publuc looking to stay somewhere in Devon - whether for business or pleasure. The rooms are advertised to suit a variety of guests - from single guests to couples to families.

# Epics and User Stories

All user stories along with their acceptance criterea and status in the project can be viewed <a href="https://github.com/users/charlottedinsdale/projects/4/views/1" target="_blank">here</a> on the project board.

## Epics
- 
-
-

## User Stories
-
-
-

# Design
## Look and Feel

The website has a professional and intuative design as it's purpose is to advertise The Castle for potential guests. The images and colourscheme chosen show both the inside and outside of The Castle and the colourscheme reflects the peaceful countyside within which the Castle sits. The image below is taken from the homepage, the first part of the website the user would see.

![Screenshot 2025-01-11 152309](https://github.com/user-attachments/assets/7ff31699-6851-4bab-a8ff-0ed62c71e9d2)

## Colourscheme

The design is intended to be simple and appealing, which is why a  muted green colourscheme was chosen. The colourscheme is also inspired by the Devon flag and reflects the colour of the pub itself.

The main Colourscheme:
![Colourscheme](https://github.com/user-attachments/assets/9dc9417f-a33a-4366-ac26-67bc034f184a)

The Devon Flag for reference:
![Devon Flag](https://github.com/user-attachments/assets/bb5e8fea-0f0d-4f3a-bb29-f339cb8ee132)

## Typography

Two fonts were chosen for the website, both imported from google fonts. The <a href="https://fonts.google.com/specimen/Cinzel" target="_blank">Cinzel</a> typeface was chosen for the title and other headings as it is similar to the typeface used on The Castle building itself, and reminds the user that The Castle is a traditional English pub with a long history. A contrasting sans-serif font; <a href="https://fonts.google.com/specimen/Ysabeau+Office" target="_blank">Ysabeau Office</a> was used or the main body text as it is easier to read in smaller text and has a professional but friendly feel.

## Wireframes

### Homepage
- img
### Rooms Page
- img
### Individual Room Page
- img
### Contact Page
- img
### Sign Up/In/Out Pages
- img
## Colour Scheme
- img
# Database Schemas

## Entity-relationship-model (ERD)

Initial entity-relationship diagram was created at the very beginning of the project. <strong>Note that the 'Review' model was renamed to 'Testimonial' during development.</strong>

![ERD](https://github.com/user-attachments/assets/6591e80c-ed52-4a5e-b004-b392d6ba0d21)

## Models

### User Model

The Django User model was used, but I included a model in the ERD in order to ensure all relationships were documented and excecuted correctly.

![User Model](https://github.com/user-attachments/assets/1973b6f9-b80d-4c72-9bcd-38ea8cf55738)

### Room Model

![Room Model](https://github.com/user-attachments/assets/9ec71ccd-e841-4675-a232-7c0619b78599)

### Room Availability Model

![Room Availability Model](https://github.com/user-attachments/assets/7b5b5428-079a-4b26-a3db-6cc39fe6912d)

### Booking Model

![Booking Model](https://github.com/user-attachments/assets/d8fc26b3-cb66-4519-9c9b-711800355016)

### Contact Form Model

This model has not yet been implemented and is intended for future release.

![Contact Form Model](https://github.com/user-attachments/assets/b6163e8a-078c-4515-a1d2-a53dfb931e09)

### Testimonial (formerly Review) Model

Note that the rating field was not included in the final model and an image field was included instead, along with an approved field. Whilst the image field was included in the model for first release, it is yet to be included in the user form and is intended for a future release.

![Testimonial Model](https://github.com/user-attachments/assets/758bdadd-fcac-42fc-880b-890b755bb6f3)

# Technologies Used

## Languages, Frameworks and Packages

The site was developed using a Django framework, with Python being the primary backend language. JavaScript was used for the calendar functionality and HTML was used alongside the Django template language to display data in the frontend. I used CSS and employed Bootstrap classes to style the website alongside some JavaScript for dynamic styling.

### Languages and Frameworks

- Python
- JavaScript
- HTML5
- CSS3
- Django
- Bootstrap

### Django Packages and Other Teachnologies

List taken from requirements.txt file in project.

- asgiref==3.8.1
- cloudinary==1.36.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==4.2.17
- django-allauth==65.3.0
- django-crispy-forms==2.3
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- pillow==11.0.0
- psycopg2==2.9.10
- sqlparse==0.5.3
- urllib3==1.26.20
- whitenoise==5.3.0

### Other Technologies

- SmartDraw was used to create the ERD
- Balsamiq was used to design the wireframes

# Features 

## Existing Features 

## Features to Implement in Future 

# Testing

## Code Validation

## Manual Testing

## Bugs 

### Unfixed Bugs

# Deployment

Webiste was deployed regularly to Heroku for testing. The final live site is deployed to Heroku and available for viewing here: https://the-castle-fe36c8bb2ab4.herokuapp.com/.

# Sources

- W3 Schools for parallax code
- Freepik for generic room images
- FullCalendar for JavaScript calendar and documentation
- chatGPT for project ideation prompting, room descriptions and code troubleshooting
- The Castle Hotel for homepage images and address 

# Acknowledgements

Thank you to all the teaching staff at the Code Institute, especially Kevin for his help getting the calendar functionality in place, Paul for the constant motivation and feedback and the Coding Coaches for their help with bugs.


