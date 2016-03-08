#!/usr/bin/perl

use strict;
use CGI::Session;
require utf8;

#
## Questo file contiene le funzioni per generare le parti comuni di codice html, gestendo un semplice sistema di
## templating dove è posibile applicare piccole variazioni a seconda della pagina (per evitare link circolari, etc)
#

# Funzione per generare l'intestazione html e il contenuto del tag head (e aprire il tag body)
sub start_html(){
  # E' possibile variare il title, la description e le keywords da inserire nei tag meta.
	my($title, $description, $keywords);
	$title=$_[0];
	$description=$_[1];
	$keywords=$_[2];
  return <<"HTML";
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
  <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta http-equiv="Content-Script-Type" content="text/javascript" />
    <meta name="author" content="Franco Berton, Filippo Carnovalini, Alberto Ferrara, Varotto Mattia" />
    <meta name="language" content="italian it"/>
    <title>$title</title>
    <meta name="title" content="$title" />
    <meta name="description" content="$description" />
    <meta name="keywords" content="$keywords" />
    <link type="text/css" rel="stylesheet" href="../css/style.css" media="handheld, screen" />
    <link type="text/css" rel="stylesheet" href="../css/print.css" media="print" />
		<link type="text/css" rel="stylesheet" href="../css/small.css" media="handheld, screen and (max-width:480px), only screen and (max-device-width:480px)" />
		<link type="text/css" rel="stylesheet" href="../css/aural.css" media="aural, speech" />
		<script type="text/javascript" src="../js/jquery.min.js"></script>
		<script type="text/javascript" src="../js/scripts.js"></script>
		<link rel="icon" type="image/png" href="../img/favicon-32x32.png"/>
  </head>
  <body>
HTML
}

# Funzione per generare l'header visibile agli utenti
sub header(){
	# Nel logo c'è un link alla home: tenerne conto nel programmare la home. (il controllo non viene effettuato qui!)
  my $header = <<"HTML";
  <div id='header'>
    <a href="./home.cgi" id="ancoraLogo"><img id="logo" src="../img/logo.png" alt="logo della copisteria Berton"/></a><!-- home.cgi -->
		<h1 class='h1title'>Copisteria Berton</h1>
		<p class="reader"><a href="#nav">Vai alla navigazione</a> <a href="#content">Vai ai contenuti</a></p>
	</div>
HTML
  return $header;
}

# Funzione per generare il breadcrumb
sub breadcrumb(){
  my $breadcrumb = $_[0];
	my $cgi = new CGI();
  my $code = <<"HTML";
  <div id='breadcrumb'>
		<hr />
		<p>Ti trovi in: $breadcrumb
HTML
	my $session = CGI::Session->load() or die $!;
	if ($session->param('username') eq "admin"){
		my $name = $session->param('amministratore');
		$code .= "<span id='admin_logout'>&emsp; Hai effettuato l'accesso come \"$name\". <a href='./logout.cgi' lang='en'>Logout</a></span>";
	}
	$code .=<<"HTML";
</p>
		<hr />
  </div>
HTML
return $code;
}

# Funzione per generare il menu laterale di navigazione. Apre anche il div main
sub nav(){
	return <<"HTML";
	<div id='main'>
  <div id='nav'>
			<ul>
				<li><a href="./home.cgi" lang="en">Home</a><!-- home.cgi --></li>
				<li><a href="./servizi.cgi">I Servizi</a><!-- servizi.cgi --></li>
				<li><a href="./storia.cgi">La Storia</a><!-- storia.cgi --></li>
				<li><a href="./guestbook.cgi">Dicono di Noi</a><!-- guestbook.cgi --></li>
				<li><a href="./contatti.cgi">Contatti</a><!-- contatti.cgi --></li>
			</ul>
  </div>
HTML
}

# Funzione per aprire il div contentente il contenuto della pagina
sub start_content(){
  return "<div id='content'>";
}

# Funzione per chiudere il div contentente il contenuto e quello contentnet la parte principale della pagina.
# Include il back to top che rimanda all'inizio del breadcrumb. Andrebbe rimosso dalla pagine molto corte.
# La funzione accetta come argomento l'ultimo indice di tabindex usato nel content, in modo da mettere il corretto tabindex
sub end_content(){
	my $tab=$_[0] + 1;
  return <<"HTML";
	<p class="backToTop"><span class="reader"><a href="#nav">Vai alla navigazione</a></span> <a href="#content" tabindex="$tab">&uarr;Torna su<span class="reader"> ai contenuti</span></a></p>
	</div> <!-- id='content' -->
</div> <!-- id='main'-->
HTML
}

# Funzione per generare il footer delle pagine
sub footer(){
	# Il footer include tre link: le pagine relative dovranno eliminarli per evitare link circolari.
  return <<'HTML';
  <div id='footer'>
		<p>&copy; Copisteria Berton</p>
		<p>Via Giovanni Verga, 25 - 35125 Padova - Telefono: 049 9789876 - <span lang="en">Fax</span>: 049 9485784 - <span lang="en">E-mail</span>: <a href="mailto:info@berton.com">info@berton.com</a></p>
		<p id="link_footer"><a href="./cookie.cgi">Informativa <span lang="en">Cookie</span></a><!-- cookie.cgi --> - <a href="./mappa.cgi">Mappa del Sito</a><!-- mappa.cgi --> - <a href="./login.cgi">Amministrazione</a><!-- login.cgi --></p>
  </div>
HTML
}

# Funzione per generare la fine delle pagine html (chiusura tag body e html)
sub end_html(){
  return <<'HTML';
  </body>
  </html>
HTML
}

# Devo ritornare true
1
