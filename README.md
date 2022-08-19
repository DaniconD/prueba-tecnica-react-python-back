# prueba-tecnica-react-python-back
Prueba de formulario con React 18+ y Django 4.0.6, Backend

## How to run the backend

1. You will need to create a blank database in your root directory by the name of "communities_db". I provided you with the same database file I used to test the project in case you want to work with that, you will find it in the root directory as "communities_db.sql".
2. For running the project server: 
     - 2.1. Open a terminal in the project root directory and type "env\Scripts\activate" to create a virtual enviroment.
     - 2.2. Change the directory to the BACKEND folder "cd BACKEND".
     - 2.3. Run the server by typing "py manage.py runserver".
3. The project server will be running at http://127.0.0.1:8000/, these are some directories that maight interest you:
    - Admin view: http://127.0.0.1:8000/admin
        - if you need access -> user: dani, password: 1234 
        - or you could create a new super user with the command "py manage.py createsuperuser"
    - Database Content: http://127.0.0.1:8000/api/communities/
4. To quit the server use "Ctrl-C" on the therminal
5. To exit the virtual enviroment type "deactivate"
  
If you find some troubles by running the project, please email me. 
    
