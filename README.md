# Double Counter Bypass

This script allows you to verify a Double Counter code by making an HTTP request to the verification service. It handles user input to ensure a valid code is provided and sends the appropriate request using custom headers.

## Features

- Prompts the user for a Double Counter verification link or code.
- Strips unnecessary parts of the URL to extract the verification code.
- Sends a GET request to the verification service with the required headers.
- Displays a success message upon successful verification.

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/zdashero/DCB.git
    cd DCB
    ```

2. Install the required Python package:

    ```sh
    pip install requests
    ```

## Usage

1. Run the script:

    ```sh
    python main.py
    ```

2. Enter the Double Counter verification link or code when prompted. The script will process the input and send a verification request.

## Example

```sh
$ python main.py
Double Counter Bypass by zdashero on github and discord
[+] Please, insert a valid Double Counter verification link / code here: https://verify.dcounter.space/v/your-code-here
[+] Successfully Bypasses Double Counter.
