# from libqtile.lazy import lazy
from settings.keys import keys, mod
from settings.widgets import widget_defaults, extension_defaults
from settings.groups import groups
from settings.screens import screens
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.path import qtile_path

dgroups_key_binder = None
dgroups_app_rules = []
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"
