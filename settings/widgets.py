from libqtile import widget
import datetime

widget_defaults = dict(
    font='Hack Nerd Font',
    fontsize=14,
    padding=3,
)

widgets = [
    widget.CurrentLayout(),
    widget.GroupBox(block_highlight_text_color='#77ff88',
                    borderwidth=0, fontsize=17, highlight_method='block',
                    padding=10),
    widget.Prompt(),
    widget.WindowName(),
    widget.Systray(),
    widget.Clock(format='%Y/%m/%d %a %H:%M:%S', foreground='#77ff88'),
]

extension_defaults = widget_defaults.copy()
