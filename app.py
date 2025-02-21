import hmac
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

api_secret = '328TZQ5vwNWr2QF9JM01Ci7SnrviE7ZQ'  # Reemplaza con tu clave secreta

@app.route('/webhook', methods=['POST'])
def webhook():
    # Cuerpo de la solicitud
    request_body = request.get_data().decode('utf-8')
    
    # Obtener la firma de la cabecera X-Noones-Signature
    provided_signature = request.headers.get('X-Noones-Signature')

    # Calcular la firma HMAC
    calculated_signature = hmac.new(api_secret.encode(), request_body.encode(), hashlib.sha256).hexdigest()

    # Verificar si las firmas coinciden
    if provided_signature == calculated_signature:
        # Procesar el evento si las firmas coinciden
        print('Firma verificada correctamente')
        return jsonify({'status': 'success'}), 200
    else:
        # Responder si la firma no coincide
        return jsonify({'status': 'error', 'message': 'Firma incorrecta'}), 403

if __name__ == '__main__':
    app.run(debug=True)
