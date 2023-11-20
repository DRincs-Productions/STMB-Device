init -1 python:
    if not "taskbar_apps" in locals() | globals():
        taskbar_apps = []
    if not "df_apps" in locals() | globals():
        df_apps = []
    if not "apps" in locals() | globals():
        apps = []

# array editable at runtime, but it is strongly discouraged to pre-enter elements (dictionary contents are based only on saves)
default apps = []
