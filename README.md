# elmadrasa.com.test

An educational platform sample built with Django REST Framework, allowing teachers to create classes and students to enroll in them. The system integrates with Stripe for secure payments.

## Features

-  Add & manage teachers  
-  Register & manage students  
- Create and list classes  
- Charge students for class registration via Stripe  
-  Automatically transfer payments to company by stripe   

## Tech Stack

- Backend: Django, Django REST Framework  
- Database: MySQL  
- Payments: Stripe API  

## Setup Instructions

. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/elmadrasa.com.test.git
   cd elmadrasa.com.test
   ```
* Run  
   ```bash
   python manage.py runserver
   ```

## API Endpoints

| Method | Endpoint             | Description                     |
|--------|----------------------|---------------------------------|
| GET    | `/api/teachers/`     | List all teachers               |
| POST   | `/api/teachers/`     | Add a new teacher               |
| GET    | `/api/students/`     | List all students               |
| POST   | `/api/students/`     | Register a new student          |              |
| POST   | `/api/classes/`      | Add a new class                 |
| POST   | `/api/charge/`       | Charge student & transfer funds |


#### Add a Teacher
```json
{
  "name": "testEx",
  "email": "testn1@example.com"
}
```

####  Add a Student
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "stripe_customer_id": "cus_1RL...  will generate by api for first time"
}
```

####  Add a Class
```json
{
  "title": "Physics 101",
  "description": "Introductory course to physics.",
  "price": 50.00,
  "currency": "usd",
  "teacher_id": 1
}
```

####  Charge Student for Class
```json
{
  "class_id": 1,
  "student_id": 2,
  "payment_method_id": "pm_1RLhauRgky7oBmWajttlMG7I"
}
```
