from django.http import Http404
from django.shortcuts import render
from django.template.defaulttags import register
from lxml import etree as ET

# Create your views here.
#
def index(request):

    tparams = {

    }
    return render(request, "index.html", tparams )
# All the players
def players(request):
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
        query= '//Player[Position="{}"]'.format(arg)

    # Retorna os jogadores de cada equipa
    elif 'Club' in request.GET:
        arg = request.GET['Club']
        query = '//Player[Club="{}"]'.format(arg)

    # Retorna os jogadores de cada nacionalidade
    elif 'Nationality' in request.GET:
        arg = request.GET['Nationality']
        query = '//player[Nationality="{}"]'.format(arg)

    ps = tree.xpath(query)
    for p in ps:
        images[p.find('Player_Name').text] = p.find('Photo').text
        rates[p.find('Player_Name').text] = p.find('Overall').text
        ages[p.find('Player_Name').text] = p.find('Age').text
        heights[p.find('Player_Name').text] = p.find('.//Height').text
        weights[p.find('Player_Name').text] = p.find('.//Weight').text
        positions[p.find('Player_Name').text] = p.find('Position').text

    tparams = {
        'prates': rates, #ordenar os jogadores por overall
        'images':images,
        'pages': ages,
        'pheights':heights,
        'pweights':weights,
        'ppos':positions,
    }

    return render(request, "players.html", tparams)

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
    fn = "app/data/players.xml"
    tree = ET.parse(fn)

    if not 'Player_Name' in request.GET:
        raise Http404('Jogador não existe!!')

    arg = request.GET['Player_Name']
    print(arg)
    pname = "//Player[Player_Name='{}']".format(arg)
    name = tree.find(pname)
    print(name)
    info = dict()


    # guarda redes tem dados na carta diferentes aos restantes jogadores
    if name.find('.//Position').text == 'GK':
        info['REF'] = name.find('.//GKReflexes').text
        info['POS'] = name.find('.//GKPositioning').text
        info['HEC'] = name.find('.//GKDiving').text
        info['TMP'] = name.find('.//SprintSpeed').text
        info['ABS'] = name.find('.//GKKicking').text
        info['BSI'] = name.find('.//GKHandling').text

    # restantes jogadores
    else:
        info['PAS'] = name.find('.//Passing').text
        info['SHO'] = name.find('.//Shooting').text
        info['PAC'] = name.find('.//').text
     #   info['DRI'] = name.find('.//Dribbling').text
        info['DEF'] = name.find('.//Defending').text
        info['PHY'] = name.find('.//Physicality').text

    print(info)
    tparams = {
        'details': info,
        'name':arg
    }
    return render(request, "detailsplayer.html", tparams)

# Retorna todas as equipas existentes
def allClubs(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = './/Club'

    # Retorna todos os clubes dessa liga
    if 'League' in request.GET:
        arg = request.GET['League']
        query = '//Player[League="{}"]'.format(arg)

    clubs = tree.xpath(query)
    info = []
    for c in clubs:
        if c.find('Club').text not in info:
            info.append(c.find('Club').text)
    print(info)
    tparams = {
        'clubs': info
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
    print(info)

    tparams = {
        'leagues': info
    }
    return render(request, "allLeagues.html", tparams)
# Retorna todos os Paises
def allCountries(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = './/Nationality'
    countries = tree.xpath(query)
    #todos as ligas
    info = []
    for c in countries:
        if c.text not in info:
            info.append(c.text)
    print(info)

    tparams = {
        'countries': info
    }
    return render(request, "allCountries.html", tparams)

@register.filter
def get_item(dict, key):
    return dict.get(key)
