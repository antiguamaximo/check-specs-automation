# Check Specs Automation Tool

This tool was created to quickly check specs of devices I manage or diagnose. It pulls information form the machine and displays it in a readable manner.

## What it does

- It helps me collect a lot of information faster
- It assist with less technical people
- test, builds, pushes on every push to `main` (CI/CD)

## Tech stack

- Python
- Docker
- GitHub Actions

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

## CI/CD Pipeline

```
Push to main → Checkout code (actions/checkout) → Set up Python + install dependencies → Run test (pytest) → Log in to Docker Hub → Build Docker image → Push image to Docker Hub, tagged with commit SHA
```
Every push to `main` triggers this pipeline automatically via GitHub Actions. Tests run before the image is built, so broken code never gets containerized or published — the pipeline "gates" on passing tests rather than just being a blind build-and-push

## Sample output

![Sample output](screenshots/sample-output.png)

## What I learned
This was my first try creating a Docker image with a Python script. Thanks to it, I increased my hands-on experience with Docker and Python. Furthermore, while I was researching how to properly configure and structure this small project, I learned how a proper GitHub repository should look before it gets pushed. 

Specifically, dealing with dependencies caused me issues because of my lack of understanding. I did not know how to fully utilize the `requirements.txt` file. After researching for a bit (and some AI assistance), I was able to figure out a proper way to create a requirements document. 

Furthermore, I initially had my virtual environment and source files mixed together in the same folder, which taught me the importance of separating environment setup from the code that actually needs to be version-controlled.

The Dockerfile itself confused me, however there were a lot of resources on the web which ranged from complex Dockerfiles to more simple ones.

### After adding the CI/CD Pipeline

Implementing a CI/CD pipeline for the first time was a challenging experience. From filename/import problems to diagnosing GitHub errors, everything that went wrong taught me something new.

Python cannot import a module with hyphens in its name, and that's how I had saved my original script: `check-specs-automation.py`, which caused an invalid syntax error. To fix this, I renamed the script to `check_specs_automation.py`. I then had to update every reference to the old filename across the project, and even missed one inside `deploy.yml`, which caused a failure.

Following up with Python, I also needed a test file. It was my first time writing one, so I had to research how it works and what should be expected of the result. I ended up requiring external assistance, and wrote one using `pytest`'s `capsys` fixture, since the `get_system_info()` function doesn't return anything, it just prints to stdout. The test needed to capture and check the printed output rather than a return value. This test now acts as a "gate" for the pipeline: if it fails, the image never gets built or pushed.

In addition, I learned about GitHub repo secrets. This saves me from hard-coding credentials into a workflow file, and instead lets me reference them via `${{ secrets.NAME }}`. This is exactly how the workflow in this repo accesses my Docker Hub token and username.

I also ran into an issue with GitHub that was vague, with no specific line number or clear cause. I reviewed the `deploy.yml ` structure and my code multiple times, assuming the problem was on my end. After checking githubstatus.com, though, it turned out there was an active GitHub Actions outage, that was the actual cause.