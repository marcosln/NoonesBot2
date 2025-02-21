from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Si es una solicitud GET, significa que es el desafío de Noones
    challenge = request.headers.get('X-Noones-Request-Challenge')
    if challenge:
        return Response(challenge, mimetype='text/plain')
    
    # Si es una solicitud POST, significa que es una notificación de Noones
    if request.method == 'POST':
        # Verificar que el tipo de contenido sea 'application/json'
        if request.content_type != 'application/json':
            print(f"Tipo de contenido incorrecto: {request.content_type}")
            return Response('Unsupported Media Type', status=415)

        try:
            # Procesar el JSON recibido
            data = request.json
            print("Notificación recibida:", data)
            # Aquí puedes agregar más lógica para procesar las notificaciones
            return Response("OK", status=200)

        except Exception as e:
            print("Error al procesar JSON:", e)
            return Response("Error procesando JSON", status=400)
    
    # Si no es ni GET ni POST, responder con error
    return Response("Método no permitido", status=405)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
