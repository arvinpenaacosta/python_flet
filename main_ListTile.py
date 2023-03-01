from flet import *
 
 
def main(page:Page):
	# FOR SCROLLING PAGE
	page.scroll = "auto"
 
	# AND CREATE FAKE DATA IN YOU TABLE
	mydata = [
	{"name":"boy22","age":12,"address":"new york12"},
	{"name":"samww","age":12,"address":"new yorksfd"},
	{"name":"does","age":12,"address":"new yorks"},
	{"name":"jakasdfs","age":12,"address":"new yorkgfdg"},
	{"name":"dodosds","age":12,"address":"new yorkere"},
	{"name":"boy1sd","age":21,"address":"new yorkwerew"},
	{"name":"sam2dsd","age":22,"address":"new yorksd"},
	{"name":"doe3sd","age":23,"address":"new york"},
	{"name":"jaka4sdf","age":42,"address":"new yorksdf"},
	{"name":"dodo 5ew","age":24,"address":"new yorksd"},\
	{"name":"dodosds","age":12,"address":"new yorkere"},
	{"name":"boy1sd","age":21,"address":"new yorkwerew"},
	{"name":"sam2dsd","age":22,"address":"new yorksd"},
	{"name":"doe3sd","age":23,"address":"new york"},
	{"name":"jaka4sdf","age":42,"address":"new yorksdf"},
	{"name":"dodo 5ew","age":24,"address":"new yorksd"},
 
 
	]
  
	# CREATE COLUMN OF TABLE
	colName = DataColumn(Text("name"))
	colAge = DataColumn(Text("age"))
	colAddress = DataColumn(Text("address"))
 
	# CREATE DATATABLE
	dt = DataTable(
		data_row_color={"hovered": "0x30FF0000"},
		columns=[
		colName,
		#colAge,
		#colAddress,
		#colName,
		#colAge,
		#colAddress,
			],
		rows=[]
 
		)
 
	# AND PUSH mydata TO TABLE 
	for x in mydata:
		dt.rows.append(
			DataRow(
				cells=[
					#DataCell(Text(x['name'])),
					DataCell(
					    Container(
					        padding=padding.symmetric(horizontal=10),
					        margin=-8,
					        height= 250,
							content=Column(
							    spacing=0,
							    alignment=MainAxisAlignment.SPACE_BETWEEN,
							    controls=[
							        ListTile(
							            #title=Text(x['name']),

							            title=Row(
									        spacing=20,             
									        controls=[
									            Text(
									            	x['name'],
									            	color=colors.BLUE,
									            	size=14,
									            	weight="bold"
									            	),

									            Text(x['address']),
									        ]),


							            subtitle=Text(x['address']),
							            #on_click=self.OpenYOuAction
							            trailing=Icon(icons.MORE_VERT),
							        	dense=True,
							        ),
							    ]
							),
					    ),
					),

					#DataCell(Text(x['age'])),
					#DataCell(Text(x['address'])),
					#DataCell(Text(x['name'])),
					#DataCell(Text(x['age'])),
					#DataCell(Text(x['address'])), 
 				]
 			),
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
 
#flet.app(target=main)
flet.app(target=main, port=8886, assets_dir="assets")
