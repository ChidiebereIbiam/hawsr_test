# Hawsr Test By Chidiebere
An API using Django REST Framework (DRF) for Admins to managing users, workers, buildings, offices and assign users to offices

## Primary Modules

1. [django](https://www.djangoproject.com/)
1. [django rest framework](http://www.django-rest-framework.org/)

## Prerequisites

1. Python

## Installation Guide

```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Using Docker
```bash
docker-compose up -d --build
```


### User Endpoints
##### 1. Retrieve All Users 

**Endpoint:** `GET /user/`

**Description:** Retrieve a list of all users.


**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/user/' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "All Users",
  "response": [
    {
      "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
      "email": "Chidiebere4@gmail.com",
      "phone": "12839",
      "first_name": "Chidiebere",
      "last_name": "Ibiam",
      "role": 1
    }
  ]
}
```
##### 2. Retrieve User Details

**Endpoint:** `GET /user/?user_id=<user_id>`

**Description:** Retrieve details for a specific user.

**Parameters:**
- `user_id` (required): User ID of the user to retrieve

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/user/?user_id=981bd4ee-f333-4013-a2ac-4626ba7318a4' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "User Details for Chidiebere4@gmail.com",
  "response": {
    "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
    "email": "Chidiebere4@gmail.com",
    "phone": "12839",
    "first_name": "Chidiebere",
    "last_name": "Ibiam",
    "role": 1,
    "created": "2024-02-27T20:31:52.643054Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 3. Create a New User

**Endpoint:** `POST /user/`

**Description:** Create a new User.

**Parameters:**
- `email` (required): Email of the user
- `phone` (required): Phone number of the user
- `first_name` (required): User's first name
- `last_name` (required): User's last_name
- `role` (required): Role of the User: Enter 1 for for Admin, 2 for User and 3 for worker
- `password` (required): Password of the user

**Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/user/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "email": "test@hawsr.com",
  "phone": "+91904895893",
  "first_name": "Chidiebere",
  "last_name": "Ibiam",
  "role": 3,
  "password": "testPassword89@"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "User created successfully",
  "response": {
    "id": "00acf46f-e916-4180-b448-e3ec3e5d59df",
    "email": "test@hawsr.com",
    "phone": "+91904895893",
    "first_name": "Chidiebere",
    "last_name": "Ibiam",
    "role": 3
  }
}
```
##### 4. Update a User

**Endpoint:** `PUT /user/`

**Description:** Update details for a specific user.

**Parameters:**
- `user_id` (required): ID of the user
- `email` (optional): Email of the user
- `phone` (optional): Phone number of the user
- `first_name` (optional): User's first name
- `last_name` (optional): User's last_name
- `role` (optional): Role of the User: Enter 1 for for Admin, 2 for User and 3 for worker


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/user/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "user_id": "00acf46f-e916-4180-b448-e3ec3e5d59df",
  "email": "test@hawsr.com",
  "phone": "+91904895893",
  "first_name": "Chidi ",
  "last_name": "Ibiam",
  "role": 3,
  "password": "testPassword89@"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "User Updated successfully",
  "response": {
    "id": "00acf46f-e916-4180-b448-e3ec3e5d59df",
    "email": "test@hawsr.com",
    "phone": "+91904895893",
    "first_name": "Chidi",
    "last_name": "Ibiam",
    "role": 3
  }
}
```

##### 5. Delete a User

**Endpoint:** `DELETE /user/`

**Description:** Delete a specific user.

**Parameters:**
- `user_id` (required): ID of the user to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/user/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "user_id": "00acf46f-e916-4180-b448-e3ec3e5d59df"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "User Deleted successfully"
}
```

### Worker Endpoints
#### 1. Create a New Worker

**Endpoint:** `POST /worker/`

**Description:** Create a new worker.

**Parameters:**
- `user` (required): ID of the user
- `worker_type` (required): Type of worker, Options: 2 for IT, 5 for  Worker, 6 for Cleaner and 7 for Other
- `is_busy` (required): Boolean for whether a worker is busy or not

**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/worker/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "user": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
    "worker_type": 2,
    "is_busy": false
    }
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Worker created successfully",
  "response": [
    {
      "id": "e46f6060-536d-4c0e-8922-862e3fed12a7",
      "user": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
      "user_details": {
        "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
        "email": "Chidiebere4@gmail.com",
        "phone": "12839",
        "first_name": "Chidiebere",
        "last_name": "Ibiam",
        "role": 1
      },
      "worker_type": 2,
      "is_busy": false
    }
  ]
}
```

##### 2. Retrieve All Workers

**Endpoint:** `GET /worker/`

**Description:** Retrieve a list of all workers.



**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/worker/' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "All Workers",
  "response": [
    {
      "id": "e46f6060-536d-4c0e-8922-862e3fed12a7",
      "user": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
      "user_details": {
        "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
        "email": "Chidiebere4@gmail.com",
        "phone": "12839",
        "first_name": "Chidiebere",
        "last_name": "Ibiam",
        "role": 1
      },
      "worker_type": 2,
      "is_busy": false
    }
  ]
}
```
##### 3. Retrieve Worker Details

**Endpoint:** `GET /worker/?id=<worker_id>`

**Description:** Retrieve details for a specific worker.

**Parameters:**
- `id` (required): ID of the worker to retrieve

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/worker/?id=e46f6060-536d-4c0e-8922-862e3fed12a7' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "Worker Details for Chidiebere Ibiam",
  "response": {
    "id": "e46f6060-536d-4c0e-8922-862e3fed12a7",
    "user": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
    "user_details": {
      "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
      "email": "Chidiebere4@gmail.com",
      "phone": "12839",
      "first_name": "Chidiebere",
      "last_name": "Ibiam",
      "role": 1
    },
    "worker_type": 2,
    "is_busy": false,
    "created": "2024-02-28T07:17:56.237762Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 4. Update a Worker

**Endpoint:** `PUT /worker/`

**Description:** Update details for a specific worker.

**Parameters:**
- `id` (required): ID of the worker
- `user` (optional): ID of the user
- `worker_type` (optional): Type of worker, Options: 2 for IT, 5 for  Worker, 6 for Cleaner and 7 for Other
- `is_busy` (optional): Boolean for whether a worker is busy or not


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/worker/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "id": "e46f6060-536d-4c0e-8922-862e3fed12a7",
    "is_busy": true
    }
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Worker Updated successfully",
 "response": [
    {
      "id": "e46f6060-536d-4c0e-8922-862e3fed12a7",
      "user": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
      "user_details": {
        "id": "981bd4ee-f333-4013-a2ac-4626ba7318a4",
        "email": "Chidiebere4@gmail.com",
        "phone": "12839",
        "first_name": "Chidiebere",
        "last_name": "Ibiam",
        "role": 1
      },
      "worker_type": 2,
      "is_busy": true
    }
  ]
}
```

