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
]

# array editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default apps = [
]
