import smtplib
from flask import Flask, request, jsonify
from email.mime.text import MIMEText


app = Flask(__name__)

@app.route('/send', methods=['POST'])
def enviar_correo():
  remitente = request.form['remitente']
  destinatario = request.form['destinatario']
  asunto = request.form['asunto']
  mensaje = request.form['mensaje']


  # Crea un nuevo mensaje de correo electrónico
  msg = MIMEText(mensaje)

  # Configura los encabezados del mensaje
  msg['From'] = remitente
  msg['To'] = destinatario
  msg['Subject'] = asunto

  # Conéctate al servidor SMTP de Gmail
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(remitente, 'trkv nmtl oglx aoxw ')
    server.sendmail(remitente, destinatario, msg.as_string())
    
    
  return jsonify({
    'mensaje':'correo enviado'
  })

if __name__=='__main__':
  app.run(debug=True)
