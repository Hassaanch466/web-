from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages,sessions,idk



# Routes
@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/services')
def services():
    return render_template('services.html', title='Services')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html', title='Gallery')




@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        sender_email = request.form['email']
        message = request.form['message']

        try:
            send_email(name, sender_email, message)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            print("Email sending failed:", e)
            flash('There was an error sending your message. Try again.', 'danger')

        return redirect('/contact')

    return render_template('contact.html', title='Contact Us')

#  sender function
def send_email(name, sender_email, message):
    EMAIL = "yourclinicemail@gmail.com"
    PASSWORD = "your_app_password"  # password from Gmail

    msg = EmailMessage()
    msg['Subject'] = f"New Contact Form Message from {name}"
    msg['From'] = EMAIL
    msg['To'] = EMAIL
    msg.set_content(f"Name: {name}\nEmail: {sender_email}\n\nMessage:\n{message}")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
