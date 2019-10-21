let $c := doc('FIFA')/Players/Player/Country
for $p in distinct-values($c/Nationality/text()) order by $p
for $f in $c
  where $f/Nationality/text() = $p
    
  return
  <Country>
    <Flag>{$f/Flag}</Flag>
    <Nationality>{$p}</Nationality>
  </Country> 
  
