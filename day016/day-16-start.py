from prettytable import PrettyTable
table = PrettyTable()
table.add_column("pokemen name", ["pichu", "goldduck", "floette"])
table.add_column("type", ["electric", "water", "fairy"])
table.header_style = "upper"
table.align = "l"

print(table)