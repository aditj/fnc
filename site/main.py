from flask import Flask,render_template,request,url_for,redirect,session
import passv
from hashlib import md5
import add_stuff
import get_var
import captcha

app =Flask(__name__,static_url_path='/static')
#inf routes
#home page
@app.route('/')
def main():
    return render_template('home.html')
#login page
@app.route('/login',methods=['GET','POST'])
def login():
    error="yo"
    if request.method=='POST':

        if passv.checkhash(request.form['username'],md5(str(request.form['password']).encode()).hexdigest())==True:
            session['username'] = request.form['username']
            session['name']=get_var.get_name(request.form['username'])

            return redirect(url_for('dash'))
        else:
            error="invalid creds boi"
    return render_template('login.html',error = error)
@app.route('/fatal')
def fatal():
    return render_template('fatal.html')
#signup
@app.route('/signup',methods=['GET','POST'])
def signup():
    error="yo"
    if request.method=='POST':
        add_stuff.register(request.form["name"],request.form["username"],md5(str(request.form["password"]).encode()).hexdigest(),request.form["email"])
        return redirect(url_for('main'))
    return render_template('signup.html',error = error)
#dash
@app.route('/dash',methods=['GET','POST'])
def dash():
    error =None
    if request.method=='POST':
        print("success2")
        add_stuff.add_api(session['username'],request.form["href"])
        return redirect(url_for('dash'))
    if 'username' in session.keys():
        return render_template('dash.html',name=session['name'],detail = get_var.get_api_detail(session['username']),error=error)
    else:
        return redirect(url_for('main'))
@app.route('/logout')
#logout
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   session.pop('name',None)
   return redirect(url_for('main'))
#captcha
@app.route('/<api_id>',methods=['GET','POST'])
def captch(api_id):
    if captcha.check_api(api_id)==False:
        return redirect('/fatal')
    error=None
    img=captcha.get_image()
    if request.method=='POST':
        if img[1]==request.form["captcha"]:

            captcha.increasecount(api_id,img[2])
            print("true")
            return redirect(img[0])
        else:
            error="Renter"
            return render_template('captcha.html',error= error,file_name1="static/img/" +img[0])
    return render_template('captcha.html',error= error,file_name1="static/img/"+img[0])
#api
#initialize
if __name__ == '__main__':
    app.secret_key = 'my unobvious secret key'

    app.debug = True
    app.run()
