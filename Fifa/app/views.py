from django.http import Http404
from django.shortcuts import render
from lxml import etree as ET

# Create your views here.
# All the players
def players(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = '//Player'
    ps = tree.xpath(query)
    info = []
    for p in ps:
        info.append(p.find('Player_Name').text)

    tparams = {
        'players': info,
    }

    return render(request, "players.html", tparams)

# Retorna todas as posições
def allPositions(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    query = './/Position'
    ps = tree.xpath(query)
    info = []
    for g in ps:
        if g.text not in info:
            info.append(g.text)
    tparams = {
        'positions': info
    }
    return render(request, "allpositions.html", tparams)

# Retorna todos os jogadores da posição selecionada
def getPosition(request):
    fn = "app/data/fifa.xml"
    tree = ET.parse(fn)
    arg = request.GET['Position']
    pposi = '//Player[Position="{}"]'.format(arg)
    ps = tree.xpath(pposi)
    info = []
    for p in ps:
        info.append(p.find('Player_Name').text)
    tparams = {
        'players': info
    }
    return render(request, "players.html", tparams)

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

    for d in name:
        info['Passing'] = name.find('.//Passing').text
        info['Shooting'] = name.find('.//Shooting').text
        info['Speed'] = name.find('.//Speed').text
        info['Handling'] = name.find('.//Handling').text
        info['Defending'] = name.find('.//Defending').text
        info['Physicality'] = name.find('.//Physicality').text


    print(info)
    tparams = {
        'details': info,
    }
    return render(request, "detailsplayer.html", tparams)

# Detalhes de cada jogador
#def detailsPlayer(request):
#    fn = "app/data/fifa.xml"
#    tree = ET.parse(fn)
#    query = '//Player'
#    det = tree.xpath(query)
#
#    return render(request, "detailsplayer.html", tparams)