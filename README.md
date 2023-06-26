# TennisIOAPI
REST API to receive data from WatchOS TennisIO project.

## Requirements
It's tested with Python 3.9.6.

## Installation

First, clone the API code:

```console
$ git clone git@github.com:ivangonzalezz/TennisIOAPI.git && cd TennisIOAPI
```

Then, install required packages:

```console
$ pip install -r requirements.txt
```

Finally, run the API service listening to any IP at port 8080:

```console
$ uvicorn main:app --host 0.0.0.0 --port 8080
INFO:     Started server process [60881]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```
