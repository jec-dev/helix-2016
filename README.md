How to run?
------------
* `git clone git@github.com:jec-dev/helix-2016.git`
* `cd helix-2016`
* `sudo pip install virtualenv`
     * Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already.
     * If you don't have pip installed, visit here to see steps to install virtualenv: [https://virtualenv.readthedocs.org/en/latest/installation.html](https://virtualenv.readthedocs.org/en/latest/installation.html)
* `virtualenv hel`
* `source hel/bin/activate`
* `pip install -r requirements.txt` (wait till the requirements are installed)
* `python manage.py syncdb`
     * It will prompt to create a new user type "yes" and add give a username, email and password. This will be one of the user which we can use to try our API.
* `python manage.py runserver` This will run the application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
