# 1.creating a simple web apllication with flask 
#WSGI is standard for connecting with web server and also it makes easy and quick 

from flask import Flask
app=Flask(__name__)

@app.route('/sample',methods=['GET'])
#above one is decorator
#rules and options will be given in the above one 
#it have string values which will be displaying the url 
def welcome():
    return "starting grasping quick.you dont have enough time"

@app.route('/sample2')
def welcome1():
    return "welcome to my second part"
    
if __name__=='__main__':
    app.run(debug=True)
#here the debug =true is mainly given because it will restart your server 

