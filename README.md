
thorgate-hr
/
collins-kipkorir
Private
Test assignment for COLLINS KIPKORIR

 0 stars  0 forks
Code
Issues
Pull requests
Actions
Projects
Security
Insights
thorgate-hr/collins-kipkorir
Latest commit
@collinskipkorir
collinskipkorir
…
on Jan 28
Git stats
Files
README.adoc
Projement - simple project management tool
Table of Contents
Project overview
Structure overview
Setup
QuickStart
The Assignment
Read before you start.
Tasks
All rights reserved by Thorgate Management OÜ.
The contents of this repository can be reproduced, copied, quoted or
distributed only with written permission of Thorgate Management OÜ.
Project overview
Projement is a simplified tool for project managers. Project managers can have an overview of all the projects in a company. This includes estimated and actual hours spent on design, development and testing.

Important
This README just outlines the test assignment tasks and basic project setup. Make sure to check out the README files for the front-end and back-end. As they document how to run tests as well as linters.

Back-end readme: projement/README.adoc

Front-end readme: projement/app/README.adoc

Structure overview
Note
It is best to follow the structure section of the README in GitHub or GitLab since the links work best there. The assignment view of the web app does not handle linking to other files or folders.
The application is split into two parts – the back-end (written in Python & Django), and the front-end (written in JavaScript & React).

The general folder structure for the project can be seen below:

├── docker             # Includes Docker files for both front and back-end
├── Makefile           # A bunch of utility commands to help developers
├── projement          # The Django app, back-end of the project
│   ├── app            # The React app, front-end of the project
│   │   └── README.md  # Useful information about the front-end
│   └── README.md      # Useful information about the back-end
├── README.md          # General overview of the project & the assignments (this file)
└── requirements.txt   # Python dependencies
To perform some routine operations, a Makefile with a set of make commands is provided. In order to run these commands, the GNU make utility needs to be installed. Some of the commands are listed below.

Tip
To see exactly what a make command is doing, you can run it with the -n argument.
make migrate -n will output:
echo -e "\033[0;36mRunning django migrations:\033[0m"
    docker-compose run --rm django ./manage.py migrate 
This that you can see how to run arbitrary django or node commands.
Setup
System Prerequisites
To be able to run the project in Docker environment, it’s necessary to have docker and docker-compose installed.\

Tip
Please refer to Docker installation docs and
Docker Compose installation docs to install them.
QuickStart
To build and setup the application from the ground up, just type:

make setup
This will create the necessary Docker containers and install the required Python and NPM packages.

Database
To start the database will be empty.

make setup also runs migrations automatically.

To manually migrate the database, run:

make migrate
Application data
At the start the project has no data in the database. No users, or projects.

To create a superuser:
make superuser
To load initial data for projects:
make load_initial_data
Running the application
make runserver
After a successful startup, the application should be accessible at http://127.0.0.1:8000.

Tip
There are a number of other useful make commands which you can check out with make help or by looking at the Makefile.

Also make commands can be chained together: make setup superuser load_initial_data will run all the above commands in order.

The Assignment
Read before you start.
Make sure to read through the whole assignment before you start writing your solutions. The last tasks might be more complicated than the first ones and, depending on the implementation, they might be related to each other.

Please use the best practices known to you to make the commits and manage branches in the repository.

We’ve set up formatters and linters for both back-end and front-end to help enforce best practices. You can run the linters with make quality.

We expect our engineers to provide high quality features and therefore to test the parts of their code that they feel should be tested. The same applies to you.

There are some example tests for both back-end and front-end, feel free to use them as a reference.

You can run tests for both back-end and front-end with make test.

If you’re running out of time or are not sure how to test a specific thing, add a comment where you describe what you would test and which scenarios you would test.

If you have any ideas on how to improve Projement - either on the architectural side, back-end implementation, code quality or developer experience - please write them down inside your Merge request.

This project is a simplified example of our project structure. Which is why some of the tools used here are not current best practice, partly so they can be pointed out in this assigment.

