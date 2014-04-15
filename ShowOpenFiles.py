# coding=utf8
import sublime, sublime_plugin

class OpenFilesPlugin(sublime_plugin.EventListener):

    def __init__(self):
        return

    def on_activated(self, view):
        self.update_status(view)
    def on_new(self, view):
        self.update_status(view)
    def on_close(self, view):
        self.update_status(view)

    def update_status(self, view):
        view_count = len(sublime.active_window().views())
        view.set_status('ShowOpenFilesPluginStatus', "Editing %d file%s" % (view_count, ("s" if view_count != 1 else "")))
