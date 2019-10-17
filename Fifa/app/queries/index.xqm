module namespace funcs = "com.funcs.my.index";
declare namespace map = "http://www.w3.org/2005/xpath-functions/map";

declare function funcs:orderbyPlayer_Name() as node() {
  <Player>{
  for $c in doc('FIFA')/Players/Player
  order by ($c/Player_Name)
    return
      <Player_Name>{$c/Player_Name/text()}</Player_Name>
  }</Player>
};

declare function funcs:orderbyPlayer_Overall() as node() {
  <Player>{
     for $c in doc('FIFA')/Players/Player
      order by number($c/Overall) descending
      return
        <Player_Name>{$c/Player_Name/text()}</Player_Name>
  }</Player>
};

declare updating function funcs:deleteClub($clubName) {
  let $d := doc('FIFA')/Players
  for $e in $d/Player/Club[Club_Name/text()=$clubName]
    return delete node $e 
};


