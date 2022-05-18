import logging
from http.server import HTTPServer, BaseHTTPRequestHandler
from ddtrace import patch_all, tracer

# Explicitly tell the tracer to instrument all modeules it supports.
patch_all()

loggingFormat = "%(asctime)s | %(levelname)s | %(message)s"
logging.basicConfig(level=logging.DEBUG, format=loggingFormat)


class httpHandler(BaseHTTPRequestHandler):
    # Decorate the method since http.server is not automatically instrumented. A flask
    # application (or a Django one) would not require decorators.
    @tracer.wrap()
    def do_GET(self):
        logging.info("Received GET request")
        self.send_response(200, "OK")
        self.send_header("content-type", "text/html")
        self.end_headers()


def main():
    port = 8899
    server_addr = ("", port)
    server = HTTPServer(server_addr, httpHandler)
    logging.info("Server started")
    server.serve_forever()


if __name__ == "__main__":
    main()
