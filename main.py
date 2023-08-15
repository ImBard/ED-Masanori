import requests

partido = "PL"
estado = "SP"

def getAllDeputados() :
    return requests.get("https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome").json()

all = getAllDeputados()

def filterDep(dep):
    if dep["siglaPartido"] == "PL":
        return True
    else: return False

listDeps = filter(filterDep, all["dados"])

# def savePhoto(name,photo): 
#     f = open(f"./photos/{name}.png", "wb")
#     f.write(photo)


# for deputado in listDeps:
#     photo = requests.get(deputado["urlFoto"]).content
#     savePhoto(deputado["nome"], photo)


# def getValue(id):

    


def getFinalPage(id):
    href = requests.get(f"https://dadosabertos.camara.leg.br/api/v2/deputados/{id}/despesas?ordem=ASC&ordenarPor=ano").json()["links"][2]
    index = href['href'].find("pagina")
    return href[index:index+9]

print(getFinalPage("221328"))