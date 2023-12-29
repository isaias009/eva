from flask import Flask, render_template, request
from eval import calculate

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

  if request.method == 'POST':
    exp = request.form['exp']
    caracteres=["+", "-", "*", "/"]

    for caracter in caracteres:
        exp = exp.replace(caracter, f" {caracter} ")
    
    result, steps = calculate(exp)

    steps_mod = []

    for index, step in enumerate(steps):
      section = step.split('=')
      obj = {
        "index": index + 1,
        "operation": section[0],
        "res": round(eval(section[1]), 4),
        "int": eval(section[1]).is_integer()
      }
      steps_mod.append(obj)

    return render_template('index.html', exp=exp, steps=steps_mod, result=round(result, 3))

  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
