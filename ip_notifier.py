import socket
import time

def get_ip_address():
    """Return the current IP address of the computer."""
    try:
        # Create a temporary socket, connect to a remote server, and get the local IP address.
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Set a timeout for the socket
            s.settimeout(0.1) 
            # Google's DNS server
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
        return ip_address
    except Exception as e:
        print("Error getting IP address:", str(e))
        return None

def main():
    """Main Function."""
    # Get the initial IP address.
    current_ip_address = get_ip_address()

    if current_ip_address:
        print("Initial IP address:", current_ip_address)
    else:
        return

    # Start a loop to check for IP address changes.
    while True:
        # Get the new IP address.
        new_ip_address = get_ip_address()

        if new_ip_address:
            # If the IP address has changed, print it to the console.
            if current_ip_address != new_ip_address:
                print("IP address changed to:", new_ip_address)
                current_ip_address = new_ip_address
        else:
            print("Failed to retrieve IP address.")

        # Wait for 1 second before checking for IP address changes again.
        time.sleep(1)

if __name__ == "__main__":
    main()