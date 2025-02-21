from flask import Flask, request, Response
import json
import time

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Validar el desafío de Noones
        challenge = request.headers.get('X-Noones-Request-Challenge')
        if challenge:
            return Response(challenge, mimetype='text/plain')
        else:
            return Response("Webhook endpoint activo", status=200)
    
    if request.method == 'POST':
        # Revisar los encabezados de la solicitud
        if request.headers.get('Content-Type') != 'text/plain':
            return Response(
                json.dumps({
                    "status": "error",
                    "timestamp": int(time.time()),
                    "error": {
                        "code": 415,
                        "message": "Unsupported Media Type"
                    }
                }),
                status=415,
                mimetype='application/json'
            )

        # Revisar los encabezados Accept
        if request.headers.get('Accept') != 'application/json; version=1':
            return Response(
                json.dumps({
                    "status": "error",
                    "timestamp": int(time.time()),
                    "error": {
                        "code": 406,
                        "message": "Not Acceptable"
                    }
                }),
                status=406,
                mimetype='application/json'
            )
        
        try:
            # Procesar el cuerpo de la solicitud (esperamos que sea texto plano)
            data = request.get_data(as_text=True)
            print("Notificación recibida:", data)
            # Aquí puedes agregar lógica adicional para procesar la notificación
            return Response(
                json.dumps({
                    "status": "success",
                    "timestamp": int(time.time()),
                    "data": {
                        "success": True,
                        "offer_hash": data  # Puedes incluir el "offer_hash" aquí si es relevante
                    }
                }),
                status=200,
                mimetype='application/json'
            )
        except Exception as e:
            print("Error al procesar la solicitud:", e)
            return Response(
                json.dumps({
                    "status": "error",
                    "timestamp": int(time.time()),
                    "error": {
                        "code": 400,
                        "message": "Bad Request"
                    }
                }),
                status=400,
                mimetype='application/json'
            )
    
    return Response("Método no permitido", status=405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
