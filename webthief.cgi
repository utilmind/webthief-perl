#!/usr/bin/perl
#                Web Thief Perl CGI script
#                -------------------------
#          File: webthief.cgi
#        Author: Aleksey Kuznetsov
#     Copyright: (c) UtilMind Solutions, 1999
#           Web: http://www.utilmind.com/
#       Support: info@utilmind.com
#       Version: 1.01
# Last modified: August 12, 1999
#
# COPYRIGHT NOTICE:
#
# Copyright 1999 UtilMind Solutions. All Rights Reserved.
#
# Since 2019 published under MIT license.
#
# Selling the code for this program without prior written consent is
# expressly forbidden. Obtain permission before redistributing this
# program over the Internet or in any other medium. In all cases
# copyright and header must remain intact.
#
# =====================================================================


# Description: This script receives the file (specified by url address)
#              from web and save it to local file.
#
#       Usage: cgi-bin/webthief.cgi?urladdress=localfilename
#
#
#   Example 1: cgi-bin/webthief.cgi?www.utilmind.com=index.html
#   Example 2: cgi-bin/webthief.cgi?www.utilmind.com/utilmind/scripts/download/counter.zip=counter.zip

require 'httpget.lib';

print "Content-type: text/html\n\n";

$query = $ENV{'QUERY_STRING'};         # Getting parameters
($query, $file) = split(/=/, $query);


($head, $body) = &HTTP_GET($query);
@HEAD = split(/\n/, $head);

foreach $line (@HEAD) {
  print "$line<br>";
}

open(FILE, ">$file");
print FILE $body;
close(FILE);
