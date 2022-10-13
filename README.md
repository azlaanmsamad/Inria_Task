# Inria Task

This Repository contains Web Development Task to be completed as a part of the Inria selection Procedure.


## Problem Statement

- Develop a web app to receive 3 different signal inputted by the user and store it in the Database for backup. 
- Retreive the last 5 datapoints from the backend and display them with timestamps.
- Expose a REST API with a one method _clear_ that cleans all the data in the memory.
- Dockerizer the different functionalities.


### Status of different steps mentioned in the Task:
1. STEP 1 `-->` Done (Understanding the RoadMap)
2. STEP 2 `-->` Done (PROJECT SETUP: Creation of the Git Repo)
3. STEP 3 `-->` _Partially Done_ (Web App Development)
4. STEP 4 `-->` _TODO_ (Broker Integration)
5. STEP 5 `-->` Done (Database Integration)

## Installation
1. First install all the requirements `pip install -r requirements.txt`
2. Execute the command `python run.py` in the terminal.
3. Open a web browser and go to `http://127.0.0.1:5000/`

## Uses
1. After opening the browser a welcome page is displayed.
2. To add a user's name go to the Register tab and add the name. This will also store it in the database.
3. Click on Users (DB) tab to see the user name's that has been added to the database up until now.


## Approach
### Workflow:
1. Create a Frontend UI where the user can submit a particular data for eg. Name of the User.
2. The user's detail is then stored in the in-memory database.
3. The top 5 most recent added Users can be checked by clicking the Users (In Memory) icon.
4. Finally, another REST API is used which clears all the data by clicking on Clear button.


### Technologies Used: 
Flask, RabbitMQ/Redis, SQLAlchemy 


## LICENSE
[MIT LICENSE](LICENSE.md)
