[app]

# (str) Title of your application
title = Solar System Simulator

# (str) Package name
package.name = solarsystem

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (source.dir) Source code directory (where main.py is)
source.dir = .

# (source.include_exts) File extensions to include
source.include_exts = py,png,jpg,kv,atlas

# (version) App version
version = 0.1

# (list) Application requirements
# common requirements are python3, kivy
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (string) Presplash background color
presplash_color = #020206

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use legacy build tools
android.use_legacy_toolchain = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning upon buildozer run if buildozer.spec is newer than Buildozer itself
warn_on_root = 1
