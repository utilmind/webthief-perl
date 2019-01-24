#!/usr/bin/perl
#                Get Header Perl CGI script
#                --------------------------
#          File: getheader.cgi
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


# Description: This script receives the header of file (specified by url
#              address) from web and output it in html format.
#
#       Usage: cgi-bin/getheader.cgi?urladdress
#
#
#   Example 1: cgi-bin/getheader.cgi?www.utilmind.com
#   Example 2: cgi-bin/getheader.cgi?www.utilmind.com/utilmind/scripts/download/counter.zip

require 'httpget.lib';

print "Content-type: text/html\n\n";

$query = $ENV{'QUERY_STRING'};         # Getting parameter

$head = &HTTP_GET_HEADER($query);
@HEAD = split(/\n/, $head);

foreach $line (@HEAD) {
  print "$line<br>";
}
