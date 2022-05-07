from rich.console import Console
from time import sleep

console = Console()

data = [1,2,3,4,5]
with console.status("[bold green]Fetching data...") as status:
    while data:
        num = data.pop(0)
        sleep(1)
        console.log(f"[green]Finish fetching data[/green]{num}")
        
    console.log(f'[bold][red])Done!')