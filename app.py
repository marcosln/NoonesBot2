import hashlib
import hmac
from flask import Flask, request, Response
import json

app = Flask(__name__)

api_secret = '92JarEF30ULie9SYp0JggKwLk524vHIc'  # Reemplaza con tu secreto de API

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        challenge = request.headers.get('X-Noones-Request-Challenge')
        if challenge:
            return Response(challenge, mimetype='text/plain')
        return "Webhook activo", 200

    if request.method == 'POST':
        # Verificar la firma
        provided_signature = request.headers.get('X-Noones-Signature')
        calculated_signature = hmac.new(api_secret.encode(), request.data, hashlib.sha256).hexdigest()
        
        if provided_signature != calculated_signature:
            return Response("Firma inválida", status=403)
        
        # Procesar el evento
        data = json.loads(request.data)
        print("Evento recibido:", data)
        return Response("Evento procesado", status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
