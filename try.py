#dev-remote
	#python3 manage.py runserver 0.0.0.0:8000 --settings=config.settings.dev



# Parent registration json
{
    "user": {
        "username": "ginu",
        "first_name": "ginu",
        "last_name": "george",
        "email": "alice.smith@example.com",
        "password": "password123"
    },
    "address": "456 Elm Street, Newtown",
    "phone_number": "987654321",
    "gender": "F",
    "children": [
        {
            "first_name": "edhu",
            "last_name": "jestin",
            "age": 10,
            "class_id": 3,  
            "gender": "M",
            "username": "edhu",
            "password": "secure_password"
        },
        {
            "first_name": "Emami",
            "last_name": "jestin",
            "age": 7,
            "class_id": 2,  
            "gender": "F",
            "username": "emami",
            "password": "secure_password"
        }
    ]
}




{
        
    "username": "li_smith",
    "password": "secure_password"
}


# Teacher Registration

{
    "user": {
        "username": "samjohn",
        "first_name": "Sam",
        "last_name": "John",
        "password": "password123"
    },
    "gender": "M",
    "class_id": 1  
}


{
    "parent_id": 21,
    "student_id": 13,
    "leave_type": "SICK",
    "leave_description": "Student is sick with a cold and needs rest.",
    "start_date": "2024-09-24",
    "end_date": "2024-09-26"
}


#pip install djangorestframework-simplejwt


{
    "class_name": "First Standard",
    "academic_year": "2023-2024",
    "grade": 1,
    "timetable": [
        {
            "day": "Monday",
            "schedule": [
                {
                    "subject": "Mathematics",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "molly"
                },
                {
                    "subject": "Physics",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "molly"
                }
            ]
        },
        {
            "day": "Tuesday",
            "schedule": [
                {
                    "subject": "History",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "Ms. Sarah Lee"
                },
                {
                    "subject": "English",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "Mr. Mark Thompson"
                }
            ]
        },
        {
            "day": "Wednesday",
            "schedule": [
                {
                    "subject": "Chemistry",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "Ms. Alice Brown"
                },
                {
                    "subject": "Physical Education",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "Mr. David King"
                }
            ]
        }
       
    ]
}


{
    "class_name": "Second Standard",
    "academic_year": "2001-2002",
    "grade": 2,
    "timetable": [
        {
            "day": "Monday",
            "schedule": [
                {
                    "subject": "Mathematics",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "molly"
                },
                {
                    "subject": "Physics",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "molly"
                }
            ]
        },
        {
            "day": "Tuesday",
            "schedule": [
                {
                    "subject": "History",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "Ms. Sarah Lee"
                },
                {
                    "subject": "English",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "Mr. Mark Thompson"
                }
            ]
        },
        {
            "day": "Wednesday",
            "schedule": [
                {
                    "subject": "Chemistry",
                    "start_time": "09:00",
                    "end_time": "10:00",
                    "teacher": "Ms. Alice Brown"
                },
                {
                    "subject": "Physics",
                    "start_time": "10:15",
                    "end_time": "11:15",
                    "teacher": "Mr. David King"
                }
            ]
        }
       
    ]
}
