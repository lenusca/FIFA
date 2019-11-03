from django.http import Http404, HttpRequest
from django.shortcuts import render
from django.shortcuts import redirect
from django.template.defaulttags import register
from lxml import etree as ET
from collections import OrderedDict
import xmltodict
from BaseXClient import BaseXClient
import random
import feedparser
#from django.shortcuts import render_to_response


#import feedparser
#import webbrowser
from io import BytesIO

# Create your views here.
#
def index(request):

    # with open("app/players.xsd", 'r') as schema_file:
    #     schema_to_check = schema_file.read().encode('utf-8')
    # with open("app/players.xml", 'r') as xml_file:
    #     xml_to_check = xml_file.read().encode('utf-8')
    # xmlschema_doc = ET.parse(BytesIO(schema_to_check))
    # xmlschema = ET.XMLSchema(xmlschema_doc)
    # try:
    #     doc = ET.parse(StringIO(xml_to_check))
    #     print('XML well formed, syntax ok')
    # except IOError:
    #     print('Invalid File')
    # except ET.XMLSyntaxError as err:
    #     print('XML Syntax Error')
    # except:
    #     print('Unknown error')

    # try:
    #     xmlschema.assertValid(doc)
    #     print('XML valid, schema validation ok.')
    # except ET.DocumentInvalid as err:
    #     print('Schema validation error')
    # except:
    #     print('Unknown error, exiting')
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    if 'search' in request.POST:
        images = dict()
        rates = dict()
        positions = dict()
        ages = dict()
        heights = dict()
        weights = dict()
        player_to_be_searched = request.POST.get("search")
        try:
            input = """
                          import module namespace funcs="com.funcs.my.index" at "index.xqm";
                          funcs:showPlayersName('{}')
                          """.format(player_to_be_searched)
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()

        dres = xmltodict.parse(res)
        lres = dres['Players']['Player']
        if(isinstance(lres,dict)):
            rates[lres['Player_Name']] = lres['Overall']
            images[lres['Player_Name']] = lres['Photo']
            ages[lres['Player_Name']] = lres['Age']
            heights[lres['Player_Name']] = lres['Phisic']['Height']
            weights[lres['Player_Name']] = lres['Phisic']['Weight']
            positions[lres['Player_Name']] = lres['Position']
        else:
            for l in lres:
                rates[l['Player_Name']] = l['Overall']
                images[l['Player_Name']] = l['Photo']
                ages[l['Player_Name']] = l['Age']
                heights[l['Player_Name']] = l['Phisic']['Height']
                weights[l['Player_Name']] = l['Phisic']['Weight']
                positions[l['Player_Name']] = l['Position']

        tparams = {
            'prates': rates,
            'images': images,
            'pages': ages,
            'pheights': heights,
            'pweights': weights,
            'ppos': positions,
        }
        return render(request, 'players.html', tparams)

    tparams = {

    }
    return render(request, "index.html", tparams )

# All the players
def players2(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)
    images = dict()
    rates = dict()
    positions = dict()
    ages = dict()
    heights = dict()
    weights = dict()
    query = '//Player'
    # Retorna todos os jogadores da posição selecionada
    if 'Position' in request.GET:
        arg = request.GET['Position']
        query= '//Player[Position="{}"]'.format(arg.strip())


    # Retorna os jogadores de cada equipa
    elif 'Club' in request.GET:
        arg = request.GET['Club']
        query = '//Player[.//Club_Name="{}"]'.format(arg)

    # Retorna os jogadores de cada nacionalidade
    elif 'Nationality' in request.GET:
        arg = request.GET['Nationality']
        query = '//Player[.//Nationality="{}"]'.format(arg)

    ps = tree.xpath(query)
    for p in ps:
        images[p.find('Player_Name').text] = p.find('Photo').text
        rates[p.find('Player_Name').text] = p.find('Overall').text
        ages[p.find('Player_Name').text] = p.find('Age').text
        heights[p.find('Player_Name').text] = p.find('.//Height').text
        weights[p.find('Player_Name').text] = p.find('.//Weight').text
        positions[p.find('Player_Name').text] = p.find('Position').text


    tparams = {
        'prates': rates,
        'images':images,
        'pages': ages,
        'pheights':heights,
        'pweights':weights,
        'ppos':positions,
    }

    return render(request, "players.html", tparams)

