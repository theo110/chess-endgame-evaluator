import flask
import database

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route('/board', methods=['GET', 'POST'])
def board():
    if flask.request.method == "POST":
        turn = True
        if flask.request.form.get('move1') == "-1":
            turn = False
        position = flask.request.form.get('position1')
        currentDTZ = database.evaluate(position,turn)
        return(str(currentDTZ))
    return flask.render_template("board.html", evaluation=0)

if __name__ == "__main__":
    app.run(debug=True)
