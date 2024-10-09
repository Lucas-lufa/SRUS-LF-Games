# Por-Asst-Task-2-v1.5

## Scenario

You are employed as a junior software developer at a boutique software house called Softwares-R-Us in Perth.

You have been assigned to the Games team and will provide some of the code required for various games that the company builds and releases.

You will be updating the existing code from the previous task to store player passwords in a secure manner. You will be using hashing to accomplish this.

## Instructions

Your code must adhere to certain style guides, the most important being PEP-8 – Style Guide for Python Code. You should familiarise yourself with PEP-8 before continuing as SRU have adopted PEP-8 as their code style.

Use of a Git repository is standard practice at Softwares-R-Us and most of the steps require the use of Git and GitHub.

There are multiple steps in this task, and you must perform each step to a satisfactory level. Please note that you’ll need the results of the tasks outlined in this assessment tool for future tasks as well.

You may answer any questions in the provided template (if available) and the use of screenshots is encouraged. However, you must also provide the actual source code as a ZIP-file of the project for any programming tasks. Make sure to remove the Virtual Environment folder (venv or .venv) from the ZIP-file before uploading.

You must document your code properly. Use docstrings where needed including but not limited to entire classes and methods. Use inline comments to clarify certain parts of code.

If you use any external resources, you should provide references.

## Step 1 – Knowledge Question (40-70 words)

In your own words, describe what hashing is in general.

Hashing is taking data and making a number from it. If you put the same data in you will get the same number out. It is a one way operation. There are a few use cases but can be split into cryptography and non-cryptography. Cryptography is used for passwords. Non-cryptography is used to identified file to confirm a file hasn't changed, to retrieve a file in a array and can be used to find out if part of a set or not. 

## Step 2 – Knowledge Question (60-100 words)

Research hashing algorithms. Describe advantages and disadvantages for at least three different hashing algorithms. Please provide references for external resources. 

https://en.wikipedia.org/wiki/Hash_function#Identity_hash_function

Identity hash function is the simplest of them. It takes the data itself and than turn it into an integer and that integer is used as the hash value.
advantages
    - The computing cost is effectively zero.
    - This hash function is perfect, as it maps each input into a distinct value.
disadvantage
    - the object needs be small enough to fit into a 32bit integer, which cuts out a lot of things

https://en.wikipedia.org/wiki/Pearson_hashing

Parson hashing is designed for fast execution on processors with 8-bit registers. The input can be any number of bytes, it produces a hash that is strongly dependent on every single bytes of the input. It requires only a few instructions and a 265-byte lookup table.

advantages
    - it is extremely simple, good to learn on
    - can run fast on resource-limited processors
    - low collisions
disadvantages
    - with the look-up table can prohibitive on memory-limited processors  

https://en.wikipedia.org/wiki/BLAKE_(hash_function)#BLAKE2

blake comes in two variants. One uses 32-bit words to create up to 256 bits long hashes and the other uses a 64-bit words to crate hashes up to 512 bits long hashes. Blake2d is used in argon2.

advantages
    - It is fairly new and is faster than alot of older hashing algorithms.
    - It is unkeyed cryptographic hash function.
    - It is more secure and is immune to length extension attacks.
disadvantages
    - If you don't need to be cryptographically secure than it is slower and takes more resources.  



## Step 3 – Knowledge Question (50-90 words)

Provide a stepwise description (algorithmic) of 
https://en.wikipedia.org/wiki/Argon2
a) how you can store a password safely using hashing techniques and 

the password is entered to be set in text.
the hashing function is call parsing in the password.
if no extra parameters is passed in with the password argon2 uses it's constants and a random salt is securely created.
the password and the salt are the inputs for the hashing.
the output is the hash with the salt stored in the hash.

b) how you can verify that some string is the right password?

argon2 has a verify method.
past to it the text and the hash.
it will extract the salt from the hash.
hash the text with the salt.
see if the two hashes match.

## Step 4 – Knowledge Question (20-40 words)

What is the purpose of a “salt” when hashing a password? What are the two most important properties of a “salt”?

Salt is additional random data feed into a one way hashing algorithm that hashes passwords or pass phrases. The salt makes guessing the password or pass phrases from the hash alot harder and also helps protect passwords/phrases that occur multiply times in a database because each entry has it's own salt.

## Step 5 – Add password to Player class

In this step, you will be adding functionality to the Player class to store a password in a safe manner. This step has multiple parts to it.

    -Install the external package argon2-cffi from pypi using pip or your IDE. Document how you installed this package.

    I installed the package inside a python virtual environment with pip
    pip install argon2-cffi

    and in my player class 
    from argon2 import PasswordHasher

    -Read the documentation for this package to understand what this package has to offer.
    https://argon2-cffi.readthedocs.io/en/stable/argon2.html


    -Add a method add_password to the Player class. It should accept a single argument (a string), which is the plaintext password. Determine which function to use from the argon2 package and implement the function to calculate a hashed version of the password. Store this value in a private instance variable. Do not create a property for this value. You may have to initialise this instance variable in the initialiser method.
    -Add a method verify_password to the Player class. It should also accept a single argument (a string), which is the plaintext password which should be checked, and return a Boolean indicating whether there is a match. 
    -Implement this method to verify that the provided password matches the stored password.
    -Create at least two unit tests to check whether your implementations work correctly.
    -Commit your changes and push to your remote GitHub repository.
    
    -Answer the question “How does the argon2-cffi package handle salt?”
    If the hash method is called without a salt argument default to None, a random salt will securely created.

