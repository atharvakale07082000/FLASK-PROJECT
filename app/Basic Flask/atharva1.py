from flask import Flask
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return ' Administrator Area, guesrt not allowed'
@app.route( '/guest/<guest>/')
def hello_guest(guest):
    return ' guest users %s not having admin rights' % guest
@app.route('/user/<name>')
if name  == 'admin':
    return redirect(url_for ('hello_admin'))
else:
    return redirect(url_for ('hello_guest',guest = name))
if __name__ == '__main__'
app.run(debug = True)          
           

    
