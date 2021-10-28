# RSA REST API

RSA cipher implementation along with REST API server and ability to encrypt/decrypt through endpoints.

### Setup
* Create a Python virtualenv within a working directory 

`python -m virtualenv venv`

* Activate virtual environment

`.\venv\Scripts\activate` on Windows  
`source venv/bin/activate` on Linux

* Install proper reqs from requirements.txt in venv

`pip install -r requirements.txt`

* Launch the server 

`uvicorn app.main:app --reload`

### Encryption

* Access FastAPI's built-in swagger (`localhost:8000/docs`)

* Enter message to encrypt into the `encrypt` endpoint

Returned list is the RSA super-safe encrypted top-secret message!

### Decrypt

* Copy an entire list of integers from response (along with the braces if you will) and paste it directly into `decrypt` endpoint message window

Careful! As the session changes so do the keys - top-secred message could stay secret forever!

### Running tests
Make sure you're into `/app` folder then execute:
`pytest -v`

### Configuration

In order to change the time cipher takes to encode/decode - change
the random sample prime range in RSA.py file. The following changes along
with the security cipher offers.
