#!/usr/bin/perl

use strict;
require utf8;
use CGI qw(:standard);
#includo questa direttiva per vedere gli errori sul browser
use CGI::Carp qw(fatalsToBrowser);

require ('template.cgi');

my $cgi = new CGI();
print "Content-type: text/html\n\n";

#Richiamo funzione per codice intestazione HTML
print &start_html("Mappa del Sito - Copisteria Berton","Mappa del sito della Copisteria Berton","Mappa, Copisteria, Berton");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Mappa del Sito');
#Richiamo funzione per codice HTML della barra laterale di navigazione
print &nav();
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
print<<HTML;
		   <h2>Mappa del Sito</h2>
		   <ul>
		   		<li><a href="./home.cgi" lang="en" tabindex="1">Home</a></li>
					<li><a href="./servizi.cgi" tabindex="2">Servizi</a></li>
					<li><a href="./storia.cgi" tabindex="3">Storia</a></li>
					<li><a href="./guestbook.cgi" tabindex="4">Dicono di noi</a></li>
		   		<li><a href="./contatti.cgi" tabindex="5">Contatti</a></li>
		   		<li>Mappa del Sito</li>
		   		<li><a href="./cookie.cgi" tabindex="6">Informativa <span lang="en">Cookie</span></a></li>
					<li><a href="./login.cgi" tabindex="7">Amministrazione</a></li>

HTML

print "</ul>";

##Richiamo funzione per codice HTML di chiusura content
print &end_content(7);
#Richiamo funzione per codice HTML footer
my $footer = &footer();
#elimino i link circolari
$footer =~ s/<a href=".\/mappa.cgi">//;
$footer =~ s/<\/a><!-- mappa.cgi -->//;
print $footer;
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
