# Sales Management API – List Case Study

## 📌 Project Overview

The **Sales Management API** is a REST API developed using **Python and FastAPI**. This project demonstrates how to perform CRUD (Create, Read, Update, Delete) operations on sales records using Python lists.

The API allows users to add new sales, retrieve all sales records, search for a sale using its ID and name, update existing sales, and delete sales.

## 🛠️ Technologies Used

* Python
* FastAPI
* Uvicorn
* Swagger UI
* Python Lists

## 📂 Project Structure

```text
List_case_study/
├── main.py
├── database.py
└── README.md
```

## ✨ Features

* Retrieve all sales records
* Add a new sale
* Search for a sale using ID and name
* Update an existing sale
* Delete a sale using its ID
* Store and manage sales records using Python lists
* Test API endpoints through interactive Swagger UI

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Narendra-batthala/Case_studies.git
```

### 2. Navigate to the Project Folder

```bash
cd Case_studies/List_case_study
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

### 5. Open Swagger UI

After starting the server, open the following URL in your browser:

http://127.0.0.1:8000/docs

You can use Swagger UI to interactively test the available API endpoints.

## 🔗 API Endpoints

| HTTP Method | Endpoint             | Description                         |
| ----------- | -------------------- | ----------------------------------- |
| GET         | `/`                  | Display the API welcome message     |
| GET         | `/sales`             | Retrieve all sales records          |
| POST        | `/sales`             | Add a new sale                      |
| GET         | `/sales/{ID}/{name}` | Search for a sale using ID and name |
| PUT         | `/sales/{sale_id}`   | Update an existing sale             |
| DELETE      | `/sales/{sale_id}`   | Delete a sale using its ID          |

## 📋 Sales Record Fields

Each sales record contains the following fields:

| Field   | Description                     |
| ------- | ------------------------------- |
| ID      | Identifier for the sale         |
| Name    | Name associated with the sale   |
| Product | Product sold                    |
| Units   | Number of units sold            |
| Price   | Price of the product            |
| Region  | Region associated with the sale |

## 🧪 API Testing

The API can be tested using the interactive Swagger documentation at `/docs`.

You can use the available endpoints to:

* Add new sales records
* View all sales records
* Search for a specific sale
* Update sale details
* Delete a sale

## 💾 Data Storage

Sales records are managed using Python lists in the `database.py` module.

**Note:** This project uses in-memory storage. Sales data is not permanently stored and may be lost when the application restarts.

## 🎯 Learning Outcomes

* Understanding REST API fundamentals
* Creating API endpoints using FastAPI
* Working with Python lists and nested lists
* Performing CRUD operations
* Using path parameters in API endpoints
* Organizing a Python project into separate modules
* Testing APIs using Swagger UI

## 👨‍💻 Author

**Narendra Batthala**

GitHub: [Narendra-batthala](https://github.com/Narendra-batthala)

---

⭐ This project was developed as a Python case study to practice list operations and REST API development using FastAPI.
