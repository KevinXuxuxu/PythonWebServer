import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    templates = {}
    templates[1] = '''\
        <html>
        <body>
        <table>
        <tr> <td>Header</td> <td>Value</td> </tr>
        <tr> <td>Request Time</td> <td>{time}</td> </tr>
        <tr> <td>Adress</td> <td>{ip}</td> </tr>
        <tr> <td>Port</td> <td>{port}</td> </tr>
        <tr> <td>Method</td> <td>{method}</td> </tr>
        <tr> <td>Path</td> <td>{path}</td> </tr>
        </table>
        </body>
        </html>
        '''

    def do_GET(self):
        page = self.create_page()
        self.send_page(page)

    def send_page(self, page):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Length', str(len(page)))
        self.end_headers()
        self.wfile.write(page)

    def create_page(self):
        values = {
        'time': self.date_time_string(),
        'ip': self.client_address[0],
        'port': self.client_address[1],
        'method': self.command,
        'path': self.path
        }
        page = self.templates[1].format(**values)
        return page

def main():
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
