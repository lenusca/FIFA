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