module namespace funcs = "com.funcs.my.index";
declare namespace map = "http://www.w3.org/2005/xpath-functions/map";


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
          <Nationality>{$c//Nationality/text()}</Nationality>
        </Player>
        
  }</Players>
};


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
       <DIV>{$c/GKDiving/text()}</DIV>
       <SPE>{$c/ExtraDetails/SprintSpeed/text()}</SPE>
       <KIC>{$c/GKKicking/text()}</KIC>
       <HAN>{$c/GKHandling/text()}</HAN>
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

declare function funcs:showPlayersPosition($pos) as node() {
  <Players>{
     for $c in doc('FIFA')/Players/Player
     where $c/Position = $pos
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
          <Nationality>{$c//Nationality/text()}</Nationality>
        </Player>
        
  }</Players>
};

declare function funcs:showPlayersName($name) as node() {
  <Players>{
     for $c in doc('FIFA')/Players/Player
 
     where contains($c/Player_Name, $name)
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
          <Nationality>{$c//Nationality/text()}</Nationality>
        </Player>
        
  }</Players>
};

declare updating function funcs:editPlayer($name, $position, $age, $rating, $v1, $v2, $v3, $v4, $v5, $v6, $club, $height, $weight){
  for $c in doc('FIFA')/Players/Player
  where $c/Player_Name/text() = $name
  return switch ($position)
    case "GK"
      return(
     replace value of node $c/Age with $age,
     replace value of node $c/Overall with $rating,
     replace value of node $c/Club/Club_Name with $club,
     replace value of node $c//Height with $height,
     replace value of node $c//Weight with $weight,
     replace value of node $c/GKReflexes with $v1,
     replace value of node $c/GKPositioning with $v2,
     replace value of node $c/GKDiving with $v3,
     replace value of node $c//SprintSpeed with $v4,
     replace value of node $c/GKKicking with $v5,
     replace value of node $c/GKHandling with $v6)
    default
      return(
        replace value of node $c/Age with $age,
        replace value of node $c/Overall with $rating,
        replace value of node $c/Club/Club_Logo with distinct-values(funcs:showClubLogo($club)),
        replace value of node $c//Height with $height,
        replace value of node $c//Weight with $weight,
        replace value of node $c//Acceleration with $v1,
        replace value of node $c//SprintSpeed with $v1,
        replace value of node $c//Positioning with $v2,
        replace value of node $c//Finishing with $v2,
        replace value of node $c//ShotPower with $v2,
        replace value of node $c//LongShots with $v2,
        replace value of node $c//Volleys with $v2,
        replace value of node $c//Penalties with $v2,
        replace value of node $c//Vision with $v3,
        replace value of node $c//Crossing with $v3,
        replace value of node $c//FKAccuracy with $v3,
        replace value of node $c//ShortPassing with $v3,
        replace value of node $c//LongPassing with $v3,
        replace value of node $c//Curve with $v3,
        replace value of node $c//Agility with $v4,
        replace value of node $c//Balance with $v4,
        replace value of node $c//Reactions with $v4,
        replace value of node $c//BallControl with $v4,
        replace value of node $c//Dribbling with $v4,
        replace value of node $c//Composure with $v4,
        replace value of node $c//Interceptions with $v5,
        replace value of node $c//HeadingAccuracy with $v5,
        replace value of node $c//Marking with $v5,
        replace value of node $c//StandingTackle with $v5,
        replace value of node $c//SlidingTackle with $v5,
        replace value of node $c//Jumping with $v6,
        replace value of node $c//Stamina with $v6,
        replace value of node $c//Strength with $v6,
        replace value of node $c//Aggression with $v6     
    )  
};


declare function funcs:showClubLogo($club) {
     for $c in doc('FIFA')/Players/Player
     where $c/Club/Club_Name = $club
      return $c/Club/Club_Logo/text()
};