def players(request):
    count = 0
    images = dict()
    rates = dict()
    positions = dict()
    ages = dict()
    heights = dict()
    weights = dict()
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

    if 'Position' in request.GET:
        try:
            input = """
                       import module namespace funcs="com.funcs.my.index" at "index.xqm";
                       funcs:showPlayersPosition('{}')
                       """.format(request.GET['Position'])
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()

        dres = xmltodict.parse(res)

    elif 'Nationality' in request.GET:
        try:
            input = """
                       import module namespace funcs="com.funcs.my.index" at "index.xqm";
                       funcs:showPlayersNationality('{}')
                       """.format(request.GET['Nationality'])
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()

        dres = xmltodict.parse(res)
    elif 'Choice' in request.GET:
        try:
            input = """
                       import module namespace funcs="com.funcs.my.index" at "index.xqm";
                       funcs:orderbyPlayer('{}')
                       """.format(request.GET['Choice'])
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()

        dres = xmltodict.parse(res)
    else:

        try:
            input = """
                    import module namespace funcs="com.funcs.my.index" at "index.xqm";
                    funcs:showPlayers()
                    """
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()

        dres = xmltodict.parse(res)


    if(dres['Players'] != None):
        lres = dres['Players']['Player']
        for l in lres:
            count += 1
            rates[l['Player_Name']] = l['Overall']
            images[l['Player_Name']] = l['Photo']
            ages[l['Player_Name']] = l['Age']
            heights[l['Player_Name']] = l['Phisic']['Height']
            weights[l['Player_Name']] = l['Phisic']['Weight']
            positions[l['Player_Name']] = l['Position']

            if(count == 10):
                break


    else:
        raise Http404('País sem jogador!!')

    tparams = {
        'prates': rates,
        'images': images,
        'pages': ages,
        'pheights': heights,
        'pweights': weights,
        'ppos': positions,
    }
    return render(request, 'players.html', tparams)

# Retorna todas as posições
def allPositions(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)
    query = './/Position'
    pos = tree.xpath(query)
    #todas as posições
    info = []
    for p in pos:
        if p.text not in info:
            info.append(p.text)
    tparams = {
        'positions': info
    }
    return render(request, "allpositions.html", tparams)

# Retorna os detalhes de cada jogador (detalhes que aparecem nas cartas)
def getDetails(request):
    info = dict()
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

    if not 'Player_Name' in request.GET:
        raise Http404('Jogador não existe!!')

    try:
        input = """
                import module namespace funcs="com.funcs.my.index" at "index.xqm";
                funcs:showDetails('{}')
                """.format(request.GET['Player_Name'])
        query = session.query(input)
        res = query.execute()
        query.close()
    finally:
        if session:
            session.close()
    dres = xmltodict.parse(res)
    lres = dres['Players']['Player']

    if lres['Position'] == 'GK':
        info['REF'] = lres['REF']
        info['POS'] = lres['POS']
        info['DIV'] = lres['DIV']
        info['SPE'] = lres['SPE']
        info['KIC'] = lres['KIC']
        info['HAN'] = lres['HAN']
        tparams = {
            'details': info,
            'name': lres['Player_Name'],
            'club': lres['Club_Logo'],
            'nat': lres['Flag'],
            'rat': lres['Overall'],
            'pos': lres['Position'],
            'img': lres['Photo'],
        }
        return render(request, "detailsplayerGK.html", tparams)

    else:
        info['PAS'] = lres['PAS']
        info['SHO'] = lres['SHO']
        info['PAC'] = lres['PAC']
        info['DRI'] = lres['DRI']
        info['DEF'] = lres['DEF']
        info['PHY'] = lres['PHY']
        tparams = {
            'details': info,
            'name': lres['Player_Name'],
            'name_upper': lres['Player_Name'].upper(),
            'club': lres['Club_Logo'],
            'nat': lres['Flag'],
            'rat': lres['Overall'],
            'pos': lres['Position'],
            'img': lres['Photo'],
        }
        return render(request, "detailsplayer.html", tparams)

