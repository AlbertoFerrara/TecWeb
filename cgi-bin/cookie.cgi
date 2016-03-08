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
print &start_html("Informativa Cookie - Copisteria Berton","Uso dei cookie sul sito della Copisteria Berton","cookie, copisteria, Berton");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Informativa sull\'uso dei <span lang="en">cookie</span>');
#Richiamo funzione per codice HTML della barra laterale di navigazione
print &nav();
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Stampo il contenuto
print<<"HTML";
		   <h2>Informativa estesa sui <span lang="en">Cookie</span></h2>
		   <p>
INFORMATIVA <span lang='en'>COOKIE</span> ai sensi dell’art. 13 del D. Lgs. n. 196/2003
Copisteria Berton s.r.l, Titolare del trattamento dei dati personali, informa
ai sensi dell’art. 13 del D. Lgs .n. 196/2003 (Codice <span lang='en'>privacy</span>), che questo sito <span lang="en">internet</span> fa uso di <span lang='en'>cookie</span>.
L’informativa è resa solo per il presente sito e non per altri siti <span lang='en'>web</span>
eventualmente consultati o comunque acceduti dall’utente tramite <span lang='en'>link</span> che potrebbero essere presenti in questo sito.
I <span lang='en'>cookie</span> sono file di testo che contengono pacchetti di informazioni che vengono
memorizzati nella directory del <span lang='en'>browser</span> <span lang='en'>web</span> sul computer o sul dispositivo mobile (ad es.
  <span lang="en">notebook, tablet, smartphone</span>, ecc.) dell’utente tutte le volte che si visita un sito <span lang="en">online</span>
attraverso un <span lang='en'>browser</span>. Ad ogni successiva visita il <span lang='en'>browser</span> invia questi <span lang='en'>cookie</span>s al sito
<span lang='en'>web</span> che li ha originati o ad un altro sito. I <span lang='en'>cookie</span> permettono ai siti di ricordare alcune
informazioni per consentire all’utente di navigare <span lang="en">online</span> in modo semplice e veloce.
Un <span lang='en'>cookie</span> non può richiamare nessun altro dato dal disco fisso dell’utente né trasmettere
virus informatici o acquisire indirizzi <span lang="en">email</span>. Ogni <span lang='en'>cookie</span> è unico per il <span lang='en'>web browser</span> dell’utente.
Tecnologie similari, come ad esempio, <span lang='en'>web beacon</span>, GIF trasparenti, sono utilizzabili per
raccogliere informazioni sul comportamento dell'utente e sull'utilizzo dei servizi. Nel
seguito di tale informativa si farà riferimento ai <span lang='en'>cookie</span> e a tutte le tecnologie similari
utilizzando semplicemente il termine “<span lang='en'>cookie</span>”.
</p>
<p>
La disciplina relativa all’uso dei <span lang='en'>cookie</span> è stata recentemente modificata a seguito dell’attuazione
della direttiva 2009/136 che ha modificato la direttiva <span lang='en'>“e-Privacy”</span> (2002/58/CE) e del provvedimento
del Garante per il trattamento dei dati personali “Individuazione delle modalità semplificate per
l’informativa e l’acquisizione del consenso per l’uso dei <span lang='en'>cookie</span> – 8 maggio 2014”.
Esistono varie tipologie di <span lang='en'>cookie</span>, alcuni per rendere più efficace l’uso del sito e migliorare
l’esperienza di navigazione dell’utente, altri per abilitare funzionalità particolari.
</p>
<p>
Si possono trovare maggiori informazioni sui <span lang='en'>cookie</span> ai seguenti indirizzi:
</p>
<ul>
<li><a href='http://it.wikipedia.org/wiki/Cookie' lang='en' tabindex="1">http://it.wikipedia.org/wiki/Cookie</a></li>
<li><a href='http://www.allaboutcookies.org' lang='en' tabindex="2">http://www.allaboutcookies.org</a> - (in inglese)</li>
</ul>

<h3>Tipologie di <span lang='en'>Cookie</span> utilizzati</h3>
  <p>
