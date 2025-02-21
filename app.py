from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # Captura el desafío del encabezado
    challenge = request.headers.get('X-Noones-Request-Challenge')
    if challenge:
        return Response(challenge, mimetype='text/plain')

    # Procesa las notificaciones reales de Noones
    data = request.json
    print("Notificación recibida:", data)
    
    # Aquí puedes agregar lógica adicional, como enviar alertas o realizar llamadas
    return Response("OK", status=200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
