# Nomio Interview Exercise

At Nomio, we turn documents into data. 

Usually our customers start by uploading all of their existing documents to our system; 
however, customers often have duplicates of files that they don't know about, 
or they will upload files that have already been uploaded to our system. 
We'd like to help them out by detecting and dealing with these duplicates.

## Getting Started

You will need to have at least Python 3.6 installed on your machine: if you don't, you can install the latest version 
[from these instructions](https://wiki.python.org/moin/BeginnersGuide/Download).

Once you have Python installed, you should be able to get set up with the following commands:


After these commands, you should be able to see a page when you visit http://localhost:8000/ and be able to log in.

## What's already done

We've created a basic Django project (`nomio`) with two applications:

- `nomio.landing` is for our basic Landing Page, which simply handles user login at `/`. 
  (You don't need to modify this app as part of this task.)
- `nomio.documents` is for our document listing and uploading application at `/documents`. 
  It currently has basic functionality to upload, list, download and delete documents for a given user. 

## What we'd like you to do

1. Review the existing code to ensure it is in line with our standards. 
   *(See the next section for details.)*

   Please add your report as a new file `review.md`, alongside this README.
   If you spot any code that should change, please make those changes.
   
2. Add functionality to detect and handle duplicate files in a user-friendly way.

## Our standards

At Nomio, we design and build **[minimalist](https://en.wikipedia.org/wiki/Minimalism#Minimalist_design_and_architecture)** tools for our customers.

Our code is **easy to understand**, **well-tested** and **able to cope when things go wrong** (whether caused by errors or malicious users).

We give feedback that is **positive**, **constructive** and **clear**.

## What we're looking for

When we get your solution, we will:

- run the instructions in _Getting Started_ to start the server, and assess your solution is complete
- run the tests to ensure they pass
- assess your code review against our review standards
- assess your new code against our coding standards

## Hints & Tips

- To run the tests, use `python manage.py test`.
- You are free to use as many (or as few!) packages as you like, but make sure they're 
  [specified](https://pip.pypa.io/en/stable/user_guide/#requirements-files) in `requirements.txt` 
  so we install them when setting up your solution.
- You can create more users from the [Django Admin Site](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
  at http://localhost:8000/admin.
