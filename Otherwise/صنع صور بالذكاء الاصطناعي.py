import requests,uuid,webbrowser,os; os.system('cls' if os.name == 'nt' else 'clear')
G1 = '\x1b[1;92m\x1b[38;5;46m'
G2 = '\x1b[1;92m\x1b[38;5;50m'
G3 = '\x1b[38;5;196m'
G4 = '\x1b[1;92m\x1b[38;5;210m'
G5 = '\x1b[38;5;90m'
G6 = '\x1b[38;5;93m'
G7 = '\x1b[1;92m\x1b[38;5;212m'
G8 = '\x1b[1;92m\x1b[38;5;208m'
G9 = '\x1b[38;5;123m'
while True:
    T = input(f'{G2}[ {G1}YOU {G2}] {G3}- {G4}Enter Text {G5}> {G6}')
    he = {'Host': 'api.getimg.ai','Accept': 'application/json','Authorization': 'Bearer key-3XbWkFO34FVCQUnJQ6A3qr702Eu7DDR1dqoJOyhMHqhruEhs22KUzR7w631ZFiA5OFZIba7i44qDQEMpKxzegOUm83vCfILb','Content-Type': 'application/json','User-Agent': 'okhttp/4.12.0','Connection': 'keep-alive',}
    js = {'height': 1024,'model': 'realvis-xl-v4','negative_prompt': 'nude, naked, porn, sexual, explicit, adult, sex, xxx, erotic, blowjob, masturbation, intercourse, hentai, vulgar, profane, obscene, dirty, slut, whore, rape, fetish, gangbang, threesome, stripper, escort,','prompt': f'{T}','response_format': 'url','seed': 0,'steps': 30,'width': 1024,}
    res = requests.post('https://api.getimg.ai/v1/stable-diffusion-xl/text-to-image',headers=he,json=js).json()
    print(res)
    if 'url' in res and res['url']:
        webbrowser.open(res['url'])
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(f"{G7}[ {G8}Image {G7}] {G3}- {G9}error")
