#!/usr/bin/perl

use strict;
require utf8;
use CGI qw(:standard);
#includo questa direttiva per vedere gli errori sul browser
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use Time::Piece;
use XML::LibXML;
use Encode;
require ('./template.cgi');
require ('./funzioni.pl');



my $cgi = new CGI();
my $error_fields = $cgi->url_param('error_fields');
my $name = encode("utf-8",$cgi->param('Nome'));
my $email = encode("utf-8",$cgi->param('Email'));
my $text = encode("utf-8",$cgi->param('Testo'));
my $id_to_del = $cgi->param('id_comment_delete');
my $tab=0;




# Provo a caricare la sessione
my $session = CGI::Session->load() or die $!;

print "Content-type: text/html\n\n";

#Richiamo funzione per codice HTML header
print &start_html("Dicono di Noi - Copisteria Berton","Lascia un commento sulla Copisteria Berton","dicono di noi,commenti,copisteria,Berton,guestbook");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Dicono di Noi');
#Richiamo funzione per codice HTML della barra laterale di navigazione
my $nav = &nav();
#elimino il link circolare dalla navigazione
$nav =~ s/<a href=".\/guestbook.cgi">//;
$nav =~ s/<\/a><!-- guestbook.cgi -->//;
print $nav;
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto




if (($cgi->param('Submit') && $name ne "" && $email ne "" && $text ne "") or ($cgi->param('deleteButton') && $session->param('username') eq "admin") ) {

my $datetime = localtime();



# apertura database dei commenti
my $file = "./xml/DatabaseCommenti.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

my $root = $doc->getDocumentElement;

my @commenti = $doc->findnodes("/commenti/commento");

if ($cgi->param('Submit')) {

# Inserisco il nuovo commento nel file DatabaseCommenti.xml
my $commento = XML::LibXML::Element->new('commento');

my $nomeuser = XML::LibXML::Element->new('nome');
$nomeuser->appendText( &sanitizza($name) );
$commento->appendChild($nomeuser);


my $emailuser = XML::LibXML::Element->new('email');
$emailuser->appendText( &sanitizza($email) );
$commento->appendChild($emailuser);

my $testouser = XML::LibXML::Element->new('testo');
$testouser->appendText( &sanitizza($text) );
$commento->appendChild($testouser);

my $dataora = XML::LibXML::Element->new('dataora');
$dataora->appendText($datetime);
$commento->appendChild($dataora);


if (@commenti) {
	my $commentoInTesta = @commenti[0];
	my $idTesta = $doc->findvalue('commenti/commento[1]/id_commento/text()');
	my $idCommento = XML::LibXML::Element->new('id_commento');
	$idCommento->appendText( $idTesta + 1 );
	$commento->appendChild($idCommento);
	$root->insertBefore($commento,$commentoInTesta);
}
else {
	my $idCommento = XML::LibXML::Element->new('id_commento');
	$idCommento->appendText( 1 );
	$commento->appendChild($idCommento);
	$root->appendChild($commento);
}

print "<h3>Commento inserito correttamente</h3>
<a href='./guestbook.cgi' tabindex='1'>Torna al Dicono di Noi</a>";
$tab=1;
}
else {


my @comments = $root->findnodes("/commenti/commento[id_commento= $id_to_del]");
$root->removeChild(@comments[0]);

print "<h3>Commento eliminato correttamente</h3>
<a href='./guestbook.cgi' tabindex='1'>Torna al Dicono di Noi</a>";
$tab=1;
}
# scrittura su file
open(OUT,">$file") or die $!;
print OUT $doc->toString;
close(OUT);


}
else {

print<<"HTML";
<h2>Dicono di Noi</h2>
	<div id="scrivi_commento">
		<h3>Lascia un commento</h3>
		<p id="inizioForm"><em>-Tutti i campi sono obbligatori</em><br/><!-- errore_caratteri --></p>
		<form class='form_con_testo' action="./guestbook.cgi#inizioForm" method="post">

HTML
		my $form_new_commento=qq(
		<p>
		<span>
		    <label id="name" for="Nome">Nome <br/><!-- errore_nome --></label>
		    <input id="Nome" type="text" name="Nome" value="$name" tabindex='1'/>
				</span>
				<span>
		    <label id="email" for="Email"><span lang="en">Email</span> (non sarà mostrata) <br/><!-- errore_email --> <!-- errore_REemail --></label>
		    <input id="Email" type="text" name="Email" value="$email" tabindex='2'/>
				</span>
		</p>
		<p>
		    <label id="testo" for="Testo">Testo <br/><!-- errore_testo --></label>
		    <textarea id="Testo" rows='6' cols='55' name="Testo" tabindex='3'>$text</textarea>
		</p>
		<p>
		    <input type="submit" class="pulsante" value="Commenta" name="Submit" tabindex='4' onclick="return validaFormNewCommento()"/>
		</p>   );
		if ($cgi->param('Submit')) {
			if ($name eq "") {$form_new_commento =~ s/<!-- errore_nome -->/<span class="error">Nome obbligatorio <\/span>/;}
			if ($email eq "") {$form_new_commento =~ s/<!-- errore_email -->/<span class="error"><span lang="en">Email<\/span> obbligatoria <\/span>/;}
			else {if ($email !~ /^[^@]+@+[^\.]+\.+[^\.]+$/) {$form_new_commento =~ s/<!-- errore_REemail -->/<span class="error"><span lang="en">Email<\/span> non valida <\/span>/;}}
			if ($text eq "") {$form_new_commento =~ s/<!-- errore_testo -->/<span class="error">Testo obbligatorio <\/span>/;}
		}
		print $form_new_commento;
		$tab = 4;
print<<"HTML";


		</form>
	</div>
	<div id="lista_Commenti">
HTML

# apertura database dei commenti
my $file = "./xml/DatabaseCommenti.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

my $root = $doc->getDocumentElement;

		my @nodes = $doc->findnodes("/commenti/commento");

		my $count = @nodes;

		print "<p id='num_commenti'><strong>Sono presenti $count commenti!</strong></p>";


		foreach my $comment (@nodes) {
			my $id = $comment->findnodes("./id_commento");
			my $nome = $comment->findnodes("./nome");
			my $testo = $comment->findnodes("./testo");
			my $mail = $comment->findnodes("./email");
			my $time_string = $comment->findnodes("./dataora")->string_value();
			my $time = Time::Piece->strptime($time_string,'%a %b %d %H:%M:%S %Y');
			my $time_modified = $time->strftime('%d-%m-%y alle ore %X');
			my $commento_da_stampare=<<"COMMENT";
             			<div class="commento" >
					<div class="commento_dati">
    		 				<h4>$nome</h4>

									<p>$testo</p>
									<p>$time_modified</p>

COMMENT
				if ($session->param('username') eq "admin") {
					$commento_da_stampare =~ s/<div class="commento_dati">/<div class="commento_dati_admin">/;
					my $commentotab= $tab + 1;
					$tab= $tab+1;
					$commento_da_stampare .=<<"COMMENT";
				<p><a href="mailto:$mail">$mail</a></p>
				</div> <!-- dati commento -->
					<div class="commento_delete">

						<form action="./guestbook.cgi" method="post">
						<div>
						<input type="submit" class="pulsante" value="Elimina" name="deleteButton" tabindex='$commentotab'/>
						<input type="hidden" value="$id" name="id_comment_delete"/>
						</div>
						</form>
					</div>
COMMENT
print $commento_da_stampare;
			}else{
				print $commento_da_stampare;
				print "</div> <!-- dati commento -->"
			}
		print "</div> <!-- commento -->";}

	print "</div> <!-- lista commenti -->";
}





##Richiamo funzione per codice HTML di chiusura content
print &end_content($tab);
#Richiamo funzione per codice HTML footer
print &footer();
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
