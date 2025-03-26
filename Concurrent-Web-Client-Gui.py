import socket
import tkinter as tk
from tkinter import messagebox

BUFFER_SIZE = 1024

# Function to start the client
def start_client():
    try:
        # Get the server details from the user input fields
        server_ip = server_ip_entry.get()
        server_port = int(server_port_entry.get())
        
        # Create the socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        
        # Get the message from the user input field
        message = message_entry.get()
        
        # Send the message to the server
        client_socket.send(message.encode('utf-8'))
        
        # Receive the server's response
        response = client_socket.recv(BUFFER_SIZE).decode('utf-8')
        
        # Display the response in the response label
        response_label.config(text=f"Server responded: {response}")
        
        # Close the connection
        client_socket.close()
    
    except Exception as e:
        messagebox.showerror("Error", f"Error in client: {e}")

# Create the main window for the client GUI
root = tk.Tk()
root.title("Client GUI")

# Set the window size
root.geometry("400x300")

# Label and input for server IP address
server_ip_label = tk.Label(root, text="Server IP address:")
server_ip_label.pack(pady=10)
server_ip_entry = tk.Entry(root, width=30)
server_ip_entry.pack(pady=5)

# Label and input for server port
server_port_label = tk.Label(root, text="Server Port:")
server_port_label.pack(pady=10)
server_port_entry = tk.Entry(root, width=30)
server_port_entry.pack(pady=5)

# Label and input for the message to send
message_label = tk.Label(root, text="Message to send:")
message_label.pack(pady=10)
message_entry = tk.Entry(root, width=30)
message_entry.pack(pady=5)

# Button to send the message to the server
send_button = tk.Button(root, text="Send Message", command=start_client)
send_button.pack(pady=20)

# Label to display the server's response
response_label = tk.Label(root, text="Server responded: ", wraplength=350)
response_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