##### 5. Delete a Worker

**Endpoint:** `DELETE /worker/`

**Description:** Delete a specific worker.

**Parameters:**
- `id` (required): ID of the worker to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/worker/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "id": "e46f6060-536d-4c0e-8922-862e3fed12a7"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Worker Deleted successfully"
}
```

### Company Endpoints
#### 1. Create a New Company

**Endpoint:** `POST /company/`

**Description:** Create a new company.

**Parameters:**
- `name` (required): Company Name
- `phone` (required): Phone number of the company

**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/company/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "name": "Facebook",
    "phone": "0905655206",
    }
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Company created successfully",
  "response": {
    "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "name": "Facebook",
    "phone": "0905655206",
    "created": "2024-02-28T08:10:36.991513Z",
    "is_active": false,
    "is_deleted": false
  }
}
```

##### 2. Retrieve All Companies

**Endpoint:** `GET /company/`

**Description:** Retrieve a list of all companies.



**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/company/' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "All Companies",
  "response": [
    {
      "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
      "name": "Facebook",
      "phone": "0905655206"
    },
    {
      "id": "da504e3b-bf61-4476-b2b8-6330b241954d",
      "name": "Google",
      "phone": "843989580"
    }
  ]
}
```
##### 3. Retrieve Company Details

**Endpoint:** `GET /company/?id=<company_id>`

**Description:** Retrieve details for a specific company.

**Parameters:**
- `id` (required): ID of the company to retrieve

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/company/?id=9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf' \
  --header 'Accept: */*' \
```

