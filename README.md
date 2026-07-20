# Check Specs Automation Tool

This tool was created to quickly check specs of devices I manage or diagnose. It pulls information form the machine and displays it in a readable manner.

## What it does

- It helps me collect a lot of information faster
- It assist with less technical people

## Tech stack

- Python
- Docker

## How to run it

### Locally
```
pip install -r requirements.txt
python check-specs-automation.py
```

### With Docker
```
docker build -t check-specs-automation .
docker run --rm check-specs-automation
```
## Note on `app.py`

This repo originally contained a single standalone script (`check-specs-automation.py`) that runs once and exits. `app.py` was added afterward as a small Flask wrapper, so this same Docker image could be deployed as a long-running service in a local Kubernetes cluster (see my [Tier 2 Kubernetes project](https://github.com/antiguamaximo/K8s-local-cluster.git) for that part).

`check-specs-automation.py` itself is unchanged — `app.py` simply calls it via subprocess and exposes it over an HTTP endpoint. The Dockerfile's `CMD` was updated accordingly to run `app.py` instead of the original script directly.

## Sample output

![Sample output](screenshots/sample-output.png)

## What I learned
This was my first try creating a Docker image with a Python script. Thanks to it, I increased my hands-on experience with Docker and Python. Furthermore, while I was researching how to properly configure and structure this small project, I learned how a proper GitHub repository should look before it gets pushed. 

Specifically, dealing with dependencies caused me issues because of my lack of understanding. I did not know how to fully utilize the `requirements.txt` file. After researching for a bit (and some AI assistance), I was able to figure out a proper way to create a requirements document. 

Furthermore, I initially had my virtual environment and source files mixed together in the same folder, which taught me the importance of separating environment setup from the code that actually needs to be version-controlled.

The Dockerfile itself confused me, however there were a lot of resources on the web which ranged from complex Dockerfiles to more simple ones.

Added some extra stuff! CI/CD Stuff!
