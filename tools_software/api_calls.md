# API Calls

#### API Status Codes:
- 200 OK
- 400 Bad Request: Invalid request
- 401 Unauthorized: Your API token is missing or invalid. 
- 403 Forbidden: Your API token does not have necessary permissions. 
- 404 Not Found: The URL specified is invalid
- 406 Not Acceptable: Data upload is in incorrect format
- 500 Internal Server: Something happened on the server end
- 501 Not Implemented: Requested method not implemented???

#### Data Encryption Methods
- Hypertext Transfer Protocol (HTTP):
  - Protocol for transferring data across internet
  - Data is not encrypted or signed, devices are not authenticated
- Secure Sockets Layer (SSL):
  - Precursor to modern TLS, update to HTTP
  - Encrypted data
  - Authentication of both the user and remote devices ("handshake")
  - Data is digitally signed to record its original state (not edited upon receipt)
  - SSL/TSL can only be used by websites that obtain an SSL certificate
- Transport Layer Security (TSL):
  - The current industry standard
  - Updated version of SSL, name changed mostly due to ownership
- Websites with "https" in their name instead of "http" use SSL or TSL
- https://www.cloudflare.com/learning/ssl/what-is-ssl/

#### Creating an API Script
 - Make sure to validate the server's SSL certificate (cURL, etc.)

#### Types of Attacks?
 - Man in the Middle: uses faked SSL certificate to pose as website