In questo sito <span lang="en">internet</span> vengono utilizzati solo <span lang='en'>cookie</span> tecnici, cioè quelli utilizzati al solo fine
di “effettuare la trasmissione di una comunicazione su una rete di comunicazione elettronica, o nella
misura strettamente necessaria al fornitore di un servizio della società dell’informazione esplicitamente
richiesto dall’abbonato o dall’Utente a erogare tale servizio” (cfr. art. 122, comma 1, del Codice <span lang='en'>privacy</span>).
Per l’installazione di tali <span lang='en'>cookie</span> non è richiesto il preventivo consenso degli utenti, mentre resta fermo
l’obbligo di dare l’informativa ai sensi dell’art. 13 del Codice. L’acquisizione e il trattamento dei dati
derivanti dall’utilizzo dei <span lang='en'>cookie</span> tecnici è obbligatorio per la consultazione del sito. In caso di opposizione
da parte dell’utente non sarà possibile la visione completa e corretta del sito.
</p>
<p>
Esclusi i <span lang='en'>cookie</span> tecnici, la regola generale per “l’archiviazione delle informazioni nell’apparecchio
terminale di un contraente o di un utente o l’accesso a informazioni già archiviate” resta quella del
consenso preventivo e informato dell’utente (c.d. opt- in).
Ciò vuol dire che tutti i <span lang='en'>cookie</span> non qualificabili come “tecnici” che presentano peraltro maggiori
criticità dal punto di vista della protezione della sfera privata degli utenti, come ad esempio,
quelli usati per finalità di profilazione, non possono essere installati sui terminali degli utenti
stessi se questi non siano stati prima adeguatamente informati e non abbiano prestato al riguardo un valido consenso.
Questo sito non utilizza <span lang='en'>cookie</span> di profilazione.
Questo sito non utilizza nemmeno <span lang='en'>cookie</span> di terze parti, ovvero gestiti da altri siti.
</p>
<h3>Come gestire i <span lang='en'>cookie</span> mediante configurazione del <span lang='en'>browser</span></h3>
<p>
Indicazioni precise su come disattivare i <span lang='en'>cookie</span> su tutti i principali <span lang='en'>browser</span> si trovano al seguente <span lang='en'>link</span>:
<a href='http://it.wikihow.com/Disattivare-i-Cookies' tabindex="3">Come disattivare i <span lang='en'>cookie</span></a>
</p>
<h3>Diritti degli interessati</h3>
<p>
I soggetti cui si riferiscono i dati personali hanno diritto in qualsiasi momento di ottenere
la conferma o meno dell’esistenza dei medesimi dati e di conoscere il contenuto e l’origine, verificare
l’esattezza degli stessi o chiederne l’aggiornamento, l’integrazione oppure la rettifica (art. 7 del Codice <span lang='en'>privacy</span>).
Ai sensi del medesimo articolo si ha diritto di chiederne la cancellazione, la trasformazione in forma anonima
o il blocco dei dati trattati in violazione di legge nonché di opporsi in ogni caso per motivi legittimi al loro trattamento.
Le richieste vanno rivolte ai contatti presenti nella pagina dei Contatti.
Questa pagina è visibile, mediante <span lang='en'>link</span> in calce in tutte le pagine del Sito (eccetto la presente) ai
sensi dell’art. 122 secondo comma del D.lgs. 196/2003 e a seguito delle modalità
semplificate per l’informativa e l’acquisizione del consenso per l’uso dei <span lang='en'>cookie</span> pubblicata
sulla Gazzetta Ufficiale n.126 del 3 giugno 2014 e relativo registro dei provvedimenti n.229 dell’8 maggio 2014.
</p>
HTML
##Richiamo funzione per codice HTML di chiusura content
print &end_content(3);
#Richiamo funzione per codice HTML footer
my $footer = &footer();
#elimino i link circolari
$footer =~ s/<a href=".\/cookie.cgi">//;
$footer =~ s/<\/a><!-- cookie.cgi -->//;
print $footer;
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
