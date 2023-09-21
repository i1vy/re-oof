import os
import shutil
import time

# the roblox folder
robloxfolder = "C:/Users/even/AppData/Local/Roblox/Versions/"

error = False

print("loading...")

# all installed roblox versions
versions = os.listdir(robloxfolder)

# remove non-folders
for version in versions:
	if not version.startswith("version-"):
		versions.remove(version)
		continue

# remove folders without ouch.ogg
for version in versions:
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

		try:
			os.remove(robloxfolder + version + "/content/sounds/ouch.ogg")
		except Exception as e:
			print("    error deleting: " + str(e))
			error = True
			continue

	# copy new ouch.ogg
	print("    copying...")

	try:
		shutil.copy2("./ouch.ogg", robloxfolder + version + "/content/sounds/ouch.ogg")
	except Exception as e:
		print("    error copying: " + str(e))
		error = True
		continue

	print("    patched!")

print()

if error:
	print("finished with errors")
	input("press enter to exit")
