import flet as ft
from db_Feb22z import *

def main(page: ft.Page):

    page.fonts = {
        "Prototype": "Prototype.ttf",
        "Candybean": "CandyBeans.otf",
    }

    #Page initialization

    page.window_height = 700
    #page.window_width = 800
    page.title = "MyPass Manager"
    #page.scroll = "auto"

    page.on_connect = initialize_db()

    #Controls Logic


    def handle_search_change(e):
         
        handle = search_box.value
        print(f".1.  {handle}")

        results = get_by_handle(handle)
        my_data[0] = my_data_table(data=results)
        page.update()


    def handle_search_change2(e):
        if switch_row[1].value == False:
            print("1")
            handle = search_box.value
            results = get_by_handle(handle)
            my_data[0] = my_data_table(data=results)
            page.update()

        if switch_row[1].value == True:
            print("2")
            service = search_box.value
            results = get_by_service(service)
            my_data[0] = my_data_table(data=results)
            page.update()


    # NEW RECORD ADDED HERE....      
    def handle_new_pass(service, account):

        def open_dlg(*e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def close_dlg(*e):
            dlg_modal.open = False
            page.update()

        def submit(*e):
            password = new_password_field.value
            create_pass(service, account, password)
            close_dlg()



        new_password_field = ft.TextField(label="New Password", width=200, height=40)

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Enter {account} Passcode?"),
            content=new_password_field,
            actions=[ft.Row(
                    [
                        ft.TextButton("Cancel", on_click=close_dlg),
                        ft.TextButton("Submit", on_click=submit)
                    ]
                )
            ]
        )

        open_dlg()



    def handle_account_click(e, password):
        print(f"def handle_account_click(e, password):--  {e.control.data.value}") 
        page.set_clipboard(password)



    def handle_account_long_press(my_id, account):

        print(f"1. {my_id} - {account}")

        def close_dlg(*e):
            dlg_modal.open = False
            page.update()

        def open_dlg(*e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        def edit_entry(*e):
            password = change_password_field.value
            change_pass(my_id, password)
            close_dlg()

        def delete_entry(e):
            delete_pass(my_id)
            close_dlg()


        #change_password_field = ft.TextField(label="Change Password", width=200, height=40)

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Edit 1 {account} Passcode?"),
            content=ft.TextField(label="Change Password", width=200, height=40),
            actions=[ft.Row(
                    [
                        ft.TextButton("Cancel", on_click=close_dlg),
                        ft.TextButton("Delete", on_click=delete_entry),
                        ft.TextButton("Submit", on_click=edit_entry)
                    ], spacing=0
                )
            ]
        )

        open_dlg()



    #  on_long_press -MODAL   
    def showdata(e,id):
        # THEN PRINT YOU SELECT TO TERMINAL
        print(f"Selected Row... {e.control.data.value}")  
        str_idx = e.control.data.value
        #print(str_idx)  

        my_idx = str_idx.split(" | ")

        print(my_idx[0])
        my_id = int(my_idx[0])
        port = (my_idx[2])
        interface = (my_idx[3])
        info2 = (my_idx[6])



        def close_dlg(*e):
            dlg_modal2.open = False
            page.update()

        def open_dlg(*e):
            page.dialog = dlg_modal2
            dlg_modal2.open = True
            page.update()

        def edit_entry(*e):
            password = change_password_field.value
            port = change_port_field.value
            interface = change_interface_field.value
            info2 = change_info2_field.value

            print(f"\nMODAL DATA165: {my_id},{port},{interface},{info2}\n")
            change_pass(my_id, password, port, interface, info2)
            page.update()
            close_dlg()

        def delete_entry(e):
            delete_pass(my_id)
            close_dlg()


        change_password_field = ft.TextField(label="Change Password", width=200, height=40)
        #print(f"\nMODAL DATA176: {change_password_field}")

        change_port_field = ft.TextField(value = port, label="Port", width=200, height=40)
        change_interface_field = ft.TextField(value = interface, label="Interface", width=200, height=40)
        change_info2_field = ft.TextField(value = info2, label="Location", width=200, height=40)


        # MODAL FORM WINDOW
        dlg_modal2 = ft.AlertDialog(

            print(f"\nMODAL DATA: {change_port_field},{change_interface_field},{change_info2_field}"),
            modal=True,
            title=ft.Text(f"Edit 2 {str_idx}"),
            #content = change_password_field,
            content = ft.Column(
                #spacing=5,
                controls=[
                    change_password_field,
                    change_port_field,
                    change_interface_field,
                    change_info2_field,
                ]
            ),

            actions=[
                ft.Row(
                    [
                        ft.TextButton("Cancel", on_click=close_dlg),
                        ft.TextButton("Delete", on_click=delete_entry),
                        ft.TextButton("Submit", on_click=edit_entry)
                    ], 
                    spacing=0
                )
            ]
        )

        open_dlg()

        
    #Controls Display
    def my_data_table(data=None):
        print(f"Line.216- {data}")
        

        data_rows = []

        if data != None:

            data_rows = []
            datax =""

            for entry in data:
                my_id=entry[0]
                service=entry[1]
                account=entry[2]
                password=entry[3]

                station = entry[4]
                port = entry[5]
                interface = entry[6]
                floor = entry[7]
                info1 = entry[8]
                info2 = entry[9]


                print(f"3->. {entry[0]} , {entry[1]} ,{entry[2]},{entry[3]} ")
                print(f"33->. {entry[4]} , {entry[5]} ,{entry[6]} , {entry[7]},{entry[8]} , {entry[9]}")



                row = ft.DataRow(
                    cells=[
                        #ft.DataCell(ft.Text(port)),
                        #ft.DataCell(ft.Text(interface)),
                        
                        ft.DataCell(
                                ft.Container(
                                    padding=1,
                                    margin=1,#height=250,
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(floor,
                                                weight=ft.FontWeight.BOLD,
                                                style=ft.TextThemeStyle.LABEL_LARGE,
                                                font_family="Candybean",
                                            ),
                                            ft.Text(station,size=12),
                                        ]
                                    ),
                                )
                            ),

                        ft.DataCell(
                                ft.Container(
                                    padding=1,
                                    margin=1,#height=250,
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(port,
                                                weight=ft.FontWeight.BOLD,
                                                style=ft.TextThemeStyle.LABEL_LARGE,
                                                font_family="Candybean",
                                            ),
                                            ft.Text(info2),
                                        ]
                                    ),
                                )
                            ),

                        ft.DataCell(
                                ft.Container(
                                    padding=1,
                                    margin=1,#height=250,
                                    content=ft.Column(
                                        spacing=0,
                                        controls=[
                                            ft.Text(interface,
                                                weight=ft.FontWeight.BOLD,
                                                style=ft.TextThemeStyle.LABEL_LARGE,
                                                font_family="Candybean",
                                            ),
                                            #ft.Text(interface),
                                        ]
                                    ),
                                )
                            ),

                        #ft.DataCell(ft.Text(service)),


                        ft.DataCell(ft.TextButton(
                                entry[3],
                                data=ft.Text(f"{entry[0]} | {entry[2]} | {entry[3]}"),
                                on_click=lambda e: handle_account_click(e, entry[3]),
                                on_long_press=lambda e:showdata(e, data)
                        )),
                        
                    ]
                    #End cells
                )
            
                data_rows.append(row)

        table = ft.DataTable(
            width=350,
            column_spacing=5,
            columns=[
                #ft.DataColumn(ft.Text("Go")),
                ft.DataColumn(ft.Text("Floor")),
                ft.DataColumn(ft.Text("Station")),
                ft.DataColumn(ft.Text("Info2")),
                
                ft.DataColumn(ft.Text("Port")),
                #ft.DataColumn(ft.Text("Interface")),
            ],
            rows = data_rows
        )
        return table


    # <FORMS ELEMENTS>
    header = ft.Text("Welcome to MyPass")

    search_box = ft.TextField(
            label="Search",
            width=250, height=40,
            suffix_icon=ft.icons.SEARCH,
            on_change=handle_search_change)


    add_station = ft.TextField(label="Add Station", height=45)
    add_port = ft.TextField(label="Add Port", height=45)
    add_interface = ft.TextField(label="Add Interface", height=45)
    add_floor = ft.TextField(label="Add Floor", height=45)
    add_info1 = ft.TextField(label="Add Info1", height=45)
    add_info2 = ft.TextField(label="Add Info2", height=45)



    add_service = ft.TextField(label="Add Service", height=45)
    add_account = ft.TextField(
        label="Add Account",
        on_submit=lambda _: handle_new_pass(add_service.value, add_account.value),
        height=45
    )



    switch_row = [ft.Text("Account"), ft.Switch(value=False), ft.Text("Service")]

    # </FORMS ELEMENTS>



    #-----------------------------------
    bldgflr_radio = ft.RadioGroup(

        content=ft.Container(
            content=ft.Column(

                controls=[
                    ft.Row(spacing=50,controls=[
                        ft.Radio(value="AF",label="All Floors",),

                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="GF",label="GF"),
                        ft.Radio(value="UG",label="UG"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="P2",label="P2"),
                        ft.Radio(value="5F",label="5F"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="6F",label="6F"),
                        ft.Radio(value="7F",label="7F"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="8F",label="8F"),
                        ft.Radio(value="9F",label="9F"),
                    ]),
                    ft.Row(spacing=50,controls=[
                        ft.Radio(value="10F",label="10F"),
                        ft.Radio(value="11F",label="11F"),
                    ]),
                ]
                )
        )

    )
    

    #-----------------------------------
    def close_dlg(e):
        dlg_modal.open = False
        bldgflr.text = bldgflr_radio.value
        print(bldgflr_radio.value)
        page.update()

    #-----------------------------------
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("What Floor"),
        content=ft.Container(
            content=ft.Row(
                scroll ="auto",
                expand=True,
                controls=[
                
                bldgflr_radio,
                
            ]),

        ),

        actions=[
            ft.TextButton("Select", on_click=lambda e: close_dlg(e)),
            ft.TextButton("Close", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )   


    #-----------------------------------   
    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()




    #-----------------------------------
    net_miko = ft.Container(
            content=ft.Column(

                controls=[
                    ft.Row(spacing=50,controls=[
                        ft.Radio(value="AF",label="All Floors",),

                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="GF",label="GF"),
                        ft.Radio(value="UG",label="UG"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="P2",label="P2"),
                        ft.Radio(value="5F",label="5F"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="6F",label="6F"),
                        ft.Radio(value="7F",label="7F"),
                    ]),
                    ft.Row(spacing=55,controls=[
                        ft.Radio(value="8F",label="8F"),
                        ft.Radio(value="9F",label="9F"),
                    ]),
                    ft.Row(spacing=50,controls=[
                        ft.Radio(value="10F",label="10F"),
                        ft.Radio(value="11F",label="11F"),
                    ]),
                ]
                )
        )







    bldgflr = ft.TextButton(text="All Floors",icon=ft.icons.MENU_ROUNDED, on_click=open_dlg_modal)




    my_data = [my_data_table()]

   

    page.add(

        ft.Column(
            expand=True,
            controls=[


                ft.Column(
                    #scroll ="auto",
                    #expand=True,
                    controls=[
                       ft.Row(controls=[bldgflr,search_box]),
                    ]

                ),

                #ft.Row([add_service], alignment="center"),
                #ft.Row([add_account], alignment="center"),
                #ft.Row(switch_row, alignment="center"),


                #ft.Row([add_station], alignment="center"),
                #ft.Row([add_port], alignment="center"),
                #ft.Row([add_interface], alignment="center"),
                #ft.Row([add_floor], alignment="center"),
                #ft.Row([add_info1], alignment="center"),
                #ft.Row([add_info2], alignment="center"),


                ft.Column(
                    scroll ="auto",
                    expand=True,
                    controls=[
                       ft.Column(my_data, alignment="center"),
                    ],alignment=ft.MainAxisAlignment.CENTER,

                )

            ]

            )
    )

ft.app(target=main, port=8886, assets_dir="assets")

# https://www.youtube.com/watch?v=Apxe4kAPIpQ&t=2s