**Response:**
```json
{
  "success": true,
  "message": "Worker Details for Facebook",
  "response": {
    "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "name": "Facebook",
    "phone": "0905655206",
    "created": "2024-02-28T08:10:36.991513Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 4. Update a Company

**Endpoint:** `PUT /company/`

**Description:** Update details for a specific company.

**Parameters:**
- `id` (required): ID of the company
- `name` (optional): Company Name
- `phone` (optional): Phone number of the company


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/company/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "phone": "090482984012"
    }
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Company Updated successfully",
 "response": [
  {
    "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "name": "Facebook",
    "phone": "090482984012",
    "created": "2024-02-28T08:10:36.991513Z",
    "is_active": false,
    "is_deleted": false
  }
  ]
}
```

##### 5. Delete a Company

**Endpoint:** `DELETE /company/`

**Description:** Delete a specific company.

**Parameters:**
- `id` (required): ID of the company to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/company/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Company Deleted successfully"
}
```

### Building Endpoints
#### 1. Create a New Building

**Endpoint:** `POST /building/`

**Description:** Create a new building.

**Parameters:**
- `company` (required): ID of the company
- `name` (required): Name of the Building
- `floor_count` (required): Number of Floors in the building
**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/building/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "company": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "name": "Annex",
    "floor_count": 10
    }
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Building created successfully",
  "response": {
      "id": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "company": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
      "name": "Annex",
      "floor_count": 10
    }
}
```

##### 2. Retrieve All Buildings

**Endpoint:** `GET /building/`

**Description:** Retrieve a list of all buildings.



**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/building/' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "All Buildings",
  "response": [
    {
      "id": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "company": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
      "name": "Annex",
      "floor_count": 10
    },
    {
      "id": "33ab2866-fd3f-42fa-8cbe-bd811fdb9b95",
      "company": "da504e3b-bf61-4476-b2b8-6330b241954d",
      "name": "Complex",
      "floor_count": 10
    },
    {
      "id": "7a64ac87-0e59-4a7c-9fa4-0520748f9169",
      "company": "da504e3b-bf61-4476-b2b8-6330b241954d",
      "name": "Abuja",
      "floor_count": 20
    }
  ]
}
```
##### 3. Retrieve Building Details

**Endpoint:** `GET /building/?id=<building_id>`

**Description:** Retrieve details for a specific building.

**Parameters:**
- `id` (required): ID of the building to retrieve

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/building/?id=7c98efff-8cb2-497d-946c-20faa94aca62' \
  --header 'Accept: */*' \
```

**Response:**
```json
{
  "success": true,
  "message": "Building Details for Annex",
  "response": {
    "id": "7c98efff-8cb2-497d-946c-20faa94aca62",
    "company": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "name": "Annex",
    "floor_count": 10,
    "created": "2024-02-28T09:48:32.530205Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 4. Update a Building

**Endpoint:** `PUT /building/`

**Description:** Update details for a specific building.

**Parameters:**
- `id` (required): ID of the building
- `company` (optional): ID of the company
- `name` (optional): Name of the Building
- `floor_count` (optional): Number of Floors in the building


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/building/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "id": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
    "floor_count":5
    }
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Building Updated successfully",
 "response": [
 {
      "id": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "company": "9a2e13a3-dbc9-42cb-8f16-18ee401bd5bf",
      "name": "Annex",
      "floor_count": 5
    }
  ]
}
```