Imagine if this project came onto your table and the client wanted to improve it, what would be the first things you would do / offer to the client?

If you have any issues or questions about the tasks
If minor issue document them as TODOs in code comments and work around them to figure out the best solution.

For bigger issues you can also ask us via e-mail or phone, but it might take some time until we respond.

Finishing the Assignment
We expect an experienced full-stack developer to complete the assignment in 4-6 hours.
Taking longer is not a problem, but you still shouldn’t exceed a total of 8-10 hours.

We value your own time as well, so just us know what you’d have wanted to complete, if you were to spend more time.
Please do so in a code-comment in your MR in the most relevant places.

Important
When you have finished, create a Pull Request in GitHub containing the entire solution, and request for a review from the owner of the repository.
Tasks
1. Fix project ordering on the dashboard
Currently, the projects on the dashboard are ordered by start date. The project managers want to see them in a different order.

As a result of this task:

Projects on the dashboard must be ordered by end date descendingly.

Projects that have not ended yet, must be shown first.

Make sure that the projects' list in the Django admin has the same ordering.

2. Actual hours need to be decimals
Currently, all the actual hours (design, development, testing) for the Project model are integers. Project managers want to have more precision - they need to be changed to decimals.

As a result of this task:

The actual hours fields must be `DecimalField`s.

The actual hours must be in the range of 0 <= x < 10000 and have 2 decimal places.

All other changes necessary to keep the application running, must be made (e.g. migrations).

Make sure that it’s possible to save the decimal values through the front-end as well.

3. Incremental changes
When two people edit the same project at the same time, and both want to increase actual hours by 10, they end up with faulty results.

For example, if the actual development hours are currently 25 in a project, and two developers begin editing the form simultaneously, then both have an initial value of 25 in the form. They both did 10 hours of work, and thus insert 35 as the development hours.

After both have submitted the form, the actual development hours stored in the database are 35, even though both developers did 10 hours of work and the resulting value should be 45 (25+10+10).

This issue applies for all actual hours: development, design and testing.

As a result of this task:

Instead of entering the total amount of actual hours, the user only has to enter the additional amount of development, design and testing hours that they have spent since last update.

It must be possible for two users to enter their additional hours simultaneously, with both entries taken into account.

4. Weird results for "project has ended"
There are some weird results for the "project has ended" indicator in the Dashboard (when a project’s name has been crossed out). We’re not sure what exactly the problem is. The crossing out of projects seems to be pretty random at the moment.

As a result of this task:

The projects should be correctly crossed out if they have actually ended.

5. Slow dashboard
The project managers have noticed that the dashboard gets slower and slower when more projects have been added. We think that it might be because the database queries are not optimized.

As a result of this task:

The dashboard performance issues should be solved.

Note: You can use a management command to generate a lot of projects:

# Creates 300 projects by default
make loadmanyprojects
# You can also specify the number of projects to create:
make loadmanyprojects cmd="--nr-of-projects 100"
Note: This task should be done before pagination (Task 6) has been implemented as pagination can help a bit with performance. We would like a different solution from pagination in this task.

6. Add pagination to the dashboard
There are quite a lot of projects in the application and the project managers have noticed that the dashboard can get a bit slow and they would prefer not to scroll through a hundred projects. It would help if the list of projects in the dashboard was paginated.

As a result of this task:

The dashboard has a paginated list of projects.

The pagination should happen without a full reload of the page.

Describe how you would make the pagination and its user experience better if you don’t manage to implement everything. For example, write these as TODO-s in the README.md.

7. (Bonus) Replace SQLite with a better database management system
The project currently uses SQLite as its database engine. SQLite is great, but it’s not very well suited for large web applications (like Projement). It makes sense to move to something more scalable like PostgreSQL or MySQL.

As a result of this task:

The project should use PostgreSQL, MySQL, or some other more advanced database management system.

The database should run inside Docker and be started along with the rest of the application when running docker-compose up or make runserver.

The database should not lose any data between Docker restarts. For example, if the Docker containers are stopped (docker-compose down) and started again (docker-compose up).
