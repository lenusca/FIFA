module namespace funcs = "com.funcs.my.index";
declare namespace map = "http://www.w3.org/2005/xpath-functions/map";

declare function funcs:orderbyPlayer_Name() as node() {
  <Players>{
  for $c in doc('FIFA')/Players/Player
  order by ($c/Player_Name)
    return
      <Player>
          <Photo>{$c/Photo/text()}</Photo>
          <Player_Name>{$c/Player_Name/text()}</Player_Name>
          <Overall>{$c/Overall/text()}</Overall>
          <Age>{$c/Age/text()}</Age>
          <Phisic>
            <Height>{$c/Phisic/Height/text()}</Height>
            <Weight>{$c/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$c/Position/text()}</Position>
        </Player>
  }</Players>
};

declare function funcs:orderbyPlayer_Overall() as node() {
  <Players>{
     for $c in doc('FIFA')/Players/Player
      order by number($c/Overall) descending
      return
        <Player>
          <Photo>{$c/Photo/text()}</Photo>
          <Player_Name>{$c/Player_Name/text()}</Player_Name>
          <Overall>{$c/Overall/text()}</Overall>
          <Age>{$c/Age/text()}</Age>
          <Phisic>
            <Height>{$c/Phisic/Height/text()}</Height>
            <Weight>{$c/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$c/Position/text()}</Position>
        </Player>
        
  }</Players>
};

(:Merge das duas funções anteriores:)
declare function funcs:orderbyPlayer($choice) as node() {
  <Players>{
      if ($choice = 'overall') then
       for $o in doc('FIFA')/Players/Player order by number($o/Overall) descending 
        return
        <Player>
          <Photo>{$o/Photo/text()}</Photo>
          <Player_Name>{$o/Player_Name/text()}</Player_Name>
          <Overall>{$o/Overall/text()}</Overall>
          <Age>{$o/Age/text()}</Age>
          <Phisic>
            <Height>{$o/Phisic/Height/text()}</Height>
            <Weight>{$o/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$o/Position/text()}</Position>
        </Player>
       else if ($choice = 'name') then
        for $n in  doc('FIFA')/Players/Player order by ($n/Player_Name)
         return 
        <Player>
          <Photo>{$n/Photo/text()}</Photo>
          <Player_Name>{$n/Player_Name/text()}</Player_Name>
          <Overall>{$n/Overall/text()}</Overall>
          <Age>{$n/Age/text()}</Age>
          <Phisic>
            <Height>{$n/Phisic/Height/text()}</Height>
            <Weight>{$n/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$n/Position/text()}</Position>
        </Player>
       else
        for $p in  doc('FIFA')/Players/Player order by ($p/Position)
         return 
        <Player>
          <Photo>{$p/Photo/text()}</Photo>
          <Player_Name>{$p/Player_Name/text()}</Player_Name>
          <Overall>{$p/Overall/text()}</Overall>
          <Age>{$p/Age/text()}</Age>
          <Phisic>
            <Height>{$p/Phisic/Height/text()}</Height>
            <Weight>{$p/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$p/Position/text()}</Position>
        </Player>
  }</Players>
};

declare function funcs:showPlayers() as node() {
  <Players>{
     for $c in doc('FIFA')/Players/Player
      return
        <Player>
          <Photo>{$c/Photo/text()}</Photo>
          <Player_Name>{$c/Player_Name/text()}</Player_Name>
          <Overall>{$c/Overall/text()}</Overall>
          <Age>{$c/Age/text()}</Age>
          <Phisic>
            <Height>{$c/Phisic/Height/text()}</Height>
            <Weight>{$c/Phisic/Height/text()}</Weight>
          </Phisic>
          <Position>{$c/Position/text()}</Position>
          <Club>
            <Club_Name>{$c/Club/Club_Name/text()}</Club_Name>
          </Club>
          <Nationality>{$c/Nationality/text()}</Nationality>
        </Player>
        
  }</Players>
};

