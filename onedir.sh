#!/bin/bash
mkdir -p /var/www/html/mzxdebs-onedir
cd /var/www/html/mzxdebs
for i in *; do
	if [[ $i == ubuntu-* ]]; then
		cd $i
		for k in *.deb; do
			m="$(echo $i | sed 's/ubuntu-//')"
			echo $m
			l="$(echo $k | sed s/amd64/$m/ | sed s/i386/$m/)"
			echo $l
			cp $k /var/www/html/mzxdebs-onedir/$l
		done
		cd ..
	else
		cd $i
		for k in *.deb; do
			m=$i
			echo $m
			l="$(echo $k | sed s/amd64/$m/ | sed s/i386/$m/ | sed s/armhf/raspbian-armhf/)"
			echo $l
			cp $k /var/www/html/mzxdebs-onedir/$l
		done
		cd ..
	fi
done

