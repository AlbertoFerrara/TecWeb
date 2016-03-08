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
print &start_html("Storia - Copisteria Berton","Storia della Copisteria Berton, dal 1993 a oggi","storia, copisteria, Berton, 1993");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Storia');
#Richiamo funzione per codice HTML della barra laterale di navigazione
my $nav = &nav();
#elimino il link circolare dalla navigazione
$nav =~ s/<a href=".\/storia.cgi">//;
$nav =~ s/<\/a><!-- storia.cgi -->//;
print $nav;
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
print<<HTML;
		   <h2>Storia</h2>
		   <div id="immagine" class="table-cell">
		   	 <img class="immagine-principale" src="../img/copisteria.jpg" alt="foto della sede della copisteria"/>
		   </div>
			<div class="table-cell">
		   		<p>La <strong>Copisteria Berton</strong> nasce nel <em>1993</em> come semplice negozio di fotocopie.</p>
				<p>Dopo breve tempo, la Copisteria Berton si paleserà come una delle <em>attività più affermate di Padova</em> nel campo della legatoria e copisteria.</p>
				<p>La passione e la visione del futuro nel settore ci ha portato ad investire in macchinari e professionalità per dare ai nostri clienti un servizio sempre più <em>preciso e puntuale.</em></p>
				<p>Grazie ai nostri macchinari, sempre aggiornati, garantiamo una velocità e una qualità unica, che ci rende il <strong>centro stampe più efficace del nostro paese.</strong></p>
				<p>La nostra elevata professionalità ha come obiettivo quello di mantenere un rapporto di reciproca fiducia e stima con la clientela.</p>
			</div>
HTML
##Richiamo funzione per codice HTML di chiusura content
print &end_content(0);
#Richiamo funzione per codice HTML footer
print &footer();
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
