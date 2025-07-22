##Building URL Dynamically
### Variables Rules and URL Building

from flask import Flask, redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to the house"
@app.route('/success/<int:score>')## here init is our won parameter and it is dynamically and also called variable rules
def success(score):
    return "The person has passed and the marks is "+str(score)


@app.route('/fail/<int:score>') 
def fail(score):
    return "The person has failed and the marks is "+str(score)


@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        reult='success'
    return redirect(url_for(result,score=marks))


if __name__=='__main__':
    app.run(debug=True)