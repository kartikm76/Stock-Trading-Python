Connection Pool - https://overiq.com/mysql-connector-python-101/connection-pooling-using-connector-python/

NOTE: you may have python or python3 installed. Please change the instructions accordingly

1.  Install Virtal Env
    pip3 install virtualenv

2.  Setup Virtual Env
    virtualenv -p python3 my_env

3.  Activate Virtual Env
    Mac     - source my_env/bin/activate
    Windows - .\my_env\Scripts\activate.bat

4.  Install Libraries based on the list from requirements.txt
    pip3 install -r requirements.txt

5.  Optional steps to ensure installed libraries and requirements.txt are in sync
    pip3 list
    pip3 freeze > requirements.txt

6. You should see terminal prompt starting with "(my_env)"
7. Go to //Stock-Trading-Python/src/main
8. python3 main.py
9. It should display following output

    * Serving Flask app "main" (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 661-488-292

10. Go to browser and type: http://127.0.0.1:5000/ - it should open Swagger UI
11. Test an end point: http://127.0.0.1:5000/api/all-users
