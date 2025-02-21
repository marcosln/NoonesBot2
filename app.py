from flask import Flask, request, Response
import json

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Manejar el desafío de verificación
    challenge = request.headers.get('X-Noones-Request-Challenge')
    if challenge:
        return Response(challenge, mimetype='text/plain')

    # Asegúrate de que el contenido sea JSON
    if request.content_type != 'application/json':
        return Response('Unsupported Media Type', status=415)

    # Procesar la notificación de Noones en formato JSON
    try:
        data = request.json
        print("Notificación recibida:", data)
        # Aquí puedes agregar lógica adicional (por ejemplo, enviar alertas)
        return Response("OK", status=200)
    except Exception as e:
        print("Error al procesar JSON:", e)
        return Response("Error procesando JSON", status=400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
