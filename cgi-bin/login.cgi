#!/usr/bin/perl

use strict;
#includo questa direttiva per vedere gli errori sul browser
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;
require utf8;

require ('./template.cgi');

my $cgi = new CGI();

# Provo a caricare la sessione
my $session = CGI::Session->load() or die $!;
# Se non esiste...
if ( $session->is_expired() || $session->is_empty() ) {

my $error = $cgi->param('error');

print "Content-type: text/html\n\n";

#Richiamo funzione per codice HTML header
print &start_html("Login - Copisteria Berton","Sezione di amministrazione del sito della Copisteria Berton","Login,amministrazione,copisteria,Berton");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; <span lang="en">Login</span> Amministrazione');
#Richiamo funzione per codice HTML della barra laterale di navigazione
print &nav();
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
my $var=<<'HTML';
		   <h2 lang="en">Login</h2>
		   	 <form id="form_login" class="form_semplice" action="./check_login.cgi">
					<p><label for="Username" lang="en" id="user">Username <br/><!-- errore_username --></label>
		   			<input type="text" id="Username" name="Username" tabindex="1"/>
					</p>
		   		<p>	<label for="Password" lang="en" id="pwd">Password <br/><!-- errore_password --></label>
		  			<input type="password" id="Password" name="Password" tabindex="2"/>
					</p>
		  		<p>	<input type="submit" class="pulsante" id="invia" value="Invia" onclick="return validaFormLogin()" tabindex="3"/>
					</p>
		   	  </form>
HTML
#Errore username non esistente
if($error == 1){
$var =~ s/<!-- errore_username -->/<span class="error" id="errore1"><span lang="en">Username<\/span> non registrato <\/span>/;
print $var;
}
else{
	#Errore password non corretta
	if($error == 2){
		$var =~ s/<!-- errore_password -->/<span class="error" id="errore2"><span lang="en">Password<\/span> errata <\/span>/;
		print $var
	}
	else{
		#Non ci sono errori devo ancora premere invio nella form
			print $var;
		}
	}
##Richiamo funzione per codice HTML di chiusura content
print &end_content(3);
#Richiamo funzione per codice HTML footer
#elimino i link circolari
	my $footer = &footer();
	$footer =~ s/<a href=".\/login.cgi">//;
	$footer =~ s/<\/a><!-- login.cgi -->//;
	print $footer;
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
}
#La sessione esiste
else{
		print redirect(-url=>'./admin.cgi');
}
