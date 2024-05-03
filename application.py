"""
Author: Menakadevi Sundaramoorthy
Date: February 24, 2024
"""

from flask import Flask, Response, request, abort
from jdmatcher import analyze

app = Flask(__name__)

@app.route('/jdmatcher', methods=['POST'])
def match_jd_and_resume():
    data = request.json
    keys = data.keys()

    resumes = data['resumes']
    job_description = data['job_description']

    try:
        return analyze(job_description, resumes)
    except Exception as e:
        abort_request(str(e.args[0]))

def abort_request(message):
    abort(Response('{"error": "' + message + '"}', 400, content_type="application/json"))

if __name__ == '__main__':
    app.run(debug=True)
