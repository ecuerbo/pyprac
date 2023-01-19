from rich.tree import Tree
from rich import print as rprint

tree = Tree("Family Tree")
tree.add("Mom").add("[red]Stepdad")
tree.add("Dad")
tree.add("Bro").add("Wife")
tree.add("[red]Sis").add("[green]Husband").add("[blue]Son")

rprint(tree)