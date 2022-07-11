from flask import Flask, render_template,session,redirect,request
app = Flask(__name__)
app.secret_key = 'super secret key'
@app.route("/login", methods=['GET'])
def loginPage():
    return render_template('login.html')

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect('/')

@app.route("/login", methods=['POST'])
def login():
    id = request.form.get('id')
    password = request.form.get('password')
    if id=='root' and password == '1234':
        session['id']='root'
    else:
        session['id']='guest'
    return redirect('/')

@app.route("/")
def hello():
    list = [ 
        { 'key' : 1, 'tag' : 'tag1', 'value' : 'value-1'}, 
        { 'key' : 2, 'tag' : 'tag1', 'value' : 'value-2'}, 
        { 'key' : 3, 'tag' : 'tag2', 'value' : 'value-3'}
    ]
    templateData = {
        "list" : list
    }
    return render_template('index.html', **templateData)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)