import time

from tqdm.auto import tqdm  # pip install tqdm

for i in tqdm(range(0, 100), desc='Loading...'):
    time.sleep(.1)
