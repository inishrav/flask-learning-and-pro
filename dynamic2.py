# 2.building the url dynamically 
####variable rules and url building 
# in this i am going to import import the new library this will be very useful for building the url dynamically  
from flask import Flask,redirect,url_for
app=Flask(__name__)

#-->here the <int:score > is used to give the value in the integer 
# data type and also we can gve string format if it wanted to give you can give like <score>  is this enough to give 

@app.route('/success/<int:score>')
def success(score):
    #return "the person passed score is "+str(score)
    return "<html><body><h1>the result will be displayed on the web page </h1></body></html>"
 
#-->here note it -> i am npt giving evrything sattically like mark =60 or 35 
#it take the value when we access the server / web browser it will give you the result
#that what you are giving in the browser page

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

if __name__=='__main__':
    app.run(debug=True)
    
#in above i wanted to show the navigation page those who got success 
