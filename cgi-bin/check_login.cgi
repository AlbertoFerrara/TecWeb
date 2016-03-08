#!/usr/bin/perl

use strict;
#includo questa direttiva per vedere gli errori sul browser
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
use Digest::SHA qw(sha256_hex);
require utf8;

require ('./template.cgi');

my $cgi = new CGI();

# lettura dati dal Post
my $user = $cgi->param('Username');
# La password deve passare attraverso alla stessa funzione di hash con la quale è stata salvata nel database
my $pass_input = sha256_hex($cgi->param('Password'));

# Carica la sessione
my $session = CGI::Session->load() or die $!;
# Se non esiste...
if ( $session->is_expired() || $session->is_empty() ) {

# apertura database
my $file = "./xml/DatabaseAmministratori.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

# recupero della password
my $pass_salvata = $doc->findvalue("/amministratori/amministratore[username=\"$user\"]/password");

# Se non è stata recuperata una password è perché l'utente non è trovato sul database.
if (!$pass_salvata){
	# Utente non registrato
	print redirect(-url=>'./login.cgi?error=1');
}
else{
	#La password non corrisponde
	if($pass_salvata ne $pass_input){
		print redirect(-url=>'./login.cgi?error=2');
	}
	else{
		#Login andato, creo sessione e passo a admin.cgi
		    my $session = new CGI::Session(undef, undef, {Directory=>'/tmp'});
			$session->param("amministratore", $user);
		    print $session->header(-location=>'./admin.cgi');
	    }
    }
}
