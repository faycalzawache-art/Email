[app]

# (str) Title of your application
title = Void Harvester

# (str) Package name
package.name = voidcrawler

# (str) Package domain (needed for android packaging)
package.domain = org.void

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# تم إضافة كل المكتبات اللازمة لعمل Requests و BeautifulSoup و Plyer
requirements = python3,kivy==2.2.1,requests,beautifulsoup4,plyer,urllib3,chardet,idna,certifi

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android build-tools version to use
android.build_tools_version = 33.0.0

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (str) Android architecture to build for.
# إذا كنت تستخدم هاتف حديث استخدم arm64-v8a، للهواتف الأقدم armeabi-v7a
android.archs = arm64-v8a

# (bool) enables Android auto backup feature.
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aar)
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 0

# (str) Path to build artifact storage, can be a variable name relative to the current directory
bin_dir = ./bin
