let $d := doc('FIFA')/Players
for $e in $d/Player/Club[Club_Name/text()="FC Barcelona"]
return delete node $e 


