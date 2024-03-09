from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor, CKEditorField
import smtplib
import os
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///information.db'
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def about2():
    return render_template('about_2.html')


@app.route('/journey')
def journey():
    return render_template('journey.html')


@app.route('/donate', methods=["GET", "POST"])
def donate():
    if request.method == "POST":
        with open('customer.txt', 'a', encoding='utf-8') as file:
            user_amount = request.form.get('flexRadioDefault')
            user_payment = request.form.get('DonationPayment')
            user_feedback = request.form.get('feedback')
            user_name = request.form.get('donation-name')
            user_email = request.form.get('donation-email')
            new_infor = [
                user_email,
                user_name,
                user_amount,
                user_feedback,
                user_payment
            ]
            file.write(f'{new_infor}\n')
        # db.session.add(new_infor)
        # db.session.commit()
        return redirect(url_for('about2'))

    return render_template('donate2.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


MAIL_ADDRESS = os.environ.get("MAIL_ADDRESS")
MAIL_APP_PW = os.environ.get("MAIL_APP_PW")
TO_MAIL = 'quocbao0905461606@gmail.com'


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MAIL_ADDRESS, MAIL_APP_PW)
        connection.sendmail(
            from_addr=MAIL_ADDRESS,
            to_addrs=TO_MAIL,
            msg=email_message
        )


@app.route('/about-us', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.form
        send_email(data["volunteer-name"], data["volunteer-email"], data["volunteer-phone"], data["volunteer-subject"])
        return render_template("contact.html", msg_sent=True)
    return render_template('index.html')


@app.route('/qr-donate')
def qrdonate():
    return render_template('donate.html')


@app.route('/season-1')
def season1():
    return render_template('season1.html')


@app.route('/season-2')
def season2():
    return render_template('season2.html')


@app.route('/season-3')
def season3():
    return render_template('season3.html')


@app.route('/season-4')
def season4():
    return render_template('season4.html')


@app.route('/season-5')
def season5():
    return render_template('season5.html')


@app.route('/season-6')
def season6():
    return render_template('season6.html')


if __name__ == "__main__":
    app.run(debug=True)
