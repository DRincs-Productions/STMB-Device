init python:
    from pythonpackages.sdtmb.app import App


define taskbar_apps = [
    App(id="phone", name=_("Phone"), icon="icon app phone"),
    App(id="messages", name=_("Messages"), icon="icon app messages"),
    App(id="contacts", name=_("Contacts"), icon="icon app contacts"),
    App(id="settings", name=_("Settings"), icon="icon app settings"),
    App(id="browser", name=_("Browser"), icon="icon app firefox"),
]

# array that cannot be modified at runtime, only by modifying the code. (content is not based on saves, but from the code)
define df_apps = [
    App(id="calculator", name=_("Calculator"), icon="icon app calculator"),
    App(id="games", name=_("Games"), icon="icon app games"),
    App(id="instagram", name=_("Instagram"), icon="icon app instagram"),
    App(id="mail", name=_("Mail"), icon="icon app outlook"),
    App(id="gallery", name=_("Gallery"), icon="icon app photo"),
    App(id="rewards", name=_("Rewards"), icon="icon app rewards"),
]

# array editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default apps = [
]