(:mostrar os detalhes do jogador diferencia GK do resto:)
declare function funcs:showDetails($pname) as node() {
  <Players>{
     for $c in doc('FIFA')/Players/Player
     where $c/Player_Name = $pname
     return
     if ($c/Position = 'GK') then
      <Player>
       <Player_Name>{$c/Player_Name/text()}</Player_Name>
       <Photo>{$c/Photo/text()}</Photo>
       <Flag>{$c//Flag/text()}</Flag>
       <Club_Logo>{$c/Club/Club_Logo/text()}</Club_Logo>
       <Overall>{$c/Overall/text()}</Overall>
       <Position>{$c/Position/text()}</Position>
       <REF>{$c/GKReflexes/text()}</REF>
       <POS>{$c/GKPositioning/text()}</POS>
       <HEC>{$c/GKDiving/text()}</HEC>
       <TMP>{$c/ExtraDetails/SprintSpeed/text()}</TMP>
       <ABS>{$c/GKKicking/text()}</ABS>
       <BSI>{$c/GKHandling/text()}</BSI>
      </Player>
     else
      <Player>
        <Player_Name>{$c/Player_Name/text()}</Player_Name>
        <Photo>{$c/Photo/text()}</Photo>
        <Flag>{$c//Flag/text()}</Flag>
        <Club_Logo>{$c/Club/Club_Logo/text()}</Club_Logo>
        <Overall>{$c/Overall/text()}</Overall>
        <Position>{$c/Position/text()}</Position>
        <PAS>{round((($c/ExtraDetails/Vision/text())+($c/ExtraDetails/Crossing/text())+($c/ExtraDetails/FKAccuracy/text())+($c/ExtraDetails/ShortPassing/text())+($c/ExtraDetails/LongPassing/text())+($c/ExtraDetails/Curve/text())) div 6)}</PAS>
        <SHO>{round((($c/ExtraDetails/Positioning/text())+($c/ExtraDetails/Finishing/text())+($c/ExtraDetails/ShotPower/text())+($c/ExtraDetails/LongShots/text())+($c/ExtraDetails/Volleys/text())+($c/ExtraDetails/Penalties/text())) div 6)}</SHO>
        <PAC>{round((($c/ExtraDetails/Acceleration/text())+($c/ExtraDetails/SprintSpeed/text())) div 2)}</PAC>
        <DRI>{round((($c/ExtraDetails/Agility/text())+($c/ExtraDetails/Balance/text())+($c/ExtraDetails/Reactions/text())+($c/ExtraDetails/BallControl/text())+($c/ExtraDetails/Dribbling/text())+($c/ExtraDetails/Composure/text())) div 6)}</DRI>
        <DEF>{round((($c/ExtraDetails/Interceptions/text())+($c/ExtraDetails/HeadingAccuracy/text())+($c/ExtraDetails/Marking/text())+($c/ExtraDetails/StandingTackle/text())+($c/ExtraDetails/SlidingTackle/text())) div 5)}</DEF>
        <PHY>{round((($c/ExtraDetails/Jumping/text())+($c/ExtraDetails/Stamina/text())+($c/ExtraDetails/Strength/text())+($c/ExtraDetails/Aggression/text())) div 4)}</PHY>  
      </Player>
  }</Players>
};

declare updating function funcs:deleteClub($clubName) {
  let $d := doc('FIFA')/Players
  for $e in $d/Player/Club[Club_Name/text()=$clubName]
    return delete node $e 
};

declare function funcs:orderbyPositions() as node() {
  <Players>{
    let $c := doc('FIFA')/Players/Player
    for $p in distinct-values($c/Position/text()) order by $p
    return <Position>{$p}</Position>
  }</Players>
};

declare updating function funcs:deletePlayer($playerName) {
  let $d := doc('FIFA')/Players
  for $e in $d/Player[Player_Name/text()=$playerName]
  return delete node $e 
};

declare function funcs:orderbyNationality() as node() {
  <Players>{
    let $c := doc('FIFA')/Players/Player/Country
    for $x in distinct-values($c/Nationality/text()) order by $x
    return
       ($c[Nationality=$x])[1]
  }</Players>
};

declare function funcs:orderbyClub() as node() {
  <Players>{
    let $c := doc('FIFA')/Players/Player/Club
    for $x in distinct-values($c/Club_Name/text()) order by $x
    return
       ($c[Club_Name=$x])[1]
  }</Players>
};


