#!/bin/sh

ACV="Autoconf version 2.13"
AMV="automake (GNU automake) 1.4"
USAGE="
You need to install:
	libtool-1.3.5
	autoconf-2.13
	automake-1.4
"

[ "`autoconf --version`" != "$ACV" ] && echo "$USAGE" && exit 1
[ "`automake --version | head -1 | sed -e 's/1\.4[a-z]/1.4/'`" != "$AMV" ] && echo "$USAGE" && exit 1

aclocal
autoheader
automake
autoconf

if [ "$1" = "--noconfigure" ]; then 
    exit 0;
fi

./configure "$@"
