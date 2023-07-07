# FILE RETRIEVAL SYSTEM

CSCD 604: DISTRIBUTED SYSTEM

COURSE WORK 1

## Group 8 Contributors

| Student                 | ID Number                 |
| :---------------------- | :------------------------ |
| TAMATEY, ABRAHAM        | 110*****                  |
| PEASAH-DARKWAH, EMMANUEL| 110*****                  |
| A*****, G*****          | 110*****                  |
| JOHNSON, MICHAEL KWAME  | 110*****                  |
| BARNES, OBED            | 110*****                  |
| KUDROHA, GIDEON KWAME   | 110*****                  |
| TAMEKLOE, PASCAL A.     | 110*****                  |

## Getting Started

Clone repository to your local and navigate into the folder

```bash
git clone https://github.com/horlali/file-retrieval-system
cd file-retrieval-system/
```

Create  and fill out the environment variable files

```bash
cp .env.example .env
```

## Dev Toolchain

- [python ^3.11](https://www.python.org/) main programming language
- [poetry](https://python-poetry.org/) for dependency management
- [pytest](https://docs.pytest.org/en/stable/) for testing
- [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) for test coverage
- [black](https://github.com/psf/black) for code styling
- [isort](https://pycqa.github.io/isort/) for import sorting styling
- [flake8](https://flake8.pycqa.org/en/latest/) for linting

## Setup Local Environment

It is preferable to create and activate a virtual environment before installing the dependencies. You can read more about python virtual environments and how to create and activate it [here](https://realpython.com/python-virtual-environments-a-primer/)

Install the required dependencies

```bash
pip install -r requirements.txt
poetry install
```

## Make Scripts Executable

```bash
chmod +x scripts/*
```

## Running Servers

In the root of the repository `:~/file-retrieval-system` run the scripts below

```bash
./scripts/run-server.sh
```

whiles the server is running open another terminal and run the client script

```bash
./scripts/run-client.sh
```

## Encryption Standards Used

The AES amd PKCS1_OAEP encryption standards were used in this project

AES and PKCS1_OAEP are two different cryptographic algorithms that are available in the pycryptodome library.

AES (Advanced Encryption Standard) is a symmetric encryption algorithm that uses a 128-bit, 192-bit, or 256-bit key to encrypt data. It is a very secure algorithm that is widely used in a variety of applications, including data encryption, file encryption, and network security.

PKCS1_OAEP (Public-Key Cryptography Standards #1 Object-Oriented Encryption with Appendix) is an asymmetric encryption algorithm that uses a public key and a private key to encrypt and decrypt data. It is a secure algorithm that is often used to encrypt sensitive data, such as passwords and credit card numbers.

The pycryptodome library provides classes and functions for using both AES and PKCS1_OAEP. For example, the AES.new() class can be used to create an AES cipher object, and the PKCS1_OAEP.new() class can be used to create a PKCS1_OAEP cipher object. These cipher objects can then be used to encrypt and decrypt data.

## Sample Request and Application Docs

Once the application is up and running, visit <http://127.0.0.1:8501/> or <http://localhost:8501> or in your browser

You should see a Streamlit Page like this

![Alt text](files/screenshots/home.png)

## Changes required for the implementation above to work on a physical network

For the changes to work on a physical we need to we need to change the environment variable file to match requirements for the server

```bash
OBJECT_ID = "the desired object id"
HOST = "the hostname of the server"
PORT = "the port you want the app to run on"
```
