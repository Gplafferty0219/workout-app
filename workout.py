import os
import base64
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from fpdf import FPDF

print("Welcome to Juicy Lifts: the Workout Customizer Tool!")
print("Please enter some information about yourself below to get started!")
print(" ")

while True:
    FitnessGoals = input("Would you like to 'gain' or 'lose' weight?: ")
    if FitnessGoals == "gain":
        print("          Swole is your Goal!")
        break
    elif FitnessGoals == "lose":
        print("          Lean, Mean, Fitness Machine!")
        break
    else: 
        print("Please enter either 'gain' or 'lose'!")
while True:
    Muscles = input("Would you like to work out your 'upper' or 'lower' body?: ")
    if Muscles == "upper":
        print("          Get that Beach Body!")
        break
    elif Muscles == "lower":
        print("          Never skip Leg Day!")
        break
    else: 
        print("Please enter either 'upper' or 'lower'!")
while True:
    Equipment = input("Do you have access to 'full' or 'none' equipment?: ")
    if Equipment == "full":
        print("          A True Weightroom Junkie!")
        break
    elif Equipment == "none":
        print("          Home-Workout Warrior!")
        break
    else: 
        print("Please enter either 'full' or 'none'!")

if FitnessGoals == "gain" and Muscles == "upper" and Equipment == "full":
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(40, 10, "fun workout")
    pdf.output("workout.pdf", "F")
elif FitnessGoals == "lose" and Muscles == "lower" and Equipment == "none":
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(40, 10, "wimpy workout")
    pdf.output("workout.pdf", "F")

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
MY_EMAIL = os.environ.get("MY_EMAIL_ADDRESS")
def send_email(subject="Workout", html="<p>Today's Workout</p>", pdf="workout.pdf"):
    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
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

    send_email(example_subject, example_html, example_pdf)
    print("Thank you for chossing Juicy Lifts! Your email has been sent. Time to grind!")