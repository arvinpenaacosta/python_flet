from flet import *
 
 
def main(page:Page):
	# FOR SCROLLING PAGE
	page.scroll = "auto"
 
	# AND CREATE FAKE DATA IN YOU TABLE
	mydata = [
	{"name":"boy","age":12,"address":"new york"},
	{"name":"sam","age":12,"address":"new york"},
	{"name":"doe","age":12,"address":"new york"},
	{"name":"jaka","age":12,"address":"new york"},
	{"name":"dodo","age":12,"address":"new york"},
	{"name":"boy1","age":21,"address":"new york"},
	{"name":"sam2","age":22,"address":"new york"},
	{"name":"doe3","age":23,"address":"new york"},
	{"name":"jaka4","age":42,"address":"new york"},
	{"name":"dodo5","age":24,"address":"new york"},
 
	]
 
 
	# CREATE COLUMN OF TABLE
	colName = DataColumn(Text("name"))
	colAge = DataColumn(Text("age"))
	colAddress = DataColumn(Text("address"))
 
	# CREATE DATATABLE
	dt = DataTable(
		columns=[
		colName,
		colAge,
		colAddress
			],
		rows=[]
 
		)
 
	# AND PUSH mydata TO TABLE 
	for x in mydata:
		dt.rows.append(
			DataRow(
				cells=[
					DataCell(Text(x['name'])),
					DataCell(Text(x['age'])),
					DataCell(Text(x['address'])),
 
 
				]
 
				)
 
			)
 
 
	def showhidename(e):
		value = e.control.value
		if value == False: 
			dt.columns[0].visible = False
			page.update()
		else:
			dt.columns[0].visible = True
			page.update()
 
	def showhideage(e):
		value = e.control.value
		if value == False: 
			dt.columns[1].visible = False
			page.update()
		else:
			dt.columns[1].visible = True
			page.update()
 
	def showhideaddress(e):
		value = e.control.value
		if value == False: 
			dt.columns[2].visible = False
			page.update()
		else:
			dt.columns[2].visible = True
			page.update()
 
	# AND I CREATE CHECKBOX FOR SHOW OR HIDE YOU COLUMN
	fillName = Checkbox(label="Name",value=True,
		on_change=showhidename
 
		)
 
	fillAge = Checkbox(label="Age",value=True,
		on_change=showhideage
 
		)
 
	fillAddress = Checkbox(label="Address",value=True,
		on_change=showhideaddress
 
		)
 
 
	page.add(
	Column([
		Text("SHow/hide datatable column",size=30,
			weight="bold"
		),
		Row([
			fillName,
			fillAge,
			fillAddress
			]),
		dt
 
 
		])
 
	)
 
flet.app(target=main)