# library covered in lab 1
import socket
# library covered in lab 3
import hashlib

# Lab 1 code
# Function: Connecting to the server on port 5555. the port I used in Lab 1.
# Security Purpose: Initiating the stateful TCP connection required for connecting to the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

# Lab 1 code
# Function: Asks for the username and sends it to the server using the HELLO command.
# Security Purpose: Sending the username in plaintext first so the server knows exactly who to generate the random challenge token for.
username = input("Enter username: ")
client.send(f"HELLO|{username}".encode())

# Lab 3 code
# Function: Receiving the challenge token from the server.
# Security Purpose: As said in Part C: After receiving this random token it will mix with our password, so our final hash is different every time to prevent malicous attackers to gain access.
response = client.recv(1024).decode()
parts = response.split('|', 1)

if parts[0] == "CHALLENGE":
    challenge_token = parts[1]

    # Function: Asks the user for their password and OTP.
    # Security Purpose: Getting the credentials locally through the console to process them without sending them over the internet in plaintext.
    password = input("Enter password: ")
    otp = input("Enter 6-digit OTP: ")

    # Lab 3 code
    # Function: Hashing the password first, then hashing it again with the token.
    # Security Purpose: The server only stores our hash not the password in plaintext, we hash the password first to match the database and then combine it with the token to prove we are legit.
    pass_hash = hashlib.sha256(password.encode()).hexdigest()
    final_hash = hashlib.sha256((pass_hash + challenge_token).encode()).hexdigest()

    # Lab 3 code
    # Function: Sends the final hash and the OTP code to the server.
    # Security Purpose: The payload is sent safely because it does not include the password only the hash. The data is pipe delimited to prevent parsing errors on the server.
    client.send(f"AUTH|{final_hash},{otp}".encode())

    # Lab 1 code
    # Function: Printing the final server response.
    # Security Purpose: Verifying if the authentication handshake was successful or if the server dropped the connection due to invalid credentials.
    final_response = client.recv(1024).decode()
    print(final_response)

client.close()
