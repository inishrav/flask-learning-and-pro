from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

# Initialize the video capture object for the default camera
camera = cv2.VideoCapture(0)

# Function to generate frames for video streaming
def generate_frames():
    while True:
        # Read the camera frame
        success, frame = camera.read()
        if not success:
            print("Failed to capture image from camera.")
            break
        else:
            # Encode the frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in a format Flask can stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Home route to render the index HTML page
@app.route('/')
def index():
    return render_template('in.html')

# Video route to stream the video feed
@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
