#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

#---------------------------------------------------------------------------#
# This file is part of Xerosploit.                                          #
# Xerosploit is free software: you can redistribute it and/or modify        #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# Xerosploit is distributed in the hope that it will be useful,             #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with Xerosploit.  If not, see <http://www.gnu.org/licenses/>.       #
#                                                                           #
#---------------------------------------------------------------------------#
#                                                                           #
#        Copyright © 2016 LionSec (www.lionsec.net)                         #
#                                                                           #
#---------------------------------------------------------------------------#

#if not os.geteuid() == 0:
#    sys.exit("""\033[1;91m\n[!] Xerosploit installer must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")

print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     Xerosploit Installer                     █
█                                                              █
└══════════════════════════════════════════════════════════════┘     \033[1;m""")

if __name__ == "__main__":
		print("\033[1;34m\n[++] Installing Xerosploit ... \033[1;m")
		# install = os.system( "apt-get update && apt-get install -y nmap hping3 build-essential python-pip ruby-dev git libpcap-dev libgmp3-dev && pip install tabulate terminaltables")
		# install1 = os.system("""cd tools/bettercap/ && chmod +x bin/xettercap && gem build bettercap.* && sudo gem install xettercap-* && rm xettercap-* && cd ../../ && sudo mkdir -p /opt/xerosploit && sudo cp -R tools/ /opt/xerosploit/ && sudo cp xerosploit.py /opt/xerosploit/xerosploit.py && sudo cp banner.py /opt/xerosploit/banner.py && sudo cp run.sh /usr/local/bin/xerosploit && sudo chmod +x /usr/local/bin/xerosploit && tput setaf 34; echo "Xerosploit has been sucessfuly installed. Reopen terminal nad execute 'sudo xerosploit'." """)	
		os.system("brew install iproute2mac nmap hping bettercap && gem install bettercap")
		os.system("pip2 install tabulate terminaltables twisted Pillow && cd sslstrip && python setup.py install && cd ..")
		os.system("""
			sudo mkdir -p /opt/xerosploit && \
			sudo cp -R tools/ /opt/xerosploit/tools && \
			sudo cp xerosploit.py /opt/xerosploit/xerosploit.py && \
			sudo cp banner.py /opt/xerosploit/banner.py && \
			sudo cp run.sh /usr/local/bin/xerosploit && \
			sudo chmod +x /usr/local/bin/xerosploit && \
			tput setaf 34; printf "Xerosploit has been sucessfuly installed.\nRestart terminal and execute 'xerosploit'." 
			""")	
