# coding=utf8
import sublime, sublime_plugin

class OpenFilesPlugin(sublime_plugin.EventListener):
    def __init__(self):
        return
    def on_new(self, view):
        self.update_encoding(view)
    def on_close(self, view):
        self.update_encoding(view)

    def update_encoding(self, view):
        view_count = len(view.window().views())
        print('Updating Status to %d' % view_count)
        view.set_status('ShowOpenFilesPluginStatus', "Editing %d file%s" % (view_count, ("s" if view_count != 1 else "")))
