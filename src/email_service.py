import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import GMAIL_USER, GMAIL_PASSWORD, SOPORTE


def FORMATO_MENSAJE(failed_urls, user_name):
    message = f"""
<html>
<head>
    <style type="text/css">
        @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;700&display=swap');

        body {{
            font-family: 'Open Sans', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #F5F5F7;
            color: #333;
        }}
        
        .container {{
            max-width: 600px;
            margin: 40px auto;
            background-color: #FFF;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }}

        .header {{
            background: linear-gradient(135deg, #004482, #0071BC);
            color: #ffffff;
            padding: 20px 30px;
            font-size: 24px;
            text-align: center;
        }}

        .content {{
            padding: 20px 30px;
            color: #666;
        }}

        strong, em {{
            color: #004482;
        }}

        ol li {{
            margin-bottom: 12px;
        }}

        .footer {{
            background-color: #EBF0F3;
            color: #666;
            padding: 20px 30px;
            text-align: center;
            font-size: 14px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            ¡Alerta, {user_name}! 🚨
        </div>
        <div class="content">
            <p>Hemos detectado problemas con algunas de nuestras APIs. Estos son los enlaces que presentaron fallos:</p>
            <ul>
                {"".join([f"<li>{url}</li>" for url in failed_urls])}
            </ul>
            <p>Por favor, revisa la situación para asegurarnos de que todo funcione correctamente. ¡Apreciaremos mucho tu ayuda!</p>
        </div>
        <div class="footer">
            PD: 🤖 Este mensaje es automático. Gracias por tu comprensión y rápida respuesta.
        </div>
    </div>
</body>
</html>
    """
    return message


def send_email(failed_urls):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(GMAIL_USER, GMAIL_PASSWORD)

    for soporte in SOPORTE:
        user_name = soporte["name"]
        user_email = soporte["email"]

        subject = "Notificación de fallo de API"
        body = FORMATO_MENSAJE(failed_urls, user_name)

        msg = MIMEMultipart()
        msg['From'] = GMAIL_USER
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html', 'utf-8'))

        server.sendmail(GMAIL_USER, user_email, msg.as_string())

    server.close()
