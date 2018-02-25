#!/bin/bash
for i in *; do
	if compgen -G "$i/home/build/megazeux/megazeux*.deb" > /dev/null; then
		mkdir -p /var/www/html/mzxdebs/$i
        	cp $i/home/build/megazeux/megazeux*.deb /var/www/html/mzxdebs/$i/
	fi
done
