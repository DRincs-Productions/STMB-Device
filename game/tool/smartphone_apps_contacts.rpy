init python:
    from pythonpackages.sdtmb.contact import Contact

define taskbar_apps = [
    Contact(id="mc", icon="mc", character=mc),
]

screen smartphone_app_contacts():

    image "/interface/app_screen/smartphone_app_instagram.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)
