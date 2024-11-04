#integrating the html with the flask application  
#HTTP verb GET and POST
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
   return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    #return "the person passed score is "+str(score)
    #return "<html><body><h1>the result will be displayed on the web page </h1></body></html>"
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person faided and finnally the score is "+str(score)

#result checker
@app.route('/finalresults/<int:marks>')
def finalresults(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

#result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    
    return redirect(url_for('success',score=total_score))

    

if __name__=='__main__':
    app.run(debug=True)
    
#in above i wanted to show the navigation page those who got success 
