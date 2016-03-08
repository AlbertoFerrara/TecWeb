#!/usr/bin/perl

use strict;
require utf8;
#includo questa direttiva per vedere gli errori sul browser
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);
use CGI::Session;
use XML::LibXML;

require ('./template.cgi');
require ('./funzioni.pl');

my $tab=0;
my $cgi = new CGI();

# Provo a caricare la sessione
my $session = CGI::Session->load() or die $!;

print "Content-type: text/html\n\n";

#Richiamo funzione per codice HTML header
print &start_html("Servizi - Copisteria Berton","Servizi offerti e listino prezzi della Copisteria Berton","servizi, prezzi, copisteria, Berton");
#Richiamo funzione per codice HTML header
print &header();
#Richiamo funzione per codice HTML breadcrumb
print &breadcrumb('<a href="./home.cgi" lang="en">Home</a> &gt; Servizi Offerti');
#Richiamo funzione per codice HTML della barra laterale di navigazione
my $nav = &nav();
#elimino il link circolare dalla navigazione
$nav =~ s/<a href=".\/servizi.cgi">//;
$nav =~ s/<\/a><!-- servizi.cgi -->//;
print $nav;
#Richiamo funzione per codice HTML di apertura content
print &start_content();
#Lettura file xml
my $file = "./xml/DatabasePrezzi.xml";

# creazione oggetto parser
my $parser = XML::LibXML->new();

# apertura file e lettura input
my $doc = $parser->parse_file($file);

if (($cgi->param('inserisci_servizio') && $cgi->param('new_nome') && $cgi->param('new_descrizione') && $cgi->param('new_prezzo'))  || $cgi->param('elimina') || ($cgi->param('conferma_modifica') && $cgi->param('edit_nome') && $cgi->param('edit_descrizione') && $cgi->param('edit_prezzo'))){
			if ($cgi->param('elimina')){
			# nodo da eliminare
			    my @nodes= $doc->findnodes("//prodotto[id_prodotto=".$cgi->param('id')."]");
			# verifica nodo trovato
			    if (@nodes){
			# eliminazione
			    $nodes[0]->unbindNode();
			# salvataggio
			    $doc->toFile("./xml/DatabasePrezzi.xml");
			    print "<h3>Eliminazione avvenuta correttamente</h3>
				   <a href='./servizi.cgi' tabindex='1'>Torna alla pagina dei servizi</a>";
				 $tab=1;
			 }
			    else{
				print "<h3>Eliminazione già avvenuta correttamente</h3>
				   <a href='./servizi.cgi' tabindex='1'>Torna alla pagina dei servizi</a>";
				 $tab=1;
			 }
			}
			if ($cgi->param('conferma_modifica')){
			# nodo da modificare
			    my @nodes= $doc->findnodes("//prodotto[id_prodotto=".$cgi->param('id')."]");
			    my $modifcaavvenuta=0;
			# modifica dati
			    if ($nodes[0]->findvalue("nome") ne $cgi->param('edit_nome')){
				my ($nomedamodificare)=$nodes[0]->findnodes("nome");
		 		    $nomedamodificare->removeChildNodes();
		 		    $nomedamodificare->appendText(&sanitizza($cgi->param('edit_nome')));
		 		    $modifcaavvenuta = 1;}
			    if ($nodes[0]->findvalue("descrizione") ne $cgi->param("edit_descrizione")){
				my ($descrizionedamodificare)=$nodes[0]->findnodes("descrizione");
		 		    $descrizionedamodificare->removeChildNodes();
		 		    $descrizionedamodificare->appendText(&sanitizza($cgi->param("edit_descrizione")));
		 		    $modifcaavvenuta = 1;}
			    if ($nodes[0]->findvalue("prezzo") ne $cgi->param('edit_prezzo')){
				my ($prezzodamodificare)=$nodes[0]->findnodes("prezzo");
		 		    $prezzodamodificare->removeChildNodes();
		 		    $prezzodamodificare->appendText(&sanitizza($cgi->param('edit_prezzo')));
		 		    $modifcaavvenuta = 1;}
			# salvataggio solo se modifica avvenuta
			    if ($modifcaavvenuta==1){
			    	$doc->toFile("./xml/DatabasePrezzi.xml");
				 print "<h3>Modifica avvenuta correttamente</h3>
					<a href='./servizi.cgi' tabindex='1'>Torna alla pagina dei servizi</a>";
					$tab=1;
			     }
			    else
				{print "<h3>Modifica non Avvenuta</h3>
					<a href='./servizi.cgi' tabindex='1'>Torna alla pagina dei servizi</a>";
				$tab=1;
			}
			}
			if ($cgi->param('inserisci_servizio')){
			    # estrazione radice
			    my $root = $doc->getDocumentElement;

			    my $prodotto = XML::LibXML::Element->new('prodotto');

    			    my $lastprodotto = $doc->findvalue("//prodotto[last()]/id_prodotto/text()");

			    my $id_prodotto = XML::LibXML::Element->new('id_prodotto');
    			       $id_prodotto->appendText($lastprodotto+1);
    			       $prodotto->appendChild($id_prodotto);

    			    my $nome = XML::LibXML::Element->new('nome');
    			       $nome->appendText(&sanitizza($cgi->param('new_nome')));
   			       $prodotto->appendChild($nome);

			    my $descrizione = XML::LibXML::Element->new('descrizione');
    			       $descrizione->appendText(&sanitizza($cgi->param('new_descrizione')));
   			       $prodotto->appendChild($descrizione);

			    my $descrizione = XML::LibXML::Element->new('prezzo');
    			       $descrizione->appendText(&sanitizza($cgi->param('new_prezzo')));
   			       $prodotto->appendChild($descrizione);
			    $root->appendChild($prodotto);

			    $doc->toFile("./xml/DatabasePrezzi.xml");
			    print "<h3>Inserimento avvenuto correttamente</h3>
				   <a href='./servizi.cgi' tabindex='1'>Torna alla pagina dei servizi</a>";
					 $tab=1;
			}
	}
