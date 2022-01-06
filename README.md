# Corona-Project
This project is a site for schools in the Covid-19 times. In this project we are trying to help students in grade schools that cant go to the school because of the covid-19 virus.

The authors : Rotem Hadad, Itay Ben Yair, Tal Maimon, Israel Lasry

The work environment : VS Code, Python, Django, HTML, CSS, SQLite3

Setup & Installation : Make sure you have the latest version of Python installed, VS Code - and inside install: Django & debug-toolbar & pipenv:

pip install pipenv

pipenv install django

pip install django-debug-toolbar

run the program : python manage.py runserver

Explain who to register to the site:

First, the manager should buy the site and we need to add his ID to the data base so he can register

we are currently registering a manager with the ID 123456789
teachers with ID's:20998866,963852741
Students of a teacher with an ID 20998866:

Student.1:20118899

Student.2:20118877

Student.3:20118866

Student.4:20118855

Students of a teacher with an ID 963852741:

Student.1:147258369

Student.2:20118844

Student.3:20118833

Student.4:20881133

Student.5:20118822

After you login to the web you can see all the function you can do with Permissions.
After the acton we realized that we need to make some changes and add system requirements to improve it and bring the project to a better and better quality state so we added requirements and changes
And these are the changes:
New requirements:
After the acton following the theoretical step and the suggestions we made for the additions we chose to add a requirement that allows the principal to add a tutor to the site. That is, a requirement that allows the principal to enter an identity card for a new teacher admitted to the system, this addition will allow the teacher to register on the site and automatically belong to his school (this requirement was also added in (meister task)
We also added disengagement buttons for each of the participants - teacher and student supervisor a total of 3 requirements.
Additions to existing requirements:
* Attendance - Adding an attendance report at the end of each attendance reading - so that the teacher has an indication of his students' submissions, adding the student's status (red / green) next to each line in attendance so that the teacher knows why the student missed - in addition to checking that no student is in status Edom did not come to school
* Sample of red students by the principal - to this requirement is added a graph showing the percentage of green and red students in the school (in addition to printing how many red and green students there are in each class)
* Student homework - an option has been added to the requirement to indicate that homework has been done and thus he will not have a highlighted notice on the home page about homework.
* Principal - status of all teachers in red - it was decided that it would be printed on the home screen and not on a dedicated button because it is important that the principal sees which of his teachers are red directly at each login to the system
* Administrator - Questionnaire for students in red status - it was decided to add to the principal a guide on how to insert a Google Forms link + add a link that will take it directly to Google Forms, so that he can quickly send the link after filling in the questionnaire fields.
