from flask import Flask,render_template,Response
import cv2
 
app=Flask(__name__)
camera=cv2.VideoCapture(0)

def generate_frames():
    while True:#here while is used for the to read the frames continuously
        success,frame=camera.read()#read the camera frame## here sucess is boolean variable
        if not success:
            break
        else:
            ## if it is true then i will encode it
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')## this func function will be generating or will be taking the frames from my webcam and it will basically pass this entire response back to this index.html

if __name__=="__main__":
    app.run(debug=True)