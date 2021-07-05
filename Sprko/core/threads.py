
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def pool(workers, lst, func):
	with ThreadPoolExecutor(max_workers=int(workers)) as executor:
		results = executor.map(func, lst)

# threads().poolBar(2000, array, function)
def poolBar(workers, lst, func):
	with ThreadPoolExecutor(max_workers=int(workers)) as executor:
		results = list(tqdm(executor.map(func, lst), total=len(lst))) #range(len(lst))