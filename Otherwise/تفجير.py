import os
import random
import concurrent.futures
G1 = ['Golden','Demo']
G2 = ['php', 'py', 'js', 'html', 'txt','bot','x','md']
G3 = 'مسار'
G4 = 9999
G5 = '@rrrrrf - Golden -|- Demo - @N_C_P\n' * 999
def G6(G7,G8):
    Gn = random.randint(1000,99999)
    file = os.path.join(G3, f'{G7}_{Gn}.{G8}')
    with open(file, 'w') as f:
        f.write(G5)
with concurrent.futures.ThreadPoolExecutor(max_workers=200) as executor:
    futures = []
    for _ in range(G4):
        G7 = random.choice(G1)
        G8 = random.choice(G2)
        futures.append(executor.submit(G6, G7, G8))
    for future in concurrent.futures.as_completed(futures):
        future.result()