#learning part

'''arr=[1,2,3,4,5]
max=0
n=len(arr)
for i in range(0,n):
    if arr[i]>max:
        max=arr[i]

print (max)
'''
'''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/max', methods=['GET'])
def get_max():
    arr = [1, 2, 3, 4, 5]
    max_value = 0
    n = len(arr)
    for i in range(0, n):
        if arr[i] > max_value:
            max_value = arr[i]
    return jsonify(max=max_value)  # Return the max value as JSON

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode
'''

'''
from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/valuemultiplied',methods=['GET'])
def get_mul():
    val1=10
    val2=20
    mul=val1*val2
    return jsonify(valuemultiplied=mul)
if __name__=='__main__':
    app.run(debug=True)
    
'''

'''
from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/add',methods=['GET'])
def get_sub():
    val1=44
    val2=22
    add=val1+val2
    return jsonify(add=add)
if __name__=='__main__':
    app.run(debug=True)
'''

'''from flask import Flask,jsonify
app=Flask(__name__)
@app.route('/fact',methods=['GET'])
def get_fact():
    fact=1
    for i in range(1,n):
        fact=fact*i
    return jsonify(fact=fact)
if __name__=='__main__':
    app.run(debug=True)

'''
'''
msg="start learning everything we dont have time quick make it fast"
print(msg)
print("heyy its time begins")
'''

''' from flask import Flask
app=Flask(__name__)
@app.route('/')
def welcome():
    return 'heyy do it fast'
if __name__=='__main__':
    app.run()
'''


from flask import Flask, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/profile')
def profile():
    return 'Welcome to your profile!'

@app.route('/go-to-profile')
def go_to_profile():
    # Redirects to the 'profile' route using url_for
    return redirect(url_for('profile'))

if __name__ == '__main__':
    app.run(debug=True)
