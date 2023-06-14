from flask import Flask, request, render_template, make_response
import smtplib
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/feedback', methods=['POST', 'OPTIONS'])
@app.route('/feedback', methods=['POST', 'OPTIONS'])
def feedback():
    if request.method == 'OPTIONS':
        # Tangani permintaan OPTIONS dengan mengizinkan sumber daya lintas domain
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

    email = request.json.get('email')
    subject = request.json.get('subject')
    message = request.json.get('message')

    feedback_data = {
        'email': email,
        'subject': subject,
        'message': message
    }

    send_email(feedback_data)
    save_feedback_to_database(feedback_data)

    return 'Terima kasih atas umpan balik Anda!'


def send_email(feedback_data):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'cycleme.feedback@gmail.com'
    smtp_password = 'lumlpcwgbeuqqzzj'
    sender_email = 'cycleme.feedback@gmail.com'
    receiver_email = 'cycleme2023@gmail.com'
    subject = 'Feedback Submission'
    message = f"Email: {feedback_data['email']}\n\nSubject: {feedback_data['subject']}\n\nMessage: {feedback_data['message']}"

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")


def save_feedback_to_database(feedback_data):
    connection = mysql.connector.connect(
        host='35.225.237.23',
        user='myuser',
        password='mypass',
        database='feedback',
    )
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS feedback (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), subject VARCHAR(255), message TEXT)')

    cursor.execute('INSERT INTO feedback (email, subject, message) VALUES (%s, %s, %s)',
                   (feedback_data['email'], feedback_data['subject'], feedback_data['message']))

    connection.commit()
    connection.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
