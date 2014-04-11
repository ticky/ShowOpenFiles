# ShowOpenFiles

Simple plugin for Sublime Text to show the number of open files in the status bar.

## Installation

You may either install using Package Control (which gains you automatic updates and a simpler install), or manually using `git`.

### Package Control (Recommended)

_**Note**: The package is not yet on Package Control. Please use the manual installation for now._

1. Install [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation).
2. Run `Package Control: Install Package` from the Command Palette
3. Find and install the `ShowOpenFiles` plugin

### Manual

1. CD into your Sublime Text 2 Packages directory;
	* Windows: `%APPDATA%\Sublime Text 3\Packages\`
	* OS X: `~/Library/Application Support/Sublime Text 3/Packages/`
	* Linux: `~/.config/sublime-text-3/Packages/`
	* Portable Installation: `Sublime Text 3/Data/Packages/`
2. `git clone https://github.com/geoffstokes/ShowOpenFiles.git ShowOpenFiles`

_**Note**: For Sublime Text 2 users, substitute the `3` in the above directory names with `2`._

## Usage

The number of files open in the current window will be displayed in the status bar. This is updated whenever a view is opened or closed. There are no settings to configure.
