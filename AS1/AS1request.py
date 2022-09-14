class Request:

    # convert a string into bytes: string.encode()

    # host, path, query have type string
    def getRequest(self, host, path, query) -> bytearray:
        """Build an HTTP GET request """
        self.request = bytearray()
        self.request += b'GET ' + path.encode() + query.encode() + b' HTTP/1.0' +  b'\nHost: ' + host.encode() + b'\nConnection: close\n\n'
        return self.request

    # host has type string
    def headRequest(self, host) -> bytearray:
        """Build a HEAD request, to check if host has "robots.txt" file """
        self.request = bytearray()
        self.request += b'HEAD /robots.txt HTTP/1.1\n' + b'Host: ' + host.encode() + b'\nConnection: close\n\n'#
        return self.request