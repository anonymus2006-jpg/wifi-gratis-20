import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_qr(url, filename="qr_code.png"):
    # Crear una instancia de QRCode con configuraciones personalizadas
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Agregar los datos (URL)
    qr.add_data(url)
    qr.make(fit=True)

    # Crear la imagen del código QR
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Guardar la imagen
    qr_image.save(filename)
    print(f"Código QR generado y guardado como '{filename}'")

# URL de la página web (ajusta esto según tu configuración)
website_url = "http://localhost:5500/index.html"

# Generar el código QR
generate_qr(website_url, "website_qr.png")
