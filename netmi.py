# LTOP1787
#   C:\DevApps\pyProj\workspace\src_flutter
# cd \devapps\pyproj\workspace\ && MainVenv\scripts\activate && cd src_flutter

import flet as ft
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

def main(page):

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme3" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme2"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    c = ft.Switch(label="Light theme1", on_change=theme_changed)
    page.add(c)

    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(name="settings", color="#c1c1c1",size=40),
        leading_width=40,
        title=ft.Text("viNoc Tools - DevApp"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
        c,
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
        ],
    )
    page.update()

    
    def yes_close(e):
        page.window_destroy()

    def close_banner(e):
        page.banner.open = False
        tb1.value = ""
        tb2.value = ""
        tb3.value = ""
        page.update()
    
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}'"
        test(t.value)
        send_show_command(tb1.value, tb2.value, tb3.value)
        page.update()

    def send_show_command(host, user, password):
        host = "sandbox-iosxe-latest-1.cisco.com"
        device = {
            "device_type": "cisco_ios",
            "host": host,
            "username": user,
            "password": password,
        }
        commands =[
            'sh ip int brie',
            'show vlans'
        ]
        
        result = {}
        err =""
        try:
            with ConnectHandler(**device) as ssh:
                ssh.enable()
                for command in commands:
                    output = ssh.send_command(command)
                    result[command] = output
            print("Done Successfully...")
            show_nextpage()
            return result
        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            err = f" {error} "
            print(err)
            show_banner(err)


    page.banner = ft.Banner(
        bgcolor=ft.colors.RED_500,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        actions=[
            ft.ElevatedButton(text="Retry New Value", on_click=close_banner),
            ft.ElevatedButton(text="Cancel", on_click=yes_close),
        ],
    )
          
    def show_banner(err):
        page.banner.content = ft.Text(f"{err}")
        page.banner.open = True
        page.update()  


    page.nextpage = ft.Column(
            horizontal_alignment="center",
            alignment="start",
            controls=[
                ft.Text(
                    "Mock!! LOGIN Form With Python API Back-End",
                    size=32,
                    weight="w700",
                    text_align="center",
                ),
                ft.Text(
                    "This Flet web-app/registration page is routed to a python (Flask-based) API. Registering sends a request to the API-specific rout and performs several functions.",
                    size=14,
                    weight="w700",
                    text_align="center",
                    color="#64748b",
                ),
            ],
        )
      

    def show_nextpage():
        #page.nextpage.content = ft.Text(f"{err}")
        page.nextpage.open = True
        page.update()    


    t = ft.Text()
    tb1 = ft.TextField(label="Host", hint_text="Host Address")
    tb2 = ft.TextField(label="UserName", hint_text="User Account")
    tb3 = ft.TextField(label="Password", hint_text="Passord", password=True, can_reveal_password=True)
    #tb4 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)

    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    
    #page.add(tb1, tb2, tb3,tb4, b, t)
    page.add(tb1, tb2, tb3, b, t)




    def test(val):
        print(val)


#ft.app(host="10.16.67.27", port=8886, target=main)
ft.app(port=8886 , target=main)
#ft.app(port=8886,target=main, view=ft.WEB_BROWSER)
#ft.app(host="192.168.1.6", port=8886,target=main, view=ft.WEB_BROWSER)