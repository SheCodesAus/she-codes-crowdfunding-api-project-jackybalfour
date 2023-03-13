# {{ Aimee Travel }}

{{ Aimee Travel helps people who needs to travel overseas due to an emergency and can’t afford it. 
People creates a crowdfunding to collect the needed amount of “travel points” to go to the desired destination.
The target audience for this project is people from 21 to 60 years old experiencing financial stress, they live overseas or have relatives living overseas, and due to an emergency need to travel, and people willing to help others to get to the desired destination.
Example:
Anna lives in Japan, her sister had an accident in Italy. 
She is collecting travel points to go to Italy and visit her sister who is in hospital.
}}

## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.** What I havent done is because I really struggled. Mentor said i meet min req

- Project
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Limit who can create 
  - [X] Limit who can retrieve - everyone can see the projects
  - [] Limit who can update
  - [] Limit who can delete
- Pledge
  - [X] Limit who can create
  - [X] Limit who can retrieve
  - [ ] Limit who can update
  - [ ] Limit who can delete
- Pledge
  - [X] Limit who can retrieve
  - [X] Limit who can update
  - [ ] Limit who can delete

### Implement relevant status codes

- [x] Get returns 200
- [x] Create returns 201
- [x] Not found returns 404

### Handle failed requests gracefully 

- [ ] 404 response returns JSON rather than text

### Use token authentication

- [X] impliment /api-token-auth/

## Additional features

- [ ] {Like a project}

{{ Every user can see how many people like that project and if they did }}

- [ ] {Comments}

{{ You can leave a comment when you add a pledge }}

- [ ] {Win a badge????search project??}

{{ description of feature 3 }}

### External libraries used

- [ ] django-filter


## Part A Submission

- [ ] A link to the deployed project.
- [ ] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [ ] A screenshot of Insomnia, demonstrating a token being returned.
- [ ] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '{
        "username": "oliver",
        "email": "oliver@oliver.com",
        "password": "oli"
}'


2. Sign in User

curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
  "username": "admin",
  "password": "ADMIN"
}'

3. Create Project

curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token 589cb900f4f7ee772e54f632d70d1ade00512ec6' \
  --header 'Content-Type: application/json' \
  --data '{
        "id": 1,
        "title": "Donate a dog",
        "description": "Please help, we need a dog for she codes plus, our class lacks barks.",
        "goal": 1,
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
        "is_open": true,
        "date_created": "2023-01-17T12:06:15.959003Z",
        "owner": 1
}'