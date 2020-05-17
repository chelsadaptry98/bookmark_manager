# bookmark_manager
Create bookmarks for customers with geographical information and filter the bookmarks using APIs

Download the repository inside an empty folder
Install Django 2.2.12 with python 3.5+
Give appropriate GOOGLE_API_KEY in bm/settings.py
Once in the proper directory run command 'python manage.py runserver' 
Open localhost:/api/create for creating bookmark with existing users and bookmarks
Open localhost:/api/create/:cust_name for creating bookmark with existing users and new bookmarks
Open localhost:/api/browse for filtering the bookmarks via various parameters like customer_id , title_contains etc

