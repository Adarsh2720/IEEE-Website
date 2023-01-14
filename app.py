from flask import Flask ,render_template, request
from email.message import EmailMessage
import ssl
import smtplib

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/council")
def team():
    return render_template('council.html')

@app.route("/events")
def events():
    return render_template('events.html')

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    return render_template('contact.html')
    
@app.route("/footer")
def footer():
    return render_template('footer.html')

@app.route("/details/pygame")
def pygame():
    return render_template('detail_pygame.html')

@app.route("/workshops")
def workshops():
    return render_template('workshop.html')

@app.route("/magazines")
def magazine():
    return render_template('magazine.html')

if __name__ == '__main__':  
   app.run(debug = True)  