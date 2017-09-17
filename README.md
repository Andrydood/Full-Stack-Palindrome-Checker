## Introduction

This system is compromised of a front end written using React.js and a back end written using the Django and Django REST framework. Its use is to check if a given string is a palindrome using an API and convey this information to the user. If the string is a palindrome, it is then stored along with the rest of the confirmed palindromes, and the first 100 are shown.

## Usage

### Back End

The back end of the system is compromised of a REST API. The first operation that can be done on this is a POST request (at the address "domain"/palindromes/) in the form {text:string}, where "string" is the string of text to be evaluated. This returns TRUE if the string is a palindrome and FALSE if it is not. This excludes the consideration of capitalization, punctuation and whitespaces/spaces. If it is a palindrome, a "palindrome" object is formed containing the original string and its creation date. This is then added to the database.

The second operation is a GET operation (at the address "domain"/palindromes/) that returns the latest 100 palindromes stored in reverse chronological order.

The third is a GET operation (at the address "domain"/palindromes/"page-number") that returns the latest 100 palindromes stored, 10 palindromes at a time, depending on the accessed "page". This is done for later use in the front end pagination.

Finally, a DELETE operation is present (at the address "domain"/palindromes/) which removes all the saved palindromes.

Unit tests for this system can be found in backEnd/src/main/tests.py. These test that the palindrome model (object) can correctly be created, that the serialization and deserialization of the model works, and that all the API functions work as intended.

### Front End

The front end is firstly compromised of a text box to input a string. By then submitting this (using enter or pressing the button), the system will communicate with the API and will show the result of the evaluation below. The list of palindromes can be seen below this, 10 at a time. If the total number of palindromes exceeds 10, a second page is available and can be accessed through the arrows. Finally, the delete button deletes all the palindromes.

## Run Instructions

The dependencies of the back end are Python 3.6, Django, Django-REST and . The front end dependencies are node-js(npm), react-js and react bootstrap.

### Back End

Firstly, the virtual environment is activated with 
```cd backEnd/
source bin/activate```

### Front End
