  
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
        print("  Swole is your Goal!")
        break
    elif FitnessGoals == "lose":
        print("  Lean, Mean, Fitness Machine!")
        break
    else: 
        print("Please enter either 'gain' or 'lose'!")
while True:
    Muscles = input("Would you like to work out your 'upper' or 'lower' body?: ")
    if Muscles == "upper":
        print("  Get that Beach Body!")
        break
    elif Muscles == "lower":
        print("  Never skip Leg Day!")
        break
    else: 
        print("Please enter either 'upper' or 'lower'!")
while True:
    Equipment = input("Do you have access to 'full' or 'none' equipment?: ")
    if Equipment == "full":
        print("  A True Weightroom Junkie!")
        break
    elif Equipment == "none":
        print("  Home-Workout Warrior!")
        break
    else: 
        print("Please enter either 'full' or 'none'!")

if FitnessGoals == "gain" and Muscles == "upper" and Equipment == "full":
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 5x5 Bench Press", ln=4)
    pdf.cell(1,10, "- 4x6 Chest Fly", ln=5)
    pdf.cell(1,10,"- 3x8 Skullcrushers", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 5x5 Bent-over Row", ln=8)
    pdf.cell(1,10,"- 4x6 Lateral Pull-Downs", ln=9)
    pdf.cell(1,10,"- 3x8 Bicep Curl", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "lose" and Muscles == "upper" and Equipment == "full":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 3x10 Bench Press", ln=4)
    pdf.cell(1,10, "- 3x10 Decline Bench Press", ln=5)
    pdf.cell(1,10,"- 3x12 Tricep Extensions", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 3x12 Single Arm Rows", ln=8)
    pdf.cell(1,10,"- 3x10 Later Pull-Downs", ln=9)
    pdf.cell(1,10,"- 3x12 Bicep Curls", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "gain" and Muscles == "upper" and Equipment == "none":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 4x15 Pushups", ln=4)
    pdf.cell(1,10, "- 4x10 Diamond Pushups", ln=5)
    pdf.cell(1,10,"- 4x8 Bench Dips", ln=6)
    pdf.cell(1,10,"- 4x8 Pike Pushups", ln=7)
    pdf.cell(1,10,"", ln=8)
    pdf.cell(1,10,"- 5x5 Pullups", ln=9)
    pdf.cell(1,10,"- 4x8 Inverted Rows", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "lose" and Muscles == "upper" and Equipment == "none":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 3x15 Burpees with Pushup", ln=4)
    pdf.cell(1,10, "- 3x15 Incline Pushup with Clap", ln=5)
    pdf.cell(1,10,"- 3x20 Mountain Climbers", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 3x8 Flex Hang", ln=8)
    pdf.cell(1,10,"- 3x6 Pullups", ln=9)
    pdf.cell(1,10,"- 3x12 Bench Dips with Leg Extension", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "gain" and Muscles == "lower" and Equipment == "full":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 5x5 Squats", ln=4)
    pdf.cell(1,10, "- 3x12 Lunges", ln=5)
    pdf.cell(1,10,"- 3x6 Front Squats", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 5x5 Deadlifts", ln=8)
    pdf.cell(1,10,"- 3x5 Romanian Deadlifts", ln=9)
    pdf.cell(1,10,"- 3x20 Calf Raises", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "lose" and Muscles == "lower" and Equipment == "full":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 3x10 Squats", ln=4)
    pdf.cell(1,10, "- 3x20 Lunges", ln=5)
    pdf.cell(1,10,"- 3x12 Bulgarian Split Squats", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 3x10 Deadlifts", ln=8)
    pdf.cell(1,10,"- 3x12 Hamstring Curls", ln=9)
    pdf.cell(1,10,"- 3x20 Calf Raises", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "gain" and Muscles == "lower" and Equipment == "none":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 5x10 Free Squats with 5sec. Hold", ln=4)
    pdf.cell(1,10, "- 5x10 One and a Quarter Squats", ln=5)
    pdf.cell(1,10,"- 4x8 Bulgarian Split Squat", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 3x6 Pistol Squats", ln=8)
    pdf.cell(1,10,"- 3x20 Calf Raises", ln=9)
    pdf.cell(1,10,"- 3x1min Wall Sit", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

    pdf.output("workout.pdf", "F")
elif FitnessGoals == "lose" and Muscles == "lower" and Equipment == "none":
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font("Arial", 'B', 24)
    pdf.cell(1, 15, "Today's Workout", ln=1)
    pdf.set_font("Arial",'', 16)
    pdf.cell(1,10, "Begin with a 10 minute warm up (bike, jog, or erg)", ln=2)
    pdf.cell(1,10, "", ln=3)
    pdf.cell(1, 10, "- 3x15 Jump Squats", ln=4)
    pdf.cell(1,10, "- 3x20 Split Squat with Jumps", ln=5)
    pdf.cell(1,10,"- 3x30sec Step Ups (for speed)", ln=6)
    pdf.cell(1,10,"", ln=7)
    pdf.cell(1,10,"- 3x16 Walking Lunge", ln=8)
    pdf.cell(1,10,"- 3x8 Broad Jumps", ln=9)
    pdf.cell(1,10,"- 3x8 Verical Jumps", ln=10)
    pdf.cell(1,10,"", ln=11)
    pdf.cell(1,10,"Finish with a 10 minute cool down (slow bike, jog, stretch)")

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
    <p> Attached to this email you will find a PDF with a workout that addresses your specific fitness needs. Time to hit the gym! </p>
    """
    example_pdf = "workout.pdf"

    send_email(example_subject, example_html, example_pdf)
    print(" ")
    print("Your email has been sent!")
    print(" ")

while True:
    Confirmation = input("Did you receive your email?: ")
    if Confirmation == "yes":
        print("Thank you for choosing Juicy Lifts! Go get on your grind!")
        break
    elif Confirmation == "no":
        print("Please make sure your email address was entered correctly and that your API key is working properly. Remember to also check your spam/junk folder as well.")
        break
    else:
        print("Please enter 'yes' or 'no'!")    