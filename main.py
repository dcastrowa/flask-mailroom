import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY').encode()


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/new_donation', methods=['GET', 'POST'])
def new_donation():
    if request.method == 'POST':
        d = Donor.select().where(Donor.name == request.form[
            'name']).get()
        donation = Donation(donor=d, value=request.form["amount"])
        donation.save()

        return redirect(url_for('all'))

    else:

        return render_template('new_donation.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
