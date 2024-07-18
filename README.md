# Mentality Blog:


![Mentality Blog Website](static/assets/images/responsiveness.JPG)


Mentality Blog is a platform designed for logging journal entries related to mental health. It provides users with a safe space to share their feelings, experiences, and resources with like-minded individuals, fostering a supportive community for collective benefit.

This blog offers a personal yet open space for those struggling with their mental health to find solace and support from others on a similar journey. Users can post their thoughts, track their mood for specific days, and share valuable resources such as articles, podcasts, videos, and books for the benefit of the entire community.

The live application can be viewed here : 

(https://mentalhealth-blog-59e7f6f2fb53.herokuapp.com/)


# Purpose and Target Audience:
 **Problem Statement:** Many individuals struggle to manage their mental health and track their emotional well-being, often resulting in increased stress and anxiety. The absence of a support structure can further intensify these mental health challenges.

**Purpose:** This mental health journal app offers a simple and intuitive way for individuals to log and share their thoughts and feelings, track their mental health, and identify patterns to improve emotional well-being. It also fosters connections with like-minded individuals who are on the same journey.

**Target Audience:** The primary target audience includes individuals seeking to improve their mental health, such as students, professionals, and anyone interested in mindfulness and self-care, as well as those looking for a stronger support structure.


# User Stories, Wireframes and Agile Methodology:

## User Stories:
* As a site user I can view a list of journal entries so that I can select which journal entry I want to read.
    Acceptance Criteria:
    * Given more than one journal entry entry in the database
    * When a user opens the main page a list of journal entries is seen
    * The user sees all journal entry headings and information to choose what to read
* As a site user I can register an account so that I can add journal entries.
    Acceptance Criteria:
    * Given a username, email and password a user can register an account
    * The user can log in
    * When the user is logged in the can add journal entries
* As a site user/admin I can view individual journal entries so that I can read the conversation.
    Acceptance Criteria:
    * Given one or more user journal entries the admin can view them
    * The site user can click on the journal entries to read the conversation
* As a site user I can modify or delete my journal entry so that I can amend my journal entry.
    Acceptance Criteria:
    * A logged in user can update their journal entry
    * A logged in user can delete their journal entry
* As a site admin I can create, read, update and delete posts so that I can manage the blog content.
    Acceptance Criteria:
    * A logged in user can create a journal entry
    * A logged in user can read a journal entry
    * A logged in user can update a journal entry
    * A logged in user can delete a journal entry


## Wireframe & Initial Design:
### Home Page

![Mobile and Desktop Wireframe - Homepage](static/assets/images/wireframe-mobiledesktop-homepage.jpg)

### (Logged in) View Journal Entries

![Mobile and Desktop Wireframe - View Journal Entries](static/assets/images/wireframe-mobiledesktop-journalentriespage.jpg)

### Create a Journal Entry

![Mobile and Desktop Wireframe - Add a Journal Entry](static/assets/images/wireframe-mobiledesktop-addjournalpage.jpg)

### Edit a Journal Entry

![Mobile and Desktop Wireframe - Edit/Delete Journal Entry](static/assets/images/wireframe-mobiledesktop-editdeletejournalpage.jpg)


## Agile:
This project was developed using Agile principles, utilizing a Kanban board on GitHub. As my first experience implementing Agile as an individual developer, creating user stories and identifying acceptance criteria provided a clear roadmap for targeting the application's features and functionalities. This approach kept me focused and minimized distractions.

![Project Kanban Board](static/assets/images/kanbanboard.JPG)


# Design Choices:

## Colour scheme:

![Project Colour Scheme](static/assets/images/colourscheme.png)

The colours were selected with the intention of complementing the hero image and the idea was to ensure the overall experience was calming.

## Typography:
The following fonts were chosen for a clean, modern and calming look that is both easily readable and simplistic.

* Headings - Playfair Display
* Paragraphs - Arial, sans-serif


## Priority Features:

### Home Page:

#### Navbar & Hero Image:
![Home Page - Navbar & Hero Image](static/assets/images/navbar-heroimage.JPG)

The landing page introduces the website and features a call-to-action button encouraging new users to sign up. Once signed up and logged in, users can view journal entries and create their own for others to interact with via comments.

The navigation bar is user-friendly, offering quick access to key sections of the website. It includes links to Home, Journal Entries, Create Journal Entry, Register/Logout, and Sign In. A hero image with graphics enhances the page's aesthetic appeal, clearly conveying the website's purpose and inviting users to join the community.


#### Registration:

Registration enables users to access journal entries and relevant resources within the community. It allows them to create, edit, and delete their own journal entries, ensuring the community content remains current and engaging.

#### Sign-Up:

![Sign-Up Page](static/assets/images/signuppage.JPG)


#### Sign-In:

![Sign-In Page](static/assets/images/signinpage.JPG)


#### Journal Entries:

![Journal Entries](static/assets/images/journalentriespage.JPG)


#### Add a Journal Entry:

![Add a Journal Entry](static/assets/images/addjournalentrypage.JPG)


The form allows users to effortlessly create journal entries that will be displayed on the journal entries page for others to browse. Users also have the ability to edit and delete their own entries, giving them complete control over their contributions.


#### Footer:

![Footer](static/assets/images/footer.JPG)

The footer links redirect users to our social media pages, providing a way to stay connected with Mentality Blog on various platforms and receive updates about any changes over time.


# Future Features:

<!-- * Implement a review system so readers can share their thoughts about books that they have completed. This will give others a better idea of whether the book is a good fit for them. 
* Display if a book is available with a status (Available, Not Available).
* Allow users to reserve a book beforehand.
* A search engine where users can search for books by title, author and genre.
* Provide locations of nearest libraries.
* Provide a way for the users to engage and form a secure community.
* Include an about page to inform others of how The Book Booth Library works and how to use it. -->


Database Design:

![ERD](static/assets/images/mh-erd.png)


Entity Relationship Diagrams (ERD) assist developers in establishing connections between databases and information. Crafting an ERD enhanced my comprehension of the relationships between tables. Utilizing dbdiagram.io facilitated the creation of the diagram, with arrows symbolizing the data field relationships.


## Data Models:


| User   |            |   |
|----------|:-------------:|------:|
| User_id |  IntegerField | FK |
| Username |  CharField   |   |
| Email | CharField |     |
| Password |  CharField |  |
| Created_at |  CharField   |   |
| Role | CharField |     |




| JournalEntry   |            |   |
|----------|:-------------:|------:|
| Title |  CharField |  |
| Slug |  SlugField |  |
| User |  ForeignKey | FK |
| Published_on |  DateTimeField |  |
| Entry_text |  TextField |  |
| Mood |  IntegerField |  |
| Resource |  ForeignKey | FK |
| Resourcetitle |  CharField |  |
| Resourceurl |  URLField |  |


| Resource   |            |   |
|----------|:-------------:|------:|
| Title |  CharField |   |
| Resource_type |  CharField | PK |



## User Flow Chart:
![Mentality Blog Flowchart](static/assets/images/website-flowchart.png)

The flowchart was instrumental in guiding crucial decisions throughout the app's development process. It enabled me to pinpoint key considerations for users and administrators alike, while also establishing robust authentication protocols. Furthermore, it assisted in prioritizing vital features such as adding, editing, and deleting journal entries.

# Validation
## HTML

<!-- | Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![home page validate](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/2ba0ff6e-6159-47e9-ad4c-2fe954589ca8) | Pass: button is a descendant of a tag |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705) | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467) | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3) | unclosed elements main and div | -->

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
<!-- | File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enhttps://jigsaw.w3.org/css-validator/validator) | ![validate css](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/200fc160-1092-4cd0-bba4-2ab1a721eb72) | Pass: No Errors | -->

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

