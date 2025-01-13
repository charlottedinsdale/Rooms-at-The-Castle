# Introduction

Rooms at The Castle is a room booking website designed to advertise rooms in a pub in the Devonshire countryside to potential customers. Customers are able to learn about the pub's location and history as well as view the individual rooms on offer. Testimonials written by authorised user's are visible on the homepage and can be edited and deleted by users if they wish. In order to make a booking the user must sign up to the website, after which they can book through an interactive calendar. 

![Screenshot 2025-01-13 134700](https://github.com/user-attachments/assets/b69bff4c-e8a0-4255-b052-a01ee4ee85f9)

![Screenshot 2025-01-13 140953](https://github.com/user-attachments/assets/0aafcf12-ae94-4d6d-8d77-a5bdde001a44)


*Disclaimer*
The project was developed for eductional purposes as part of my studies at the Code Institute. Whilst it is based on a real-life place with potential for real application in the future, it has also been designed to meet assessment critrea and demonstrate my capabilities as a Full-Stack Software Developer. Therefore the project conatins a mix of real images and content alonside stock images and 'made-up' content. 

## Project Goals

Design and build an engaging and straight-forward website advertising The Castle to potential guests.
Create a fully functional booking system where availability is updated each time a booking is made or the admin has blocked a time-period. 
Allow users to book through a calendar that is simple and intuative, providing clear user feedback.
Ensure that the admin has full control over all bookings and user information, as well as the ability to create, edit and update room details.
Ensure that the user can create, edit, read and delete testimonials in order to give feedback on their experience to the owner and other guests.

## Target Audience

The target audience for the website is broad, targetting any member of the publuc looking to stay somewhere in Devon - whether for business or pleasure. The rooms are advertised to suit a variety of guests - from single guests to couples to families.

# User Stories

User stories were developed in the early stages of the project and prioritised in the workflow using MosCow Prioritisation. I used GitHub's project feature to track development using a Kanban board; moving the user stories into relevant sections as development progressed and labelling with priority tags (Must Have, Should Have, Could Have).

Below are some example titles of user stories that were created for this project.
All user stories along with their acceptance criterea and status in the project can be viewed <a href="https://github.com/users/charlottedinsdale/projects/4/views/1" target="_blank">here</a> on the project board.

## User Stories
- Create an account
- View rooms 
- Book rooms
- Admin add rooms
- Admin view bookings
- Write tetimonials
- Edit or delete testimonials
- Edit or delete testimonials
- Submit a contact form

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

## Favicon/Logo

I designed a favicon/logo for The Castle with the aim to create a simple, easily-identifiable logo that represented the brand and looked good on browsers in both light and dark mode. I based the design on the medieval castle image on the signage for the pub. Below is the Favicon (left) and The Castle signage (right).

![castle-logo](https://github.com/user-attachments/assets/202f0923-042d-45d6-94fc-4a41cdc39c63) ![Castle Signage](https://github.com/user-attachments/assets/ae60c9d2-e0bf-42f6-90b4-d99813f1b783)


## Wireframes

Similarly to the ERD, wireframes were designed in the project ideation phase and modifications were made to the design and layout later in the project develpment. Key features in the deployed website such as the header, footer and page layout are very similar to the wireframes, but other features differ. The contact page has not been included in the first release due to time constraints and prioritisation, but is intended for a later release.


### Home and About
![Screenshot 2025-01-11 142410](https://github.com/user-attachments/assets/c169c814-5025-4db9-9bea-923053519812)

### Rooms, Booking and Contact
![Screenshot 2025-01-11 142440](https://github.com/user-attachments/assets/55024d74-254f-4a12-ba37-fc6d35d7b4da)

### Booking Confirmation
![Screenshot 2025-01-11 142447](https://github.com/user-attachments/assets/4f94f9d4-f761-4b7a-b2f9-9492187dd813)

### Mobile Wireframes
![Screenshot 2025-01-11 142401](https://github.com/user-attachments/assets/1d7b7c54-1ad3-4f0d-ac0e-b4fa2bf2fcf4)


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
- flake8

### Other Technologies

- SmartDraw to create the ERD
- Balsamiq to design the wireframes
- PowerPoint to design Favicon/Logo
- Am I Responisve? for responsiveness testing and feature image

# Features 

## Existing Features 

### Django Admin Page

The Django superuser (page administrator) can access a customised Django admin page where they can view, edit and delete Bookings, Room Availability status', Testimonials and Rooms. They also have the ability to approve a testimonial before it is posted to the website. 

### Home Page

The home page features a fully-responsive navbar and header, as well as and 'About' section, 'Testimonials' section, a Google Calendar iframe and footer containing contact information. The home page features three images between the sections which create a parallax scrolling effect, and the header shrinks on scrolling. 

### Testimonials

Within the home page is a testimonial section containing user-written testimonials shown in a carousel, as well as a testimonial form for authorised users to submit their own testimonial if they wish. Autherised users can also edit and delete their own testimoials.

### Room Pages

The 'Rooms' page features a list of all rooms on the database, showing an image of the room, the room capacity, number of beds and price per night. Users can then click on individual rooms and view the room in detail, where they can see a description of the room and click on the 'book now' button to make a booking.

### Booking Page

Once user's have selected a room to book, they are taken to the 'Booking Page' where they can choose the number of guests and select a start and end date from a calendar. The calendar fetches Room Availabity data to dynamically display available and unavailable dates (which users cannot select) to the user. A modal appears once the date selection has been made so that users can confirm their selection before submitting the booking. The total booking price is shown to the user before they submit the booking form. Once the form is submitted the user is shown a booking confirmation, with their booking reference and a summary of the booking.

## Future Improvements

Due to the time constraints of the project and issues arising during development that weren't factored into the initial planning and prioritisation phases, there are some features that I would have liked to have improved on and certainly will for future updates. These include:

- notifications on the admin panel when a testimonial has been edited by adding an updated_on field to the Testimonial model
- better Calendar UX and checks to ensure that end_date cannot be before start_date and bookings cannot be made for dates in the past
- another modal with total price would be shown before submission of a booking, with users being able too cancel or continue

## Features to Implement in Future 

The Contact Page, including user contact form and admin email reply feature will be implemented for the next release. This will allow users to ask questions about The Castle and its rooms to help them decide on aspects of their booking and will allow the owners to recieve feedback from users. This would likely also lead to the addition of an FAQs section as laid out in the Contact Page wireframe.

There will also be a 'Manage Bookings' page where authorised users can manage their current bookings and view details for previous bookings. This will allow users to request cancellations or updates to their stay period or number of guests etc.

There will also be an addition to the Testimonials section, where authorised users can chose to view only their own testimonials from the carousel, so that when there is more data, the user can filter out their own testimonials more easily in order to edit or delete them as they please.

A method for taking payments would be implemented should the site be used in the future, as it has been designed intitially for educational purposes, this was not included in the initial development phase.

# Testing

## Code Validation

### HTML Validation

W3C's HTML validation was used to validate HTML in the project, and some errors were highlighted relating to attributes and nesting. Some were addressed, however due to time constraints, not all errors have been addressed at this point. Some examples can be seen below.

![HTML Validation](https://github.com/user-attachments/assets/2f48cff8-d708-4b1d-ad05-340456215032)

### CSS Validation

CSS was also validated using W3C's validation tool and the project met CSS3 standards with no errors found.

![CSS Validation](https://github.com/user-attachments/assets/a543a78d-2c79-4adf-9e26-35f770ddecf9)

### Python Linting

Python linting using the Code Institute's Linter tool and Flake8 extension highlighted quite a few errors in my python code due to line length. There were a few indentation errors and whitespace errors which were corrected, however due to time constraints most line length errors were not corrected. These will be corrected for future releases and in the future I would use Flake8 to address these errors throughout development.

### Performance Testing

Lighthouse performance testing was used to test performance, accesibility, best practices and SEO on the deployed site. Initial performance testing highlighted a major hinderence due the size of the main homepage image and due to unused JavaScript largely attributed to FullCalendar. Below is a comparison between the performance rating before compressing the key image and after. I will look to optimise further by cutting down on unused JavaScript for future releases.


![Lighthouse Testing before Compression](https://github.com/user-attachments/assets/26cb1360-0012-48c1-b5a1-631b1c53fa6e)![Lighthouse Testing after Compression](https://github.com/user-attachments/assets/bc9d9d4c-396e-4ff6-a14e-480d1348a088)

## Manual Testing


| Feature       | Expected Behaviour | Pass/Fail |
| ------------- | -------------      | --------- |
| Sign Up  | Users can sign up to the website by creating a username and secure password. They are then redirected to the homepage. | Pass |
| Sign In  | Content Cell       |           |
| Sign Out  | Content Cell       |           |
| View Rooms  | Content Cell       |           |
| Select Room  | Content Cell       |           |
| Make Booking  | Content Cell       |           |
| Submit Testimonial  | Content Cell       |           |
| View Testimonials  | Content Cell       |           |
| Delete Testimonial  | Content Cell       |           |
| Edit Testimonial  | Content Cell       |           |
| Manage Rooms on Admin Panel  | Content Cell       |           |
| View Users on Admin Panel  | Content Cell       |           |
| Manage Bookings on Admin Panel  | Content Cell       |           |
| View Room Availability on Admin Panel  | Content Cell       |           |
| Block Rooms on Admin Panel  | Content Cell       |           |
| Approve Testimonials on Admin Panel  | Content Cell       |           |

### Account Creation

### Room View

### Room Booking

### Testimonial Submission

### Testimonial Deletion

### Testimonial Editing

### Admin Panel
- Adding a Room
- Adding Availability Status (blocking rooms)
- Managing Accounts
- Viewing Bookings
- Managing Testimonials

# Reflection on Development Process

## Successes

As my first Full-Stack project using the Django framework I am very proud of what I've managed to produce in 3 weeks. I am particularly pleased with the implementation of a dynamic calendar for bookings, the JavaScript elements on the homepage and overall look of the site. 

## Challenges

I faced quite a few challenges when implementing the dynamic calendar and linking JavaScript and Python logic in order to make the bookings and editing testimonial functions work successfully. With perserverance and practice after created mulptiple apps and models (and some help from Kevin) I was able to overcome many of the challenges faced. 

A key challenge was the time constraint of the project and in the future I would look to improve on code validation and python linting at an earlier stage. Use of a project board and well planned user stories was invaluable to being able to produce the project within the assesssment period.

# Deployment

To deploy the project, user's would need to fork the repository and link this to their own Heroku account, generating their own CONFIG VARS including SECRET_KEY and DATABASE_URL. Ensure that Debug is set to False on deployment. 

The site was regularly deployed to Heroku in the development stages. The following steps were taken before initial deployment:
- Django project and first app 'rooms' were set up 
- env.py created, and DATABASE_URL and SECRET_KEY were added and linked to settings.py in project
- env.py added to gitignore to ensure secruity of DATABASE_URL and SECRET_KEY
- gunicorn installed and added to requirements.txt by running "pip3 requirements freeze --local" after installment
- Procfile created and "web: gunicorn the_castle.wsgi" added so Heroku knows how to run project
- App created in Heroku and linked to GitHub repository
- DATABASE_URL and SECRET_KEY added to CONFIG VARS in the app settings
- Debug set to False before deployment

The following steps were taken before each subsequent deployment:
- Debug set to False
- Any new packages installed added to requirements.txt
- Any changes were commited to GitHub

The final live site is deployed to Heroku and available for viewing here: https://the-castle-fe36c8bb2ab4.herokuapp.com/.

# Sources

- W3 Schools for parallax code
- Freepik for generic room images
- FullCalendar for JavaScript calendar and documentation
- chatGPT for project ideation prompting, room descriptions and code troubleshooting
- Google Maps for map iframe
- The Castle Hotel for homepage images and address 

# Acknowledgements

Thank you to all the teaching staff at the Code Institute, especially Kevin for his help getting the calendar functionality in place, John and the rest of the Coding Coaches for their help with bugs and Paul for his constant motivation and feedback.


