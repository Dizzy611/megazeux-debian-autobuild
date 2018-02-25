#!/usr/bin/env python3.5

import os, sys
from subprocess import check_call, call, check_output

blacklist = [ "sources" ]
chroots = []
x = os.scandir(".")


if len(sys.argv) < 2:
	print("Please give the version number to build.")
	sys.exit(1)
version = sys.argv[1]

for entry in x:
	if entry.is_dir():
		if entry.name not in blacklist:
			print(entry.path)
			chroots.append(entry.path)
y = os.scandir("./sources")
for entry in y:
	#check_call(["git", "pull", "origin"], cwd="./sources/megazeux")
	#check_call(["git", "checkout", "tags/v" + version], cwd="./sources/megazeux")
	for directory in chroots:
		call(["umount", "*/proc"])
		builddir = directory + "/home/build/megazeux"
		check_call(["mkdir", "-p", builddir])
		finalname = "megazeux-" + version
		check_call(["rm", "-rf", builddir + "/" + finalname])
		check_call(["rsync", "-avxHAX", "./sources/megazeux/", builddir + "/megazeux-" + version ])
		id = check_output("chroot " + directory + " bash -c \"lsb_release -is\"", shell=True).lower().strip().decode("ascii")
		if (id == "debian"):
			#TO DO: Get debian version
			dchcmd = "dch -v " + version + "+deb9u1 \\\"Packaging Update\\\""
		else:
			dchcmd = "dch -v " + version + "-1ubuntu1 \\\"Packaging Update\\\""
		internalbuilddir = "/home/build/megazeux"
		check_call("chroot " + directory + " bash -c \"mount -t proc proc /proc && apt-get update && apt-get --yes --force-yes dist-upgrade && apt-get --yes --force-yes install devscripts build-essential debhelper libsdl2-dev libvorbis-dev libpng-dev zlib1g-dev && chown -R build /home/build && cd " + internalbuilddir + "/" + finalname + " && " + dchcmd + " && su build -c \\\"yes | debuild -us -uc\\\" && umount /proc\"", shell=True)
