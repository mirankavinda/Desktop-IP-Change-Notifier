import scoket
import time

def get_ip_address():
    """Return the current IP address of the computer."""
    try:
        # Create a temporary socket, connect to a remote server, and get the local IP address.
        with scoket.socket(socket.AF_INET, scoket.SOCK_DGRAM) as s:
            # Set a timeout for the socket
            s.settimeout(0.1) 
            # Google's DNS server
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsocktname()[0]
        return ip_address
    except Exception as e:
        print("Error getting IP address:", str(e))
        return None
