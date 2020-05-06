# Workout App

Sends you a customized workout program based on your fitness needs. The workout will be generated into a PDF and emailed to you.

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/workout-app/
```

Create and activate a new Anaconda virtual environment, perhaps named "gym-env":

```sh
conda create -n gym-env python=3.7
conda activate gym-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain an API Key from the [SendGrid](https://app.sendgrid.com/settings/api_keys) service. Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example
SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="larry@bigmuscles.com"

MY_NAME="Larry the Lobster"
```

## Usage

From within the virtual environment, you are now ready to run the code:

```sh
python app/workout.py
```

NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")