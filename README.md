# Event Management System

## Project Details

### Overview
The **Event Management System** is a Django-based application designed to manage events through a role-based access control system. The system allows different types of users—Admin, Principal, HOD, and Students—to interact with event data according to their roles and permissions.

### Key Features
- **Event Management**: Admins can create, edit, and manage event details.
- **Role-Based Access**:
  - **Admin**: Can post, edit, and manage events. Has the highest level of access.
  - **HOD**: Can review, edit, and accept or cancel events posted by the Admin.
  - **Principal**: Can review and approve events that have been accepted by the HOD.
  - **Students**: Can register for events that have been approved by the Principal.
- **Event Details**:
  - Event Name
  - Description
  - Date
  - Venue
  - Number of People Expected
  - Guest Names
  - Location
  - Estimated Budget
  - Time
  - Poster (Uploadable image)
- **User Dashboard**:
  - **Admin Dashboard**: Access to all event management functions.
  - **HOD Dashboard**: Access to review and manage events.
  - **Principal Dashboard**: Access to approve events.
  - **Student Dashboard**: Access to register for approved events.

### Technologies Used
- **Framework**: Django
- **API Framework**: Django REST Framework
- **Database**: PostgreSQL (or any other Django-supported database)
- **Authentication**: Django's built-in authentication system with role-based access control

### Installation and Setup
1. **Clone the repository**:
   
   ```git clone <repository-url>```


<hr>

**Navigate to the project directory:**

```cd event_management```

**Set up the virtual environment:**

```python -m venv venv```

**Activate the virtual environment:**

*On Windows:*

```venv\Scripts\activate```

*On macOS/Linux:*

``source venv/bin/activate``

**Install dependencies:**

```pip install -r requirements.txt```

**Apply migrations:**

```python manage.py migrate```

**Create a superuser:**

```python manage.py createsuperuser```

**Run the server:**

```python manage.py runserver ```


<hr>

# **Project Steps Completed So Far**
*1. Set up Django project and app*
- Created a Django project named event_management.
- Created an app called events for managing event-related functionality.


*2. Installed Django REST Framework*
- Installed djangorestframework for building the API.

*3. Created User Groups*
- Defined user groups for Admin, Principal, HOD, and Students using Django’s built-in Group model.

*4. Defined Event Model and Permissions*
- Created the Event model in events/models.py.
- Defined custom permissions for viewing, editing, and managing events for each role.

*5. Set Up REST Framework Configuration*
- Configured rest_framework in settings.py to handle API authentication and permissions.

