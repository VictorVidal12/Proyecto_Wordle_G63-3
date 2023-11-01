from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def registro():
    return render_template('registro.html', juego_url=url_for('juego'))


@app.route('/Juego')
def juego():
    return render_template('juego.html')


if __name__ == "__main__":
    app.run(debug=True, port=5017)
