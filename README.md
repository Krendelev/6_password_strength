# Password Strength Calculator

This script will calculate the strength of your password according to the following criteria:

- minimum length of 8 characters
- lack of character repetition
- the use of both upper-case and lower-case letters (case sensitivity)
- inclusion of one or more numerical digits
- inclusion of special characters, such as @, #, $

In addition, it can check your password against passwords blacklist if provided. Various blacklists can be found in [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) repository. List should be in `plaintext`.

## Quick Start

```bash
$ python password_strength.py
Enter your password:
Passwords strength is 7 out of 10

$ python password_strength.py darkweb2017-top10000.txt
Enter your password:
Passwords strength is 1 out of 10
```

## Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
