const express = require('express');
const app = express();
const port = 5500; // Set the desired port number
const nodemailer = require('nodemailer');

app.use(express.json());

// Configure the email transport
const transporter = nodemailer.createTransport({
  service: 'Gmail',
  auth: {
    user: 'cycleme.feedback@gmail.com', // Replace with your Gmail email address
    pass: 'lumlpcwgbeuqqzzj' // Replace with your Gmail password
  }
});

// Handle POST requests to /submit-feedback
app.post('/submit-feedback', (req, res) => {
  const { email, subject, message } = req.body;

  // Prepare the email content
  const mailOptions = {
    from: 'cycleme.feedback@gmail.com',
    to: 'cycleme2023@gmail.com',
    subject: subject,
    text: `From: ${email}\n\n${message}`
  };

  // Send the email
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      console.error('Error sending email:', error);
      res.status(500).send('Error sending feedback. Please try again.');
    } else {
      console.log('Email sent:', info.response);
      res.sendStatus(200);
    }
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
