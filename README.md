# Quantum Money

Central Bank Digital Currencies and Blockchain technology are advancements within financial technologies that is shaping the modern global economy. Banks have recently begun developing digital currencies that aims to replace physical money used within circulation. Counterfeiting money, whilst non-trivial, can be performed using specialised equipment that defeats the trust and integrity of modern physical money and potentially digital currencies. Quantum mechanics reveals interesting properties that can effectively make money impossible to be forged. 

This repository demonstrates a working proof-of-concept implementation of Wiesner’s quantum money that will be issued by an online quantum banking system. A web-based banking application was developed to allow transactions with quantum bank notes such as buying items and sending to other users. The implemented system uses quantum hardware for randomly generating states, verifying quantum bank notes and can work with any arbitrary number of qubits stored on the bank notes.

## Setup

Using Python 3.11, setup a virtual environment in the root folder
```
python -m venv .
```

Activate the virtual environment and install the packages
```
python -m pip install -r requirements.txt
```

Run index.py and open 127.0.0.1:8080 in a web browser

### AWS Braket

This project utilises AWS Braket for executing quantum jobs on real quantum hardware.

By default, the simulator is used.

To switch to using Braket, modify the boolean in quantum/backend.py to False

```
USE_SIMULATOR = False
```

Next, it is copy the config.template file to the .aws folder within the user directory

Windows: C:/Users/your_username/.aws/config

Linux: ~/.aws/config

Replace the necessary fields with an access token from AWS that has the AmazonBraketFullAccess policy.

## Using the Quantum Bank System

There are two existing accounts already registered

| email | password |
|---|---|
|alice@gmail.com|test|
|bob@gmail.com|test|

After logging in, there are a few features you can try
- The Purchase QNotes button allows you to add QNotes to your wallet
- The store page offers two services for buying electricity units and airtime
- The transfer page allows for sending QNotes to other users by clicking the QNote visual and selecting the serial numbers.