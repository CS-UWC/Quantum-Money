# Quantum Money

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



