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
require ('./funzioni.pl');

my $cgi = new CGI();

#Leggo dati dal POST
my $user = $cgi->param('Username');
my $pwd = $cgi->param('Password');
my $cpwd = $cgi->param('ConfermaPassword');

my $cgi = new CGI();

# Provo a caricare la sessione
my $session = CGI::Session->load() or die $!;
# Se non esiste...
if ( $session->is_expired() || $session->is_empty() ) {
	print redirect(-url=>'./admin.cgi');
}
#se la sessione è definita, quindi procedo con il controllo campi
else{
	if($user eq ''){
		print redirect(-url=>'./admin.cgi?erroradmin=1#content');
	}
	else{
		if($pwd eq ''){
			print redirect(-url=>'./admin.cgi?erroradmin=2#content');
		}
		else{
			if($cpwd eq '' || $cpwd ne $pwd){
				print redirect(-url=>'./admin.cgi?erroradmin=3#content');
			}
			else{
				#Se arrivo qui tutti i dati sono definiti in modo corretto, inserisco on XML
				my $file = "./xml/DatabaseAmministratori.xml";
				# creazione oggetto parser
				my $parser = XML::LibXML->new();

				# apertura file e lettura input
				my $doc = $parser->parse_file($file);

				# estrazione radice
				my $root = $doc->getDocumentElement;
				# array degli elementi username
				my @username = $root->getElementsByTagName('username');

				# controllo che l'username fornito non sia presente nell'array
				# variabile di controllo
				my $trovato = 0;

				# controllo che l'useremail della form registrazione sia presente nel file
				for my $u (@username){
				  $u = $u->to_literal();
				  if($user eq $u){ # l'username è gia presente
				    $trovato = 1;
    				last;
  				  }
				}
				if($trovato){
					#admin esiste già, lo segnalo
					print redirect(-url=>'./admin.cgi?erroradmin=4#content');
				}
				else{
					# Inserisco il nuovo utente nel file utenti.xml
    				my $amministratore = XML::LibXML::Element->new('amministratore');

    				my $admin = XML::LibXML::Element->new('username');
						# sanitare qui è precauzionale, l'utente dovrebbe sapere già che non può usare certi caratteri
    				$admin->appendText(&sanitizza($user));
    				$amministratore->appendChild($admin);

    				my $adminP = XML::LibXML::Element->new('password');
						my $hash = sha256_hex($pwd);
						# non serve sanitare grazie all'hashing.
    				$adminP->appendText($hash);
    				$amministratore->appendChild($adminP);

    				$root->appendChild($amministratore);

					# scrittura su file
					open(OUT,">$file") or die $!;
					print OUT $doc->toString;
					close(OUT);

					print redirect(-url=>'./admin.cgi?done=1#content');
				}

			}
		}
	}

}
