from flask import Flask,request

app = Flask(__name__)
temp = 25
@app.route('/temp')
def get_temp():
    return str(temp)


@app.route('/temp',methods = ['POST'])
def post_temp():
    global temp
    val = request.form.get("value")
    if val:
        temp = val
        print(f"Temp = {temp}")
        return f"Temperature updated to {temp}\n"
    return f"ERRORRRRR :("