let $d := doc('FIFA')/Players
for $e in $d/Player[Player_Name/text()="L. Messi"]
return delete node $e 