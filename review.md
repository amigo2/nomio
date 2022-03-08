## Getting Started

Added Docker instead of virtual environment to the project, to be able to run Docker you need to
follow the next steps:

- Install Docker
- open a terminal and run
- docker-compose build
- docker-compose up
- open another terminal and run docker ps to find out the id of the application to make
  some changes.
- docker exec -it container_id python manage.py createsuperuser
- docker exec -it container_id python manage.py makemigrations
- docker exec -it container_id python manage.py migrate

After these commands, you should be able to see a page when you visit http://localhost:8000/ and be able to log in.

## Review

After reviewing all code it seems quite within the standards of Nomio

- Just added some functionality as mentioned in the what we'd like you to do section.
- The functionality I added is to not upload any duplicate files to the application.
- First thing I added a file called scripts.py where I create a function helper that would
  generate a sha1 file from the name of the file, this way the application would be able to
  check if the sha1 encoding exists in the application and it would not upload.
- As we want to stop duplicates the earliest as possible, I added a for loop in the save function
  to check for the files if the just create sha1 encode matches any already in the db, if so,
  delete the file and just upload the non-duplicates ones.
- Finally, the files that are not duplicated are saved into the db.
- A better form interface could be beneficial, but I just wanted to keep it simple.
- Some tests should be implemented for the new functionality.


