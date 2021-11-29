from flask import Flask, request, jsonify

from CheckInput import CheckExpression
from EvaluatePosfix import EvaluatePostFix
from Tokenizer import token_expressions
from convertToPostFix import *

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle_get(path):
    checker = CheckExpression(path)

    if checker.check_if_has_more_than_single_parentheses():
        result = r"expressao deve conter apenas um parenteses"
    elif checker.check_if_has_number_too_long():
        result = r"numero deve estar no intervalo [-99999,99999]"
    else:
        try:
            list_of_tokens = token_expressions(path)
            postfix_expression = ConvertorToPosfix(
                list_of_tokens).translate_infix_to_posfix()
            result = EvaluatePostFix(postfix_expression).evaluate_posfix()
        except:
            result = "insira uma expressao matematica valida"

    output_data = {'status': 'OK', 'result': result}
    return jsonify("result": result)

if __name__ == '__main__':
    #app.debug = False
    app.run(host='0.0.0.0', port=3001)