##### 5. Delete a Building

**Endpoint:** `DELETE /building/`

**Description:** Delete a specific building.

**Parameters:**
- `id` (required): ID of the building to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/building/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "id": "7c98efff-8cb2-497d-946c-20faa94aca62"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Building Deleted successfully"
}
```

### Office Endpoints
#### 1. Create a New Office

**Endpoint:** `POST /office/`

**Description:** Create a new office.

**Parameters:**
- `building` (required): ID of the building
- `floor` (required): Office Floor
- `number` (required): Office Number
**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    }
}'
```

**Example Response:**
```json
{
  "success": true,
  "message": "Office created successfully",
  "response": {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    }
}
```

##### 2. Retrieve All Offices

**Endpoint:** `GET /office/`

**Description:** Retrieve a list of all offices.



**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/office/' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "All Offices",
  "response": [
    {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    },
    {
      "id": "5e5cbd04-8d05-46da-8b03-659d040e75fa",
      "building": "33ab2866-fd3f-42fa-8cbe-bd811fdb9b95",
      "floor": 10,
      "number": 20
    },
    {
      "id": "81ce592f-a9c5-40c3-9751-a736b6837041",
      "building": "33ab2866-fd3f-42fa-8cbe-bd811fdb9b95",
      "floor": 10,
      "number": 20
    }
  ]
}
```
##### 3. Retrieve Office Details

**Endpoint:** `GET /office/?id=<office_id>`

**Description:** Retrieve details for a specific office.

**Parameters:**
- `id` (required): ID of the office to retrieve

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/office/?id=7e50c80c-732c-43ab-83e2-1447b4724397' \
  --header 'Accept: */*' \
```

**Response:**
```json
{
  "success": true,
  "message": "Office Details for 7e50c80c-732c-43ab-83e2-1447b4724397",
  "response": {
    "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
    "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
    "floor": 10,
    "number": 20,
    "created": "2024-02-29T19:47:28.839374Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 4. Update a Office

**Endpoint:** `PUT /office/`

**Description:** Update details for a specific office.

**Parameters:**
- `id` (required): ID of the office
- `building` (required): ID of the building
- `floor` (required): Office Floor
- `number` (required): Office Number


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
    "number":1
    }
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Office Updated successfully",
 "response": [
  {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 5,
    }
  ]
}
```

##### 5. Delete a Office

**Endpoint:** `DELETE /office/`

**Description:** Delete a specific office.

**Parameters:**
- `id` (required): ID of the office to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "id": "7e50c80c-732c-43ab-83e2-1447b4724397"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "Office Deleted successfully"
}
```

### User Office Endpoints
#### 1. Assign an Office to a user

**Endpoint:** `POST /user-office/`

**Description:** Assign a new office to a user.

**Parameters:**
- `office` (required): ID of the office
- `user` (required): ID of the user

**Example Request:**
```bash
curl  -X POST \
  'http://127.0.0.1:8000/user-office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d"
    }'
```

**Example Response:**
```json
{
  "success": true,
  "message": "User Office created successfully",
  "response": {
    "id": "8de24091-e288-4821-b221-6edfd1cafece",
    "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
    "office_details": {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    },
    "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
    "user_details": {
      "id": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
      "email": "489f4@gmail.com",
      "phone": "09056557206",
      "first_name": "Ngozi",
      "last_name": "Okorie",
      "role": 2
    }
  }
}
```

##### 2. Retrieve All User's Offices

**Endpoint:** `GET /user-office/`

**Description:** Retrieve a list of all user's offices.



**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/user-office/' \
  --header 'Accept: */*' \
```

