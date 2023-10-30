from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def juego():
    return render_template('juego.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

if __name__ == "__main__":
    app.run(debug=True, port=5017)
