import flet
from flet import (
    Page,
    Text,
    Row,
    TextField,
    ElevatedButton,
)
 

def main(page:Page):
    t=Text(value="Hello",color="green")
    page.controls.append(t)
    page.update()

    t2=Text(value="Hello2",color="red")
    page.add(t2)

    page.add(
        Row(controls=[
            Text("A"),
            Text("B"),
            Text("C"),
        ])
    )

    t31 = Text("D")
    t32 = Text("E")
    t33 = Text("F")
    page.add(
        Row(controls=[
            t31,t32,t33
        ])
    )

    t41 = TextField(label="D1")
    t42 = TextField(label="E2")
    t43 = TextField(label="F3")
    ebtn = ElevatedButton(text="Button1")
    page.add(
        Row(controls=[
            t41,t42,t43,ebtn
        ])
    )


    def button1_clicked(e):
        page.add(Text("Clicked"))

    ebtn2 = ElevatedButton(text="Button2", on_click=button1_clicked)
    page.add(
        Row(controls=[
            t41,ebtn2
        ])
    )


    def button2_clicked(e):
        t51.value = t51.value
        page.add(Text(t51.value))
        

    t51 = TextField(label="G1")
    ebtn3 = ElevatedButton(text="Button2", on_click=button2_clicked)
    page.add(
        Row(controls=[
            t51,ebtn3
        ])
    )



flet.app(port=8886, target=main)
