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


### Technologies Used: 
Flask, RabbitMQ/Redis, SQLAlchemy 


## LICENSE
[MIT LICENSE](LICENSE.md)
