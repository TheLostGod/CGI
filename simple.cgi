#!/bin/bash

# This is a little CGI program
###################################################################
# The following are environment variables that are available to you
#
# CONTENT_TYPE:      The desired MIME type for the response.
# CONTENT_LENGTH:    The length of the query information.
# GATEWAT_INTERFACE: Currently CGI/1.1
# HTTP_HOSR_AGENT:   Information about the requesting client.
# QUERY_STRING:      The query string.
# REQUEST_METHOD:    The method used to make the request. 
# REQUEST_URI:       The URI of the request.
# SERVER_PROTOCOL:   Currently “HTTP/1.1”.

# SCRIPT_FILENAME:   The full path to the CGI script.
# SCRIPT_NAME:       The name (i.e., URI) of the CGI script.
# SERVER_NAME:       The server's hostname or IP Address.
# SERVER_PORT:       The port of the server.

# Add a content type and a blank line
echo "X-COMP-490: ${USER}"
echo "Content-type: text/html"
echo ""
echo `/usr/bin/curl -s www.csun.edu/~steve/ | sed -i "s#</head>#hello\n</head>#"`

exit 0