**Response:**
```json
{
  "success": true,
  "message": "All User offices",
  "response": [
    {
      "id": "be33a480-f40b-47d4-96c0-0315ac18d6fc",
      "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "office_details": {
        "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
        "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
        "floor": 10,
        "number": 20
      },
      "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
      "user_details": {
        "id": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
        "email": "489f4@gmail.com",
        "phone": "09056557206",
        "first_name": "Ngozi",
        "last_name": "Okorie",
        "role": 2
      }
    },
    {
      "id": "8de24091-e288-4821-b221-6edfd1cafece",
      "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "office_details": {
        "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
        "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
        "floor": 10,
        "number": 20
      },
      "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
      "user_details": {
        "id": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
        "email": "489f4@gmail.com",
        "phone": "09056557206",
        "first_name": "Ngozi",
        "last_name": "Okorie",
        "role": 2
      }
    }
  ]
}
```
##### 3. Retrieve User Office Details

**Endpoint:** `GET /useroffice/?id=<user-office_id>`

**Description:** Retrieve details for a specific user  office record by its id. The response will contain the user's office information if it exists otherwise

**Parameters:**
- `id` (required): ID of the user-office record to retrieve.

**Request:**
```bash
curl  -X GET \
  'http://127.0.0.1:8000/user-office/?id=8de24091-e288-4821-b221-6edfd1cafece' \
  --header 'Accept: */*' 
```

**Response:**
```json
{
  "success": true,
  "message": "User_office Details for 8de24091-e288-4821-b221-6edfd1cafece",
  "response": {
    "id": "8de24091-e288-4821-b221-6edfd1cafece",
    "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
    "office_details": {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    },
    "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
    "user_details": {
      "id": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
      "email": "489f4@gmail.com",
      "phone": "09056557206",
      "first_name": "Ngozi",
      "last_name": "Okorie",
      "role": 2
    },
    "created": "2024-03-01T09:00:49.872614Z",
    "is_active": false,
    "is_deleted": false
  }
}
```
##### 4. Update a User Office

**Endpoint:** `PUT /user-office/`

**Description:** Update details for a specific office.

**Parameters:**
- `id` (required): ID of the office
- `office` (optional): ID of the office
- `user` (optional): ID of the user


**Request:**
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "id": "8de24091-e288-4821-b221-6edfd1cafece",
    "office":"7e50c80c-732c-43ab-83e2-1447b4724397"
    }
}'
```

**Response:**
```json
{
  "success": true,
  "message": "User-office Updated successfully",
 "response": [
  {
    "id": "8de24091-e288-4821-b221-6edfd1cafece",
    "office": "7e50c80c-732c-43ab-83e2-1447b4724397",
    "office_details": {
      "id": "7e50c80c-732c-43ab-83e2-1447b4724397",
      "building": "7c98efff-8cb2-497d-946c-20faa94aca62",
      "floor": 10,
      "number": 20
    },
    "user": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
    "user_details": {
      "id": "5b74b708-9885-4fd3-ac0b-7f2a926d530d",
      "email": "489f4@gmail.com",
      "phone": "09056557206",
      "first_name": "Ngozi",
      "last_name": "Okorie",
      "role": 2
    }
  }
  ]
}
```

##### 5. Delete a User Office

**Endpoint:** `DELETE /user-office/`

**Description:** Delete a specific user office.

**Parameters:**
- `id` (required): ID of the user-office to delete

**Request:**
```bash
curl  -X DELETE \
  'http://127.0.0.1:8000/user-office/' \
  --header 'Accept: */*' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "id": "8de24091-e288-4821-b221-6edfd1cafece"
}'
```

**Response:**
```json
{
  "success": true,
  "message": "User-office Deleted successfully"
}
```




#### Swagger and Redoc Documentation

- Swagger UI: `http://127.0.0.1:8000/swagger/`
- Redoc: `http://127.0.0.1:8000/redoc/`