def getDetails2(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)

    if not 'Player_Name' in request.GET:
        raise Http404('Jogador não existe!!')
    arg = request.GET['Player_Name']
    pname = "//Player[Player_Name='{}']".format(arg)
    name = tree.find(pname)
    info = dict()


    # guarda redes tem dados na carta diferentes aos restantes jogadores
    if name.find('.//Position').text == 'GK':
        info['REF'] = name.find('.//GKReflexes').text
        info['POS'] = name.find('.//GKPositioning').text
        info['DIV'] = name.find('.//GKDiving').text
        info['SPE'] = name.find('.//SprintSpeed').text
        info['KIC'] = name.find('.//GKKicking').text
        info['HAN'] = name.find('.//GKHandling').text
        tparams = {
        'details': info,
        'name': arg,
        'club': name.find('.//Club_Logo').text,
        'nat': name.find('.//Flag').text,
        'rat': name.find('Overall').text,
        'pos': name.find('Position').text,
        'img': name.find('Photo').text,
        }
        return render(request, "detailsplayerGK.html", tparams)


    # restantes jogadores
    else:
        ac = int(name.find('.//Acceleration').text)
        ss = int(name.find('.//SprintSpeed').text)
        pos = int(name.find('.//Positioning').text)
        fis = int(name.find('.//Finishing').text)
        sp = int(name.find('.//ShotPower').text)
        ls = int(name.find('.//LongShots').text)
        v = int(name.find('.//Volleys').text)
        p = int(name.find('.//Penalties').text)
        vi = int(name.find('.//Vision').text)
        cro = int(name.find('.//Crossing').text)
        accu = int(name.find('.//FKAccuracy').text)
        spa = int(name.find('.//ShortPassing').text)
        lpa = int(name.find('.//LongPassing').text)
        curve = int(name.find('.//Curve').text)
        ag = int(name.find('.//Agility').text)
        ba = int(name.find('.//Balance').text)
        re = int(name.find('.//Reactions').text)
        bc = int(name.find('.//BallControl').text)
        dr = int(name.find('.//Dribbling').text)
        co = int(name.find('.//Composure').text)
        inter = int(name.find('.//Interceptions').text)
        ha = int(name.find('.//HeadingAccuracy').text)
        defa = int(name.find('.//Marking').text)
        stac = int(name.find('.//StandingTackle').text)
        sltac = int(name.find('.//SlidingTackle').text)
        jump = int(name.find('.//Jumping').text)
        stamina = int(name.find('.//Stamina').text)
        strength = int(name.find('.//Strength').text)
        agr = int(name.find('.//Aggression').text)

        info['PAS'] = str(int((vi+cro+accu+spa+lpa+curve)/6))
        info['SHO'] = str(int((pos+fis+sp+ls+v+p)/6))
        info['PAC'] = str(int((ac+ss)/2))
        info['DRI'] = str(int((ag+ba+re+bc+dr+co)/6))
        info['DEF'] = str(int((inter+ha+defa+stac+sltac)/5))
        info['PHY'] = str(int((jump+stamina+strength+agr)/4))

    tparams = {
        'details': info,
        'name': arg,
        'club': name.find('.//Club_Logo').text,
        'nat': name.find('.//Flag').text,
        'rat': name.find('Overall').text,
        'pos': name.find('Position').text,
        'img': name.find('Photo').text,
    }
    return render(request, "detailsplayer.html", tparams)

