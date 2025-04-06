from flask import Flask, request, jsonify, send_from_directory
from detect import detect_helmet_and_plate
import os

# Initialize Flask app
app = Flask(__name__, static_folder="../frontend")
UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Serve frontend HTML
@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

# Serve static files (CSS/JS)
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# Serve uploaded output video
@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Upload video handler
@app.route("/upload", methods=["POST"])
def upload_video():
    print("🔔 Upload route hit")  # Debug log

    if 'video' not in request.files:
        print("🚫 No video in request")
        return jsonify({'error': 'No video uploaded'}), 400

    video = request.files['video']
    if video.filename == '':
        print("🚫 No selected file")
        return jsonify({'error': 'No selected video'}), 400

    # Save uploaded video
    path = os.path.join(app.config['UPLOAD_FOLDER'], video.filename)
    video.save(path)
    print(f"📁 Video saved to: {path}")

    # Run detection
    output_path, plates = detect_helmet_and_plate(path)
    print(f"✅ Detection complete. Output video: {output_path}")
    print(f"🛑 Detected plates: {plates}")

    # Send relative URL for frontend to access
    relative_url = "/uploads/" + os.path.basename(output_path)

    return jsonify({
        "output": relative_url,
        "plates": plates
    })

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
