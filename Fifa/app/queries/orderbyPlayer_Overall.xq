module namespace funcs = "com.funcs.my.index";
declare namespace map = "http://www.w3.org/2005/xpath-functions/map";

declare function funcs:orderbyPlayer_Overall() as node() {
  <Player>{
     for $c in doc('FIFA')/Players/Player
      order by number($c/Overall) 
      return
        <Player_Name>{$c/Player_Name/text()}</Player_Name>
  }</Player>
};

