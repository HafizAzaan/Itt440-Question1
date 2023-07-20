import socket

def send_and_receive_data(server_address, server_port, student_id):
    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Send the student ID to the server
        client_socket.send(student_id.encode())

        # Receive and print the server response
        response = client_socket.recv(1024).decode()
        print("Server response:", response)

        # Close the connection
        client_socket.close()

        # Return the unique URL for the next question and instructions
        return response.strip()

    except Exception as e:
        print("Error:", e)
        return None

if __name__ == "__main__":
    server_address = "izani.synology.me"
    server_port = 8443
    student_id = "2022787265"  # Replace with your actual UiTM Student ID

    url_for_next_question = send_and_receive_data(server_address, server_port, student_id)
    if url_for_next_question:
        print("Next question URL:", url_for_next_question)
    else:
        print("Failed to retrieve the next question URL.")
