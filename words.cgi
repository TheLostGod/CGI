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


QUERY_STRING="www.csun.edu/~steve/"

#echo "$(dirname $SERVER_NAME$REQUEST_URI)"


#the working sed
#tr '        \n' '  ' | sed -e "s/  */ /g" -e 's/<[^>]*a[^>]*>\([^<]*\)<\/a>/\1/g' -e "s/<[^>]*>/_/g" -e "s/\([a-zA-Z0-9(),'.:;+-][ a-zA-Z0-9(),'.:;+-]*\)/\|\1\|/g" | tr '\|_' '\n\n'

var=$(curl "www.csun.edu/~steve/" 2&>1)

#| /usr/bin/tr '        \n' '  ' |

echo $var
echo "<!DOCTYPE html>"
echo "<head>"
echo "<title>Paragraph</title>"
echo "<link rel="stylesheet" type="text/css" href="style.css">"
echo "<script src="words.js"></script>"
echo "</head>"
echo "<body><canvas id=\"c\">$var</canvas></body>"
echo "</html>"

exit 0
