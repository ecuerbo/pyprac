from rich.progress import track
from time import sleep

def process_data():
    sleep(0.01)
    
for _ in track(range(1000),description='[green]Processing data'):
    process_data()