# Retorna todas as equipas existentes
def allClubs(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)
    query = './/Club'

    # Retorna todos os clubes dessa liga
    #if 'League' in request.GET:
     #   arg = request.GET['League']
      #  query = '//Player[League="{}"]'.format(arg)

    clubs = tree.xpath(query)
    info = dict()
    for c in clubs:
        if c.find('Club_Name').text not in info and c.find('Club_Name').text != None:
            info[c.find('Club_Name').text] = c.find('Club_Logo').text
    tparams = {
        'clubs':  OrderedDict(sorted(info.items(), key=lambda x: x[0]))
    }
    return render(request, "allclubs.html", tparams)

# Retorna todas as ligas existentes
def allLeagues(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = './/League'
    leagues = tree.xpath(query)
    #todos as ligas
    info = []
    for l in leagues:
        if l.text not in info:
            info.append(l.text)

    tparams = {
        'leagues': info
    }
    return render(request, "allLeagues.html", tparams)

# Retorna todos os Paises
def allCountries(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)
    query = './/Country'
    countries = tree.xpath(query)
    #todos as ligas
    info = dict()
    for c in countries:
        if c.find('Nationality').text not in info:
            info[c.find('Nationality').text] = c.find('Flag').text
    tparams = {
        'countries': OrderedDict(sorted(info.items(), key=lambda x: x[0]))
    }
    return render(request, "allCountries.html", tparams)

# Elimina o jogador selecionado
def deletePlayer(request):
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    if 'Delete' in request.GET:
        try:
            input = """
                           import module namespace funcs="com.funcs.my.index" at "index.xqm";
                           funcs:deletePlayer('{}')
                           """.format(request.GET['Delete'])
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()
    response = redirect("/players")
    return response

# Estatisticas dos clubes
def statistics(request):
    fn = "app/data/players.xml"
    tree = ET.parse(fn)
    query1 = ".//Club"
    tover = 0
    count = 0
    media = 0
    clubs_array = []
    overall_array = []

    clubs = tree.xpath(query1)
    for c in clubs:
        if c.find('Club_Name').text not in clubs_array and c.find('Club_Name').text != None:
            clubs_array.append(c.find('Club_Name').text)
    random.shuffle(clubs_array)
    for i in clubs_array[0:10]:
        session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
        try:
            input = """
                           import module namespace funcs="com.funcs.my.index" at "index.xqm";
                           funcs:showOverallForClub('{}')
                           """.format(i)
            query = session.query(input)
            res = query.execute()
            query.close()
        finally:
            if session:
                session.close()
        dres = xmltodict.parse(res)
        lres = dres['Club']['overall']
        for o in lres:
            tover = tover + int(o)
            count = count + 1

        media = tover / count
        overall_array.append(media)


    tparams = {
       'overall': overall_array,
       'clubs': str(clubs_array[0:10]).replace("'", '"')
    }

    return render(request, "statistics.html", tparams)

def news(request):
    assert isinstance(request, HttpRequest)
    if(request.GET['select'] == 'a'):
        feed = feedparser.parse('https://www.fifa.com/rss-feeds/news')
    elif (request.GET['select'] == 'b'):
        feed = feedparser.parse('https://www.fifa.com/the-best-fifa-football-awards/rss/news')
    elif (request.GET['select'] == 'c'):
        feed = feedparser.parse('https://www.fifa.com/about-fifa/who-we-are/rss/news')
    tparams = {
        'feed': feed,
    }
    return render(request, 'news1.html',tparams)

def news1(request):

    return render(request, 'news.html')


def table(request):
    dom = "app/data/players.xml"
    xslt = "app/data/table.xsl"
    transform = ET.XSLT(xslt)
    newdom = transform(dom)

    outfile = open('app/templates/tabelas.html', 'wb')
    outfile.write(ET.tostring(transform))
    webbrowser.open_new_tab('app/templates/tabelas.html')
    return redirect('/')

@register.filter
def get_item(dict, key):
    return dict.get(key)
