from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    "id": 1,
    "title": "Software Developer",
    "location": "Remote",
    "salary": "Rs. 10,00,000"
}, {
    "id": 2,
    "title": "Software Developer 2",
    "location": "Mumbai, India",
    "salary": "Rs. 15,00,000"
}, {
    "id": 1,
    "title": "Software Analyst",
    "location": "Remote",
    "salary": "Rs. 12,00,000"
}]


@app.route('/')
def hello_world():
  return render_template("home.html", jobs=JOBS, company_name="Sushant")


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
