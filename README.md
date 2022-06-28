# dh-real-time-historical-crypto

This project demonstrates how to work with historical and real-time crypto data together.

## Components

* `Dockerfile`: The Dockerfile that extends the Deephaven server image to install the project dependencies
* `docker-compose.yml`: The docker-compose file that defines the local Dockerfile build, and the Deephaven application mode directory
* `requirements.txt`: The Python dependencies for the project
* `data/app.d/`: The Deephaven application mode directory 
  * `data/app.d/app.app`: The Deephaven application mode config file
  * `data/app.d/real_time_crypto.py`: The Python script that pulls data from Cryptowatch and creates the Deephaven real-time table
* `data/notebooks/`: Extra Python scripts to work with the historical and real-time data together

## Launch

Simply run

```
docker compose up
```

to launch the app, then go to http://localhost:10000 to view the tables and run the extra Python scripts.
