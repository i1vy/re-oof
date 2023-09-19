import os
import shutil
import time

print("""
                              __ 
                             / _|
  _ __ ___ ______ ___   ___ | |_ 
 | '__/ _ \______/ _ \ / _ \|  _|
 | | |  __/     | (_) | (_) | |  
 |_|  \___|      \___/ \___/|_|  
                                 
                                 
""")

# the roblox folder
robloxfolder = "C:/Users/even/AppData/Local/Roblox/Versions/"

print("loading...")

# all installed roblox versions
versions = os.listdir(robloxfolder)

# remove folders without ouch.ogg
for version in versions:
	if not version.startswith("version-"):
		versions.remove(version)
		continue
	
	if not "content" in os.listdir(robloxfolder + version):
		versions.remove(version)
		continue


print("found " + str(len(versions)) + " versions to patch")

# patch all patchable versions
for version in versions:
	print()

	print("patching " + version + ":")

	# delete old ouch.ogg
	if os.path.isfile(robloxfolder + version + "/content/sounds/ouch.ogg"):
		print("    deleting...")
		os.remove(robloxfolder + version + "/content/sounds/ouch.ogg")

	# copy new ouch.ogg
	print("    copying...")
	shutil.copy2("./ouch.ogg", robloxfolder + version + "/content/sounds/ouch.ogg")

	print("    patched!")