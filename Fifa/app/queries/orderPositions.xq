let $c := doc('FIFA')/Players/Player
for $p in distinct-values($c/Position/text()) order by $p
  return <position>{$p}</position>
     