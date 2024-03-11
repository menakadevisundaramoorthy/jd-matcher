# JD Matcher

JD Matcher is a tool designed to match job descriptions (JDs) with candidate resumes. It uses advanced natural language processing (NLP) techniques to analyze and compare the content of job descriptions and resumes, providing insights into the suitability of candidates for specific roles.

## Features

- **JD Analysis**: Upload and analyze job descriptions to identify key skills, qualifications, and responsibilities.
- **Resume Parsing**: Upload candidate resumes to extract relevant information such as skills, experience, and education.
- **Matching Algorithm**: Utilizes sophisticated matching algorithms to determine the degree of fit between job descriptions and resumes.
- **Visualization**: Provides visualizations and reports to summarize the match results and highlight areas of alignment or mismatch.
- **Customization**: Allows users to customize matching criteria and weights to prioritize different aspects of the match.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/jd-matcher.git
   cd jd-matcher
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```


3. **Set Up Environment Variables**:

Create a `.env` file in the project directory and add any necessary environment variables, such as API keys or configuration settings.

4. **Follow the steps to run the app**:

- On __MacOS/Linux__ to configure and run flask, follow the steps below:
    ```bash
    export FLASK_APP=application.py
    export FLASK_ENV=development
    python3 -m flask run
    ```
    If `python3` command is not found or for older versions, use: `python -m flask run` or simply run `flask run`


 - On __Windows__, to configure and run flask, follow the steps below:
    ```bash
    set FLASK_APP=application.py
    set FLASK_ENV=development
    flask run
    ```
The Flask server should be started and running on http://127.0.0.1:5000/


## Usage

1. **Curl command to test**:
    Modify the inputs and test.
    ```bash
    curl --location 'http://127.0.0.1:5000/jdmatcher' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "resumes": "<Resume_Path (Path of the PDF file)>",
        "job_description": "job_description_goes_here"
        }'
    ```
