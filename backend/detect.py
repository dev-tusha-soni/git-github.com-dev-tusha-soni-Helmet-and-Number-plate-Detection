def detect_helmet_and_plate(video_path):
    print("🧠 Detection started...")  # Debug log
    try:
        # Your existing detection logic here

        # Assume final output is saved as output_video_path
        output_video_path = "uploads/video.mp4"
        detected_plates = ["PB103C3107", "PB11W9231"]  # Just example values

        print("🎉 Detection completed successfully.")
        return output_video_path, detected_plates
    except Exception as e:
        print("❌ Error during detection:", e)
        return "error", []
