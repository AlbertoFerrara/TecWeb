#!/usr/bin/perl

use strict;
require utf8;
use CGI qw(:standard);
#includo questa direttiva per vedere gli errori sul browser
use CGI::Carp qw(fatalsToBrowser);

require ('./template.cgi');

my $cgi = new CGI();
print "Content-type: text/html\n\n";

#Richiamo funzione per codice intestazione HTML
print &start_html("Copisteria Berton","Home page del sito della Copisteria Berton","index, copisteria, legatoria, Berton");
#Richiamo funzione per codice HTML header
my $header = &header();
#elimino il link circolare presente nel logo:
$header =~ s/<a href=".\/home.cgi" id="ancoraLogo">//;
$header =~ s/<\/a><!-- home.cgi -->//;
print $header;
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<span lang="en">Home</span>');
#Richiamo funzione per codice HTML della barra laterale di navigazione
my $nav = &nav();
#elimino il link circolare dalla navigazione
$nav =~ s/<a href=".\/home.cgi" lang="en">/<span lang="en">/;
$nav =~ s/<\/a><!-- home.cgi -->/<\/span>/;
print $nav;
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
print<<"HTML";
			<h2>Benvenuto!</h2>
			<p>La <strong>Copisteria Berton</strong> offre decine e decine di prodotti e servizi nell'ambito della
				<strong>stampa</strong> e della <strong>legatoria</strong> per soddisfare il bisogno di chiunque ed è senz'altro
				l'azienda più adatta alle vostre esigenze.</p>
			<p>Vieni a trovarci in <em>Via Giovanni Verga n° 25, a Padova</em>: troverai indubbiamente quello che stai cercando.</p>
			<p><a href="./servizi.cgi" id="servizi" tabindex="1">Visualizza i nostri servizi!</a></p>
HTML
##Richiamo funzione per codice HTML di chiusura content
my $end = &end_content(1);
$end =~ s/<p class="backToTop">/<p class="noDesktop backToTop">/;
print $end;
#Richiamo funzione per codice HTML footer
print &footer();
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
