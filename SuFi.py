#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author = M Adi SyahPutra
#SENGAJA GAK DI COMPILE.BIAR YANG NEWBIE BISA BELAJAR DARI SCRIPT INI :)


wd = "\033[90;1m" # dark
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
P = "\033[1;35m"

                                   
print GG+"\t\t      @@@@@@   @@@  @@@  @@@@@@@@  @@@  "
print"\t\t     @@@@@@@   @@@  @@@  @@@@@@@@  @@@  "
print"\t\t     !@@       @@!  @@@  @@!       @@!  "
print"\t\t     !@!       !@!  @!@  !@!       !@!  "
print"\t\t     !!@@!!    @!@  !@!  @!!!:!    !!@  "
print"\t\t      !!@!!!   !@!  !!!  !!!!!:    !!!  "
print G+"\t\t          !:!  !!:  !!!  !!:       !!:  "
print"\t\t         !:!   :!:  !:!  :!:       :!:  "
print"\t\t     :::: ::   ::::: ::   ::        ::  "
print"\t\t     :: : :     : :  :    :        :"
print YY+"\t\t\t     Subdomain Finder"
print""
print WW+"\t\t  #########################################"
print"\t          #                                       #"
print "\t\t  #           Author : iExEi HD           #"
print "\t\t  #         Thanks To : ITermSec          #"
print"\t          #                   : Akbar-Neotech     #"
print "\t          #                                       #"
print RR+"\t\t  #>>>>>>>> >> Lead Cyber Team << <<<<<<<<#"
print "\t\t  #>>>>>>>> > INDONESIAN LAMMER < <<<<<<<<#"
print WW+"\t          #                                       #"

print"\t\t  #########################################"


print wd+"NOTE : Masukan Website Tanpa Https:// Ataupun Www"
print""
import requests

target_url = raw_input(GG+"\tMasukan Site : "+P)
def rikues(url):
 try:
  return requests.get("http://"+url)
 except requests.exceptions.ConnectionError:
  pass

target_url 

with open("heker.txt", "r") as wordlist_file:
 for line in wordlist_file:
  word=line.strip()
  test_url=word+"."+target_url
  response = rikues(test_url)
  if response:
   print(RR+"Subdomain Ditemukan >> "+WW+test_url)
