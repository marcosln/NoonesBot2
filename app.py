from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Si es una solicitud GET, verificar si contiene el desafío
    if request.method == 'GET':
        challenge = request.headers.get('X-Noones-Request-Challenge')
        if challenge:
            return Response(challenge, mimetype='text/plain')
        else:
            # Si no hay desafío, devolver un mensaje simple
            return Response("Webhook endpoint activo", status=200)
    
    # Si es una solicitud POST, procesar como notificación
    if request.method == 'POST':
        # Verificar que el tipo de contenido sea 'application/json'
        if request.content_type != 'application/json':
            print(f"Tipo de contenido incorrecto: {request.content_type}")
            return Response('Unsupported Media Type', status=415)
        try:
            data = request.json
            print("Notificación recibida:", data)
            # Aquí puedes agregar la lógica para procesar la notificación
            return Response("OK", status=200)
        except Exception as e:
            print("Error al procesar JSON:", e)
            return Response("Error procesando JSON", status=400)
    
    return Response("Método no permitido", status=405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
