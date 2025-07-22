from flask import Flask

# wsgi
app=Flask(__name__)# Ye line ek Flask application banati hai.
#Flask(__name__) ka matlab hai ki current Python file ko Flask app banaya gaya hai.
#app variable aapke Flask app ko represent karega.

@app.route('/')##Ye ek route define karta hai:
#@app.route('/') ka matlab hai jab koi user home page (http://localhost:5000/) par jaata hai, tab ye function chalega.
def welcome():
    return "welcome"


if __name__ =='__main__':##Ye code sirf tab chalega jab aap is file ko direct run karoge (na ki kisi aur file se import karoge):## yeh se code execute hona start hoga


    app.run(debug=True)