<!-- | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/run.py) | ![screenshot]![forms py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f299346f-bb44-43a2-a8a5-868373d753e3)
 | Pass: No Errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py) | ![screenshot]![settings py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7951202c-2d55-4adb-90d6-8fef0707c82c)
 | Pass: No Errors |
| Book views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/blog/views.py) | ![screenshot]![views py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f545d53-b304-4600-b9fb-d4feb93b6c93)
 | Pass: No Errors |
| Book urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/checkout/urls.py) | ![screenshot]![urls py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e3f52187-1f65-4171-b1ba-e9096d1b5fc0)
 | Pass: No Errors |
|  models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/profiles/models.py) | ![screenshot]![models py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f3438ec1-f275-44b6-847d-48a93c0466ed)
 | Pass: No Errors | -->

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

<!-- * Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen -->

 Mobile Devices:
<!-- * Google Pixel 4a -->

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

<!-- ![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a) -->


* Microsoft Edge

<!-- ![microsoft edge](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/1570a9cd-6591-45db-840b-ecbe7f7aeb5b) -->


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

<!-- ![Screenshot_20231207-234024](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0f0b0d7d-a72f-43a4-8a57-bc1cf02a1367)

![Screenshot_20231207-234033](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4c3cc202-b8f6-4f9d-b1bd-cf57c911db65)

