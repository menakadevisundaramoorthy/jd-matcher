import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(api_key="")

# Load environment variables
load_dotenv()

# Set up OpenAI API key

def get_chat_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=3000
    )
    return response.choices[0].message.content

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    print(text)
    return text


def analyze(job_description, resume):
    print(resume)
    if resume is not None:
        resume_text = input_pdf_text(resume)
        input_prompt = f"""
        Hey Act Like a skilled or very experienced ATS (Application Tracking System) with a deep understanding of the tech field, software engineering, data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description.

        You must consider the job market is very competitive, and you should provide the best assistance for improving the resumes. Assign the percentage matching based on JD and the missing keywords with high accuracy.

        resume: {resume_text}
        description: {job_description}

        I want the response in one single string having the structure: {{"JD Match": "%", "MissingKeywords": [], "Profile Summary": ""}}
        """
        return get_chat_response(input_prompt)
