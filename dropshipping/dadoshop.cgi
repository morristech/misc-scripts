#!/bin/sh
echo "Content-type: text/html"
echo

# Fornitore
SUPPLIER=dadoshop

# Estensione
EXT=csv

# Nome file di destinazione
DESTFILE="$SUPPLIER-elaborato.$EXT"

# Cartella destinazione Prestashop
DESTDIR="/srv/http/admin033tqfqsd/import/"

# Cartella temporanea
TMPOUT="/srv/http/upload/"

if [ "$REQUEST_METHOD" = "POST" ]; then
  cat >$TMPOUT$SUPPLIER.$EXT

  # Elaborazione specifica per fornitore   
   sed -i 's/<endrecord>/\n/g' $TMPOUT$SUPPLIER.$EXT

   sed -i 's/^/2|/' $TMPOUT$SUPPLIER.$EXT

   # Rimuovi prime righe
   tail -n +5 $TMPOUT$SUPPLIER.$EXT >$TMPOUT$SUPPLIER.$EXT.1
 
  # Rimuovi ultime righe 
   head -n -6 $TMPOUT$SUPPLIER.$EXT.1 >$TMPOUT$SUPPLIER.$EXT
   
  # Sposta in destinazione finale
   mv $TMPOUT$SUPPLIER.$EXT $DESTDIR$DESTFILE
  # Rimuovi file temporanei
   rm $TMPOUT$SUPPLIER.$EXT.1   
fi
NUMPROD=$(cat $DESTDIR$DESTFILE | wc -l)
echo "Upload completato di $SUPPLIER<br>"
echo "Caricati $NUMPROD prodotti<br>"
