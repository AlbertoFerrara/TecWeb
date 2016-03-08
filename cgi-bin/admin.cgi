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

my $erroradmin = $cgi->param('erroradmin');
my $admin = $cgi->param('amministratore');
my $adddone = $cgi->param('done');
my $tab=0;
# Provo a caricare la sessione
my $session = CGI::Session->load() or die $!;
$session->param('username',"admin");
# Se non esiste...
if ( $session->is_expired() || $session->is_empty() ) {
	  print redirect(-url=>'./login.cgi');
}
#la sessione esiste
else{
	print "Content-type: text/html\n\n";

	#Richiamo funzione per codice intestazione HTML
	print &start_html("Amministrazione - Copisteria Berton","Parte di amministrazione del sito della Copisteria Berton","Amministrazione, Copisteria, Berton");
	#Richiamo funzione per codice HTML header
	print &header();
	#Richiamo funzione per codice HTML breadcrumb
	print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Amministrazione');
	#Richiamo funzione per codice HTML della barra laterale di navigazione
	print &nav();
	#Richiamo funzione per codice HTML di apertura content
	print &start_content();
	#Stampo il contenuto
my $var=<<'HTML';
		   <h3>Inserimento nuovo amministratore</h3>
			 <p id="inizioForm"><em>-Tutti i campi sono obbligatori</em><br/><!-- errore_caratteri --></p>
		   	<form action="./add_admin.cgi" id="new_admin_form" class="form_semplice">
		   	<p><label for="Username" id="user" lang="en">Username <br/><!-- errore_username_esiste --><!-- errore_username --></label>
		   		<input type="text" id="Username" name="Username" tabindex="3"/>
				</p>
		   	<p>
					<label for="Password" id="pwd" lang="en">Password <br/><!-- errore_password --></label>
		   		<input type="password" id="Password" name="Password" tabindex="4"/>
				</p>
				<p>
		   		<label for="ConfermaPassword" id="cpwd">Conferma <span lang="en">Password</span> <br/><!-- errore_conferma_password --></label>
		   		<input type="password" id="ConfermaPassword" name="ConfermaPassword" tabindex="5"/>
				</p>
				<p>
		   		<input type="submit" id="invia" value="Invia" class="pulsante" onclick="return validaFormNewAdmin()" tabindex="6"/>
				</p>
		  </form>
HTML
#Errore username non corretto
if($erroradmin == 1){
$var =~ s/<!-- errore_username -->/<span class="error"><span lang="en">Username<\/span> obbligatorio <\/span>/;
}
else{
	#Errore password obbligatoria
	if($erroradmin == 2){
		$var =~ s/<!-- errore_password -->/<span class="error"><span lang="en">Password<\/span> obbligatoria <\/span>/;
	}
	else{
	#Errore conferma password non inserita o non corrisponde
	if($erroradmin == 3){
		$var =~ s/<!-- errore_conferma_password -->/<span class="error">Le <span lang="en">Password<\/span> non corrispondono <\/span>/;
	}
	else{
		#Errore uname già esistente
		if($erroradmin == 4){
			$var =~ s/<!-- errore_username_esiste -->/<span class="error"><span lang="en">Username<\/span> già esistente, usarne un altro <\/span>/;
			}
		else{
			if($adddone == 1){
			print <<"HTML";
			<h3>Inserimento avvenuto correttamente</h3>
			 <a href='./admin.cgi' tabindex='1' >Torna alla pagina di amministrazione</a>
HTML
$tab=1;
			}
		}
	}
  }
}
if($adddone != 1){
print<<HTML;
		<h2>Amministrazione</h2>
		<p><strong>Da questa pagina puoi solo inserire nuovi amministratori.</strong></p>
		<p>Se vuoi modificare o aggiungere servizi vai alla
			<a href="./servizi.cgi" tabindex="1">pagina dei servizi</a>, e se vuoi moderare i commenti vai alla pagina del
		<a href="./guestbook.cgi" tabindex="2">Dicono di Noi</a>.</p>
		$var

HTML
$tab= 6;
}


#Qui vado a inserire l'inserimento di un nuovo admin (form) e modifica prezzi

	##Richiamo funzione per codice HTML di chiusura content
	print &end_content($tab);
	#Richiamo funzione per codice HTML footer
	my $footer = &footer();
	#elimino i link circolari
	$footer =~ s/<a href=".\/login.cgi">//;
	$footer =~ s/<\/a><!-- login.cgi -->//;
	print $footer;
	#Richiamo funzione per codice di chiusura file HTML
	print &end_html();
}
