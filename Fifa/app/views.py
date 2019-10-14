from django.http import Http404
from django.shortcuts import render
from django.template.defaulttags import register
from lxml import etree as ET

# Create your views here.
# All the players
def players(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
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

    ps = tree.xpath(query)
    for p in ps:
        print(p.find('Player_Name').text)
        rates[p.find('Player_Name').text] = p.find('Overall').text
        ages[p.find('Player_Name').text] = p.find('Age').text
        heights[p.find('Player_Name').text] = p.find('.//Height').text
        weights[p.find('Player_Name').text] = p.find('.//Weight').text
        positions[p.find('Player_Name').text] = p.find('Position').text

    tparams = {
        'prates': rates, #ordenar os jogadores por overall
        'pages': ages,
        'pheights':heights,
        'pweights':weights,
        'ppos':positions,
    }

    return render(request, "players.html", tparams)

# Retorna todas as posições
def allPositions(request):
    fn = "app/data/fifa.xml"
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
    fn = "app/data/fifa.xml"
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
        info['REF'] = name.find('.//Reflexes').text
        info['POS'] = name.find('.//Positoning').text
        info['HEC'] = name.find('.//Diving').text
        info['TMP'] = name.find('.//Speed').text
        info['ABS'] = name.find('.//Kicking').text
        info['BSI'] = name.find('.//Handling').text

    # restantes jogadores
    else:
        info['PAS'] = name.find('.//Passing').text
        info['SHO'] = name.find('.//Shooting').text
        info['PAC'] = name.find('.//Pace').text
        info['DRI'] = name.find('.//Dribbling').text
        info['DEF'] = name.find('.//Defending').text
        info['PHY'] = name.find('.//Physicality').text


    print(info)
    tparams = {
        'details': info,
    }
    return render(request, "detailsplayer.html", tparams)

# Retorna todas as equipas existentes
def allClubs(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = './/Club'
    clubs = tree.xpath(query)
    #todos os clubes
    info = []
    for c in clubs:
        if c.text not in info:
            info.append(c.text)

    tparams = {
        'clubs': info
    }
    return render(request, "allclubs.html", tparams)

@register.filter
def get_item(dict, key):
    return dict.get(key)