![Screenshot_20231207-234013](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/39989e07-4e8d-4faf-8b57-e11686792b38)


![0](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/211095bf-ffac-42ca-b1c8-2a45d8444038)

![Screenshot_20231207-234117 (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e52d022b-d3fb-4f6c-8fcb-092386ce566b)

![Screenshot_20231208-000014](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0cd224f9-b46e-4db9-9260-999cc63fff90) -->





Tablet Devices:


<!-- ![homepage](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5e6eb5c7-4aba-434c-8ed8-8bfd56632f8a)

![signup tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5f5a237-83ee-4ef3-b9b0-444f648ca225)

![sign in tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9ac1d08b-d4b8-4aa5-a65b-e46040f3b60b)

![books tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a9c42d34-a49a-48ed-97ba-660c02de3543)

![tabletadd](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b516d61d-6e21-460a-b7f4-5b18abf41d00)

![bookdetails tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/17a0f099-ae15-4b8a-887b-254beac2dbb0) -->





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

<!-- ![homeaudit](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5fa9bac2-d4bf-47fe-bb4a-50b3b0c4938b) -->

Books 

<!-- ![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d6401b01-e4d5-4ed1-b8e9-ff6d5eeb4bd9) -->

Add a book 
<!-- ![audit add book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e429ee62-ecbe-4b2f-8521-28da15773a46) -->

On a mobile device:

Home 
<!-- ![audit home mobile ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/348889e3-8c4e-41d4-b1c6-2c974780e23b) -->

Books
<!-- ![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fad662af-54da-45d0-b381-c0d70955e4e4) -->

Add a book 
<!-- ![audit addbookmobile](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/634965ca-1b9d-4aa1-bd17-bda89f9fbafe) -->


## Links

<!-- | Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Fail |
| Home | Navigates to the home page when clicked | Pass |
| Books | Navigates to a book list  page when clicked | Pass |
| Add a Book | Navigates to a form to add a book when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass | -->

## Testing 


<!-- | Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9e8658e8-f751-4cdf-be3d-ca19ad6c47b2)
| User logged in | Text displays the user logged in with their username | Pass | ![modal sign in name](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/cc4a71db-9962-49c1-b4b6-563000687ad7)
| View books | Users can see available books which have been added | Pass | ![testing books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/01cc3a5b-db46-4742-a8e1-cf715d78c89b)
| Add a book | Add a book to the book collection that will be available to borrow | Pass | ![addbook](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/82133f44-d43a-4f40-863a-f4e8970057aa)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a book | A user can edit the details on the book that they have addded. It will update their addition on the books page | Pass | ![edit book ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a book | A user who added a book OR an admin can delete a book. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e9e6c4e1-c90a-4854-a11c-014a8fc80043)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/3fafee34-e6d6-4162-8989-faa78e1bf355)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
| Grid display | A CSS grid will display the books in a clear, responsive format | Pass | N/A
| Functional buttons | Edit, delete, create buttons will be functional throughout the site | Pass | ![edit delete buttons](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/67cfb78d-7d5b-4072-8aa8-812b9c444b67)
| Footer | A footer displays social information | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)
| Social links work | The social links will navigate to a new page when they're clicked. They will open in a new tab | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f) -->


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* CI Database Generator used as the Postgres database.
* Heroku used for hosting the deployed back-end site.
* Cloudinary used for online static file storage.
* Canva Utilized for collaborative design and prototyping(wireframes).
* Google, Stack Overflow and Phind utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML5
* CSS
* Python

# Deployment :

I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

# Bugs

* Slug Field not operational yet due to the Comments model not being created as yet. This would be a future feature to implement and the slug field would be used to link the journal entry to the comment and also allow for editing and deleting comments. Currently, this does not affect the user CRUD functionality.

* Horizontal scroll tab appears on the Journal Entries page when pagination occurs past 6 journal entries. This does not affect the user experience however it is something that would be resolved in the future.

Most bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the following future features:

* 




# Credit: 

* Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by reaching to fellow students in the cohort and drawing inspiration from the walkthrough project on the LMS.

* Tutor Support, Google, Stack Overflow, Phind and ChatGPT was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* Thank you to all the other individuals in our cohort for their continuous support throughout the course.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes were created with Balsamiq and Canva.

* Flowcharts were created using LucidChart.

* The text and descriptions were generated by ChatGPT.