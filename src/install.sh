#!/bin/bash
# Simple script to install MySpell dics
# Copyright 2007-2010 Alan Baghumian <alan@technotux.org>
# Released under the GNU/GPL

# Only users with $UID 0 have root privileges.
ROOT_UID=0
LANGUAGE="hy"
COUNTRY="AM"
UNDERLINE=$'\137' # 137 is octal ASCII code for '_'

if [ "$UID" -ne "$ROOT_UID" ]
then
  echo "Must be root to run this script."
  exit 1
fi

# Installing info file
echo "DICT $LANGUAGE $COUNTRY $LANGUAGE$UNDERLINE$COUNTRY" > /usr/share/myspell/infos/ooo/myspell-$LANGUAGE

# Installing dics and affix data files
cp `echo "$LANGUAGE$UNDERLINE$COUNTRY.*"` /usr/share/hunspell/ && chmod 644 /usr/share/hunspell/`echo "$LANGUAGE$UNDERLINE$COUNTRY.*"`

# Creating links
cd /usr/share/hunspell/
ln -sf `echo "$LANGUAGE$UNDERLINE$COUNTRY.dic"` $LANGUAGE.dic
ln -sf `echo "$LANGUAGE$UNDERLINE$COUNTRY.aff"` $LANGUAGE.aff
cd /usr/share/myspell/dicts/
ln -sf /usr/share/hunspell/`echo "$LANGUAGE$UNDERLINE$COUNTRY.dic"` `echo "$LANGUAGE$UNDERLINE$COUNTRY.dic"`
ln -sf /usr/share/hunspell/`echo "$LANGUAGE$UNDERLINE$COUNTRY.aff"` `echo "$LANGUAGE$UNDERLINE$COUNTRY.aff"`
ln -sf /usr/share/hunspell/`echo "$LANGUAGE$UNDERLINE$COUNTRY.dic"` $LANGUAGE.dic
ln -sf /usr/share/hunspell/`echo "$LANGUAGE$UNDERLINE$COUNTRY.aff"` $LANGUAGE.aff
cd

# Update OOo's dic list
/usr/sbin/update-openoffice-dicts

# Finishing installation
echo "$LANGUAGE$UNDERLINE$COUNTRY MySpell data installed sucessfully."
