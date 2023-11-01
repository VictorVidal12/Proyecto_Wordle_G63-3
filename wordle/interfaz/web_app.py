from flask import Flask, render_template, url_for, session

app = Flask(__name__)
app.secret_key = 'DkGh78jMn9LpKwXeYqR5zA'


@app.route('/')
def registro():
    return render_template('registro.html', juego_url=url_for('juego'))


@app.route('/juego')
def juego():
    if 'casilla_activa' not in session:
        session['casilla_activa'] = (0, 0)
    return render_template('juego.html', casilla_activa=session['casilla_activa'])


if __name__ == "__main__":
    app.run(debug=True, port=5017)
