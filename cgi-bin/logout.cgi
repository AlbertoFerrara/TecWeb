#!/usr/bin/perl

use strict;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use CGI::Cookie;
require utf8;

# controllo se la sessione esiste
my $session = CGI::Session->load() or die $!;

my $name = $session->param('amministratore');

# cancellazione della sessione
$session->close();
$session->delete();
$session->flush();

# cancellazione del cookie creato con la sessione
my $cgi = new CGI;
my $cookie = $cgi->cookie(-name => $session->name, -value => '-1', -expires => '-1d');

print header(-cookie => $cookie);

# Pagina di redirect
print <<EOF;

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="refresh" content="0; URL=./home.cgi" />
		<title>Loading</title>
	</head>
	<body/>
</html>
EOF
