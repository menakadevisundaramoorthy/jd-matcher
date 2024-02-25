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

    # validate cart_value
#    if 'cart_value' not in keys or type(data['cart_value']) is not int:
#        abort_request("Please enter valid cart_value")

    # validate delivery_distance
#    if 'delivery_distance' not in keys or type(data['delivery_distance']) is not int:
#        abort_request("Please enter valid delivery_distance")

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
