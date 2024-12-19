from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hitung', methods=['POST'])
def hitung_kecepatan():
    try:
        jarak = float(request.form['jarak'])
        waktu = float(request.form['waktu'])
        
        if waktu <= 0:
            return "Waktu harus lebih besar dari 0."
        
        kecepatan = jarak / waktu
        return f"Kecepatan kendaraan adalah {kecepatan:.2f} km/jam."
    
    except ValueError:
        return "Input tidak valid. Harap masukkan angka."

if __name__ == '__main__':
    app.run(debug=True)
