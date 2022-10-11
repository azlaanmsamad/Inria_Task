# Inria Task

This Repository contains Web Development Task to be completed as a part of the Inria selection Procedure.


## Problem Statement

- Develop a web app to receive 3 different signal inputted by the user and store it in the Database for backup. 
- Retreive the last 5 datapoints from the backend and display them with timestamps.
- Expose a REST API with a one method _clear_ that cleans all the data in the memory.
- Dockerizer the different functionalities.

## Approach

### Technologies Used: 
Flask, RabbitMQ/Redis, SQLAlchemy 

### Workflow:
1. Create a Frontend UI where the user can submit a particular data for eg. Name of the User.
2. Trigger a REST API to pass this data to the Message Queue (MQ) using the POST method.
3. This MQ triggers a job which looks at the # of data points in the queue and displays the last five data points.
4. The user data is also stored in the Database.
5. Finally, another REST API is used which clears all the data in the MQ. 





## LICENSE
[MIT LICENSE](LICENSE.md)
