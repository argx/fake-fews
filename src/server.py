import threading
import webbrowser
import http.server
import http.server
import model # from ./model.py

FILE = 'frontend.html'
PORT = 8080

class ClassificationHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Handler for Facebook Chrome extension"""

    def do_POST(self):
        """Handle a POST request by parsing training example and feeding into
        model"""

        print("Client feeding us (x, y)...")

        # Grab client data
        length = int(self.headers.get_all('content-length')[0])
        data_string = str(self.rfile.read(length))
        features = data_string.split("=")[1]
        label = data_string.split("=")[3]
        print("Recieved body = '" + str(data_string) + "'") 
        print("Features = '" + str(features) + "'") 
        print("Label = '" + str(features) + "'") 

        # Train on data data 
        # TODO add to classifier
        result = "success!"

        # Write response to client
        result_bytes = str.encode(result) # bytes
        self.wfile.write(result_bytes)
        print("Sending confirmation = '" + str(result) + "'") 

        print();

    def do_GET(self):
        """Handle GET by taking input x and giving classification"""

        print("Sending client y^...")

        # Grab client data
        length = int(self.headers.get_all('content-length')[0])
        data_string = str(self.rfile.read(length))
        features = data_string.split("=")[1];
        print("Recieved body = '" + str(data_string) + "'") 
        print("Features = '" + str(features) + "'") 

        # Classify with data 
        # TODO classify example
        try:
            result = "real" 
        except:
            result = "fake"

        # Write response to client
        result_bytes = str.encode(result) # bytes
        self.wfile.write(result_bytes)
        print("Label = '" + result + "'") 

        print();

def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = http.server.HTTPServer(server_address, ClassificationHandler)
    server.serve_forever()

if __name__ == "__main__":
    #open_browser()
    start_server()