#Stampo il contenuto

else	{

	print<<HTML;
<div id="pannelloServizi">
<div id="introServizi">
				<h2>I Nostri Servizi</h2>
				<p>Da più di vent’anni nel settore, offriamo al cliente qualità e precisione eccellenti nei servizi di: </p>
			</div>

<div id="sezionericerca">
	<h3>Ricerca tra i Servizi <span class="reader">(necessita di Javascript)</span></h3>
	<p id="noscript">Attiva Javascript sul tuo browser per filtrare gli annunci</p>
</div>
</div>
HTML

$tab=3;


	#Se la sessione esiste, do la possibilità di inserire un nuovo servizio
	     if ( !$session->is_expired() && !$session->is_empty())
		{
			$tab=7;
		print "<div id='inserisci_prodotto'><h3>Inserisci Nuovo Servizio</h3><p id='inizioForm'><em>-Tutti i campi sono obbligatori</em><br/><!-- errore_caratteri --></p>";
		my $form_new_servizio = qq(<form class='form_con_testo' method='post' action='#inizioForm'>
			<p>
			<span>
			<label id='l_nome' for='new_nome'>Nome <br/><!-- errore_nome --></label>
		   	<input type='text' name='new_nome' id='new_nome' tabindex='4'/>
				</span>
				<span>
			<label id='l_prezzo' for='new_prezzo'>Prezzo <br/><!-- errore_prezzo --></label>
		   	<input type='text' name='new_prezzo' id='new_prezzo' tabindex='5'/>
				</span>
			</p>
			<p>
			<label id='l_descrizione' for='new_descrizione'>Descrizione <br/><!-- errore_descrizione --> </label>
			<textarea rows='6' cols='55' name='new_descrizione' tabindex='6' id='new_descrizione'></textarea>
			</p>
			<p>
		        <input type='submit' value='Inserisci Servizio' tabindex='7' class="pulsante" name='inserisci_servizio' onclick='return validaFormNewProdotto()'/>
			</p>
		      </form></div>);
		if (!$cgi->param('new_nome') && $cgi->param('inserisci_servizio')){
			$form_new_servizio =~ s/<!-- errore_nome -->/<span class="error">Nome obbligatorio <\/span>/;}
		else{
			my $new_nome=$cgi->param('new_nome');
			$form_new_servizio =~ s/name='new_nome'/name='new_nome' value='$new_nome'/;}
		if (!$cgi->param('new_descrizione') && $cgi->param('inserisci_servizio') ){
			$form_new_servizio =~ s/<!-- errore_descrizione -->/<span class="error">Descrizione obbligatoria <\/span>/;}
		else{
			my $new_descrizione=$cgi->param('new_descrizione');
			$form_new_servizio =~ s/id='new_descrizione'>/id='new_descrizione'>$new_descrizione/;}
		if (!$cgi->param('new_prezzo') && $cgi->param('inserisci_servizio') ){
			$form_new_servizio =~ s/<!-- errore_prezzo -->/<span class="error">Prezzo obbligatorio<\/span>/;}
		else{
			my $new_prezzo=$cgi->param('new_prezzo');
			$form_new_servizio =~ s/name='new_prezzo'/name='new_prezzo' value='$new_prezzo'/;}
		print $form_new_servizio;
	}

		#stampa informazioni prodotti
		my @nodes=$doc->findnodes("//prodotto");
		print "<ul id='lista_servizi'>";
		my $i=1;

		for  my $node (@nodes){
		    if ($node->findvalue('id_prodotto')==$cgi->param('id') && !$cgi->param('annulla_modifica')){
			my $nometab= $tab +1;
			my $descrizionetab= $tab +2;
			my $prezzotab= $tab +3;
			my $annullatab= $tab +5;
			my $submittab= $tab +4;
			$tab= $tab +5;
			my $edit_id=$cgi->param('id');
			my $form_edit_prodotto = qq(<li id='prodotto_n_$edit_id' class='servizio'>
			<p id='inizioEditForm'><!-- errore_caratteri --></p>
				   <form method='post' class='azioni_servizio' action='#inizioEditForm'><div>
				     <label id='l_edit_nome' for='edit_nome'>Nome <br/><!-- errore_nome --></label>
				     <input type='text' name='edit_nome' id='edit_nome' tabindex='$nometab'/>
				     <label id='l_edit_descrizione' for='edit_descrizione'>Descrizione <br/><!-- errore_descrizione --></label>
			    	     <textarea rows='6' cols='18' name='edit_descrizione' tabindex='$descrizionetab' id='edit_descrizione'></textarea>
				     <label id='l_edit_prezzo' for='edit_prezzo'>Prezzo <br/><!-- errore_prezzo --></label>
			    	     <input type='text' name='edit_prezzo' id='edit_prezzo' tabindex='$prezzotab'/>
				     <input type='hidden' value='$edit_id' name='id'/>
				     <input type='submit' class='pulsante' value='annulla' tabindex='$annullatab' name='annulla_modifica'/>
				     <input type='submit' class='pulsante' value='conferma' tabindex='$submittab' name='conferma_modifica' onclick="return validaFormEditProdotto()" />
				   </div></form>
				   </li>);
			if ($cgi->param('modifica')){
				my $edit_nome=$node->findvalue('nome');
				my $edit_descrizione=$node->findvalue('descrizione');
				my $edit_prezzo=$node->findvalue('prezzo');
				$form_edit_prodotto =~ s/id='edit_nome'/id='edit_nome' value='$edit_nome'/;
				$form_edit_prodotto =~ s/id='edit_descrizione'>/id='edit_descrizione'>$edit_descrizione/;
				$form_edit_prodotto =~ s/id='edit_prezzo'/id='edit_prezzo' value='$edit_prezzo'/;
			  }

			if ($cgi->param('conferma_modifica') && (!$cgi->param('edit_nome') || !$cgi->param('edit_descrizione') || !$cgi->param('edit_prezzo')))	{
			    my $edit_nome=$cgi->param('edit_nome');
			    my $edit_descrizione=$cgi->param('edit_descrizione');
			    my $edit_prezzo=$cgi->param('edit_prezzo');
			   if ($cgi->param('edit_nome')){
				$form_edit_prodotto =~ s/<input type='text' name='edit_nome'/<input type='text' value='$edit_nome' name='edit_nome'/;      }
			   else{
				$form_edit_prodotto =~ s/<!-- errore_nome -->/<span class="error">Nome obbligatorio <\/span>/;}
			   if ($cgi->param('edit_descrizione')) {
				$form_edit_prodotto =~ s/id='edit_descrizione'>/id='edit_descrizione'>$edit_descrizione/;      }
			   else{
				$form_edit_prodotto =~ s/<!-- errore_descrizione -->/<span class="error">Descrizione obbligatoria <\/span>/;}
			   if ($cgi->param('edit_prezzo')){
				$form_edit_prodotto =~ s/<input type='text' name='edit_prezzo'/<input type='text' value='$edit_prezzo' name='edit_prezzo'/;      }
			   else{
				$form_edit_prodotto =~ s/<!-- errore_prezzo -->/<span class="error">Prezzo obbligatorio <\/span>/;}

			}
			 print $form_edit_prodotto;
		      }
		     else{
  			     print "<li id='prodotto_n_".$node->findvalue('id_prodotto')."' class='servizio'>
						<p class='nome_prodotto'><strong>".$node->findvalue('nome')."</strong></p>
		  	     	    <p class='descrizione_prodotto'>".$node->findvalue('descrizione')."</p>
			     	    <p class='prezzo_prodotto'>".$node->findvalue('prezzo')."</p>";

# Se la sessione esiste mostro i pulsanti per modificare e eliminare un servizio
			     if ( !$session->is_expired() && !$session->is_empty()){
						 my $eliminatab=$tab + 1;
						 my $modificatab=$tab + 2;
						 $tab = $tab + 2;
			     print "<form method='post' class='azioni_servizio'
			 	 action='#prodotto_n_".$node->findvalue('id_prodotto')."'>
				 <div>
					<input type='submit' class='pulsante noPrint' value='elimina'  name='elimina' tabindex='$eliminatab'/>
					<input type='submit' class='pulsante noPrint' value='modifica' name='modifica' tabindex='$modificatab'/>
					<input type='hidden' value='".$node->findvalue('id_prodotto')."'  name='id'/>
				  </div>  </form>";
				}
				print"</li>";
			}

		$i++;
		}
	print "</ul> <!-- lista_servizi -->";}

##Richiamo funzione per codice HTML di chiusura content
print &end_content($tab);
#Richiamo funzione per codice HTML footer
print &footer();
#Richiamo funzione per codice di chiusura file HTML
print &end_html();
