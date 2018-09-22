from flask import Flask,flash,request,render_template,redirect
from wtforms import Form,StringField,validators
import random
import sqlite3
from flask_wtf import FlaskForm
import sqlite3
#connection of database
conn = sqlite3.connect('data.db')
#coolect data
cursor_ads = conn.execute("SELECT file_name,ans FROM ads")
cursor_apis = conn.execute("SELECT api_id,count FROM api")
dict_ans={}
for i in cursor_ads:
    dict_ans[i[0]]=i[1]
#create random image
imglist=[]
for i in cursor_ads:
    imglist.append(i[0])
sr= random.SystemRandom()
file_name = sr.choice(imglist)
#validationFunction
def valid(form,field):
    print("HELLO")
    global file_name
    if dict_ans[file_name]!=field.data:
        flash("NC")
        raise validators.ValidationError('Captcha Not Correct')
#formClass
class captcha(Form):
    ans = StringField(u'Your Answer',[valid])
#image address
add_img= "/static/img/"+file_name
#app begin
app =Flask(__name__,static_url_path='/static')
#main Routing
@app.route("/main", methods=['POST','GET'])
def main():
    form = captcha(request.form)

    if request.method == 'POST' and form.validate():
        print(form.validate())
        flash('Correct!')
        return redirect("http://www.google.com")
    return render_template('index.html', form=form,file_name1=add_img )
#api Routing
@app.route('/captcha/<api_key>')
def captchal(api_key):
   #return 'Hello %s!' % name
   form = captcha(request.form)

   if request.method == 'POST' and form.validate():
       print(form.validate())
       flash('Correct!')
       return redirect("http://www.google.com")
   return render_template('index.html', form=form,file_name1=add_img )
#initialize
if __name__ == '__main__':
    app.secret_key = 'my unobvious secret key'

    app.debug = True
    app.run()
