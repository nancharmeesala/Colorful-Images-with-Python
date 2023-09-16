import cv2
import socket
import pickle
import struct

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)  # Use the default camera (change the index if you have multiple cameras)

# Create a socket to send video frames
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.29.252'  # Replace with your server's IP address
port = 9999
server_socket.bind((host_ip, port))
server_socket.listen(5)  # Listen for incoming connections

print(f"Listening on {host_ip}:{port}")

# Accept a client connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

while True:
    try:
        ret, frame = cap.read()  # Read a frame from the camera
        serialized_frame = pickle.dumps(frame)  # Serialize the frame
        message_size = struct.pack("L", len(serialized_frame))  # Pack message size

        # Send the message size first
        client_socket.send(message_size)

        # Send the frame data
        client_socket.send(serialized_frame)

        # Display the frame locally (optional)
        cv2.imshow("Video Streaming", frame)
        cv2.waitKey(1)

    except Exception as e:
        print(f"Error: {str(e)}")
        break

# Release the camera and close OpenCV window
cap.release()
cv2.destroyAllWindows()

# Close sockets
client_socket.close()
server_socket.close()
