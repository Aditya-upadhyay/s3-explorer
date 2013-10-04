<h2> S3 Explorer </h2>
<p>This is a simple app which ask you your AWS credentials and lets you browse, search, sorta and download keys in any bucket.</p>
</br>
</br>
<h3>Installation Instructions.</h3>
* Install Django-trunk version from <a href="https://docs.djangoproject.com/en/dev/topics/install/"> here</a>. It should work fine with latest Django stable version also.
* Clone this repository,Change directory to s3-explorer and run `sudo pip install -r Requirement.txt` 
* Sync db by running `django-admin.py syncdb`.
* Run server `python manage.py runserver 8008`
* Open http://localhost:8008 in your browser.
