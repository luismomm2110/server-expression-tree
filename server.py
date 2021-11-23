from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/<expression>', methods=["GET"])
def handle_get(expression):
    output_data = {'status': 'OK', 'result': expression}
    return jsonify(output_data)


if __name__ == '__main__':
    #app.debug = True
    app.run(host='localhost', port=3001)
