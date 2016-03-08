#!/usr/bin/perl

use strict;
require utf8;
use CGI qw(:standard);
#includo questa direttiva per vedere gli errori sul browser
use CGI::Carp qw(fatalsToBrowser);

require ('./template.cgi');

my $cgi = new CGI();
print "Content-type: text/html\n\n";

#Richiamo funzione per codice HTML header
print &start_html("Contatti - Copisteria Berton","Come trovare la copisteria Berton","Contatti, Trovarci, Indirizzo, Telefono, Chi Siamo");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Contatti');
#Richiamo funzione per codice HTML della barra laterale di navigazione
my $nav = &nav();
#elimino il link circolare dalla navigazione
$nav =~ s/<a href=".\/contatti.cgi">//;
$nav =~ s/<\/a><!-- contatti.cgi -->//;
print $nav;
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
print<<'HTML';
		   <h2>Contatti</h2>
			<div id="immagine" class="table-cell">
			<img class="immagine-principale" src="../img/mappa.png" alt="mappa che mostra la posizione della copisteria in via Verga 25 a Padova"/>
			</div>
			<div class="table-cell">
		    <h3>Come Trovarci</h3>
			<ul>
				<li><strong>Indirizzo</strong>: Via Giovanni Verga 25, Padova</li>
				<li><strong>Telefono</strong>: 049 9789876</li>
				<li><strong lang="en">Fax</strong>: 049 9485784</li>
				<li><strong lang="en">E-mail</strong>: <a href="mailto:info@berton.com" tabindex="1">info@berton.com</a></li>
			</ul>
			<h3>Chi Siamo</h3>
			<ul>
				<li><em>Berton Franco</em> - Titolare</li>
				<li><em>Carnovalini Filippo</em> - Legatoria</li>
				<li><em>Ferrara Alberto</em> - Copisteria</li>
				<li><em>Varotto Mattia</em> - Impaginazione</li>
			</ul>
			</div>


HTML
##Richiamo funzione per codice HTML di chiusura content
print &end_content(1);
#Richiamo funzione per codice HTML footer
print &footer();
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
