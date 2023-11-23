init -1 python:
    if not "taskbar_apps" in locals() | globals():
        taskbar_apps = []
    if not "df_apps" in locals() | globals():
        df_apps = []
    if not "apps" in locals() | globals():
        apps = []
    if not "contacts" in locals() | globals():
        contacts = []
    if not "messages_mc_list" in locals() | globals():
        messages_mc_list = []
    if not "df_messages_mc_list" in locals() | globals():
        df_messages_mc_list = []

# array editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default apps = []

default messages_mc_list = []
