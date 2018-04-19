from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi
import numpy as np


hostName = "localhost"
hostPort = 9000

class StoreHandler(BaseHTTPRequestHandler):
    def do_POST(self):

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        gre_score = float(form['gre'].value)
        gpa_score = form['gpa'].value
        rank_score = form['rank'].value

        min_max_file = "min_max.npy"
        theta_file = "theta_bin.npy"

        theta = np.load(theta_file)
        min_max = np.load(min_max_file)
        x_data = np.array([gre_score,gpa_score, rank_score], dtype=np.float32)

        x_data_rescale = (x_data - min_max[0]) / (min_max[1] - min_max[0])
        x_data_rescale = np.insert(x_data_rescale, 0, 1)

        def sigmoid(z):
            return 1 / (1 + np.exp(z))

        def hypothesis_function(x, theta):
            z = (np.dot(-x, theta))
            return sigmoid(z)

        h_result = hypothesis_function(x_data_rescale, theta)
        print(h_result)
        print(theta)

        result_set = h_result > 0.5

        if result_set == True:
            result = ("Get Admission!!")
        else:
            result = ("Fail")

        self.respond(result.encode())

    def do_GET(self):
        response = b"""
<!DOCTYPE html>
<html lang="en">

<body>
    <p>Check your admission status!</p>
    <form method="post">
        <p>gre: <input type="text" name="gre"></p>
        <p>gpa: <input type="text" name="gpa"></p>
        <p>rank: <input type="text" name="rank"></p>
        <p><input type="submit" value="submit"></p>
    </form>
</body>
</html>
        """

        self.respond(response)

    def respond(self, response, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)


myServer = HTTPServer((hostName, hostPort), StoreHandler)
print(time.asctime(), "Server Starts - %s:%s"    % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))