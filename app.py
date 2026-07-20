from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/run")
def run_check():
    result = subprocess.run(["python", "check_specs_automation.py"], capture_output=True, text=True)
    return result.stdout

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)