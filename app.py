from flask import Flask, jsonify

# Create the "App" (The Clerk)
app = Flask(__name__)

# Define the "Window" where people ask questions
@app.route('/')
def home():
    # This is the data we send back
    return jsonify({
        "status": "Online",
        "company": "Agoda",
        "message": "Welcome to the DevOps Lab"
    })

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
