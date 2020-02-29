# Roboadvisor

[Project Description]
(https://github.com/prof-rossetti/intro-to-python/tree/master/projects/robo-advisor)

## Prerequisites 

    + Anaconda 3.7
    + Python 3.7
    + Pip

## Installation

Clone or download from [GitHub source] then navigate into the project repository 

```sh
cd roboadvisor
```

Use Anaconda to create and activate a new virtual enviornment. From inside this enviornment, install the package dependencies:

```sh
pip install requests python-dotenv
```
## Setup 

Before using or developing this application, take a moment to obtain an AlphaVantage API Key (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

```sh
API_KEY="abc1212"
```

## Usage 

Run the program 

```py
python robo.py
```