print("Welcome to Juicy Lifts: the Workout Customizer Tool!")

import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Today's Workout")
pdf.output("workout.pdf", "F")
#def add_image(image_path):
#    pdf = FPDF()
#    pdf.add_page()
#    pdf.image(image_path, x=10, y=8, w=100)
#    pdf.set_font("Arial", size=12)
#    pdf.ln(85)  # move 85 down
#    pdf.cell(200, 10, txt="{}".format(image_path), ln=1)
#    pdf.output("workout.pdf")
    
#if __name__ == '__main__':
#    add_image('C:/Users/Gavin Lafferty/Desktop/mypic.jpg')

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")

def send_email(subject="Workout", html="<p>Today's Workout</p>", pdf="workout.pdf"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    
    #print("SUBJECT:", subject)
    
    message = Mail(from_email=MY_EMAIL, to_emails=MY_EMAIL, subject=subject, html_content=html)
    file_path = 'workout.pdf'
    with open(file_path, 'rb') as f:
        data = f.read()
        f.close()
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType('application/pdf')
    attachment.file_name = FileName('JuicyLiftWorkout.pdf')
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId('Example Content ID')
    message.attachment = attachment
    try:
        response = client.send(message)
        #print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        #print(response.status_code) #> 202 indicates SUCCESS
        return response
    except Exception as e:
        print("OOPS", e.message)
        return None
    

if __name__ == "__main__":
    example_subject = "Juicy Lifts Workout"
    example_html = f""" 
    <h3> Welcome to Juicy Lifts! </h3>
    <p> Attached to this email you find a PDF with a workout that addresses your specific fitness needs. Time to hit the gym! </p>
    """
    example_pdf = "workout.pdf"
    #example_html = f"""
    #<h3>This is a test of the Daily Briefing Service</h3>
#
    #<h4>Today's Date</h4>
    #<p>Monday, January 1, 2040</p>
#
    #<h4>My Stocks</h4>
    #<ul>
    #    <li>MSFT | +04%</li>
    #    <li>WORK | +20%</li>
    #    <li>ZM | +44%</li>
    #</ul>
#
    #<h4>My Forecast</h4>
    #<ul>
    #    <li>10:00 AM | 65 DEGREES | CLEAR SKIES</li>
    #    <li>01:00 PM | 70 DEGREES | CLEAR SKIES</li>
    #    <li>04:00 PM | 75 DEGREES | CLEAR SKIES</li>
    #    <li>07:00 PM | 67 DEGREES | PARTLY CLOUDY</li>
    #    <li>10:00 PM | 56 DEGREES | CLEAR SKIES</li>
    #</ul>
    #"""
#
    #send_email(example_subject, example_html, example

