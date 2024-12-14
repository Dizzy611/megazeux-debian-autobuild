# megazeux-debian-autobuild
Autobuilding scripts in use by the Megazeux project (see AliceLR/megazeux). Very hacky.


NOTES:

Fresh debootstrap'd chroots need the following done to them to be usable:

* lsb-release, procps, fakeroot need to be installed
* a user named "build" needs to be created with the home directory /home/build
* ubuntu chroots need to add universe and multiverse to /etc/apt/sources.list
