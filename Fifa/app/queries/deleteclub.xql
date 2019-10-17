let $d := doc('players')/players
for $e in $d//player//club[club_name/text()="FC Barcelona"]
return delete node $e 


