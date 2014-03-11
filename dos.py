import sublime, sublime_plugin
import os
from subprocess import Popen


class DosCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if len(self.view.file_name()) > 0:
			cmd_line = ''
			if sublime.platform() == "windows":
				cmd_line = 'CMD /K CD /D "%s"' % (os.path.dirname(os.path.realpath(self.view.file_name())))
			print "MS-DOS command: " + cmd_line
			Popen(cmd_line)


	def is_enabled(self):
		return sublime.platform() == "windows" and self.view.file_name() and len(self.view.file_name()) > 0
