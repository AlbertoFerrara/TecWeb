#!/usr/bin/perl

use strict;
require utf8;

#
## Questo file è pensato per le funzioni di utilità da richiamare in più file che però non riguardino la struttura html.
#

## Questa funzione serve per eliminare caratteri potenzialmente dannosi per xml, da usare per sanitare
## l'input di utenti che deve essere salvato su database

sub sanitizza(){
  my $testo=$_[0];
  $testo =~ s/<//g;
  $testo =~ s/>//g;
  $testo =~ s/;//g;
  return $testo;
}
