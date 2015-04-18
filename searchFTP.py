#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os 
import re


def sur8bit(Liste):
    print("Toto")
    #~ return False
    if type(Liste) is list:
        l = len(Liste)
    for i in Liste:
        if type(i) is not str:
            return False
    Liste2 = []
    for i in Liste:
        while len(i) < 8:
            i = '0' + str(i)
        Liste2.append(i)
    return Liste2


def iteration(Liste, masque):
    '''
    '''
    print(Liste)
    ip = ''
    for i in Liste:
        ip += i
    print(ip, masque)
    print("----------------------")
    IP = str(ip)
    IP = IP[:masque]
    IP += '0' * (32 - len(IP))    
    print(IP)

def IPv4iter(Tuple):
    ''' Reçoit un tuple en entrée. Devrait être IP/masque ou bien (ip, masque)
    Renvoie la liste des IPs correspondant au masque.
    '''
    if type(Tuple) is not tuple:
        print(type(Tuple))
        Tuple = str(Tuple)
    l = len(Tuple)
    print(l)
    if l != 2:
        try:
            Liste = Tuple.split('/')
            ip = Liste[0]
            masque = Liste[1]
        except:
            return False
    else:
        ip = Tuple[0]
        masque = Tuple[1]
    try:
        Liste = ip.split('.')
    except:
        return False
    try:
        IP0 = int(Liste[0])
        IP1 = int(Liste[1])
        IP2 = int(Liste[2])
        IP3 = int(Liste[3])
        M = int(masque)
    except:
        raise Exception("N.A.N")
        return False
    if M == 32:
        return ip
    elif M < 32 and M >= 0:
        Liste2 = ip2bit(Liste, masque)
    else:
        return False
    Liste3 = iteration(Liste2, M)
    
    
    print(Tuple)
    return Liste2


def ip2bit(Liste, masque):
    l = len(Liste)
    if l != 4:
        return False
    Liste2 = []
    for i in Liste:
        try:
            i = int(i)
        except:
            raise Exception("N.A.N.")
            return False
        Liste2.append(str(bin(i)[2:]))
    Liste3 = sur8bit(Liste2)
    
    return Liste3


#~ IPv4iter(("toto", 1))

#~ Liste1 = IPv4iter("192.168.2.25/32")
Liste2 = IPv4iter("192.168.6.1/30")
#~ print(Liste1, Liste2)
print(Liste2)



#######################



def IPv6iter(Tuple = None):
    ''' Srsly Dude ?
    Here, have a penguin :             ooo
                                   ooo$$$$$$$$$$$oo
                                o$$$$$$$$$$$$$$$$$$$ooo
                              o$$$$$$$$$$$$$$$$$"$$$$$$$oo
                           o$$$$$$$$$$$$$$$$$$$  o $$$$$$$$$$$$$$oooo
                          o$$$$"""$$$$$$$$$$$$$oooo$$$$$$$$$$$$$"""
                        oo$""      "$$$$$$$$$$$$$$$$$$$$$$$$"
                       o$$          $$$$$$$$$$$$$$$$$$$$$$"
                      o$$            $$$$$$$$$$$$$$$$$$$$
                    o$$$$             $$$$$$$$$$$$$$$$$"
                   o$$$$$$oooooooo "                $"
                  $$$$$$$$$$$$$$"
                 $$$$$$$$$$$$$$
                o$$$$$$$$$$$$$                         o
               o$$$$$$$$$$$$$                           o
              o$$$$$$$$$$$$$$                            "o
             o$$$$$$$$$$$$$$$                             "o
            o$$$$$$$$$$$$$$$$                              $
           o$$$$$$$$$$$$$$$$"                              "
           $$$$$$$$$$$$$$$$$                                $
          o$$$$$$$$$$$$$$$$$                                $
          $$$$$$$$$$$$$$$$$                                 $
         $$$$$$$$$$$$$$$$$$                                 "
         $$$$$$$$$$$$$$$$$                                   $
        $$$$$$$$$$$$$$$$$                                    $
        $$$$$$$$$$$$$$$$"                                    $$
       $$$$$$$$$$$$$$$$$                                      $o
       $$$$$$$$$$$$$$$$$                                      $$
      $$$$$$$$$$$$$$$$$$                                       $
      $$$$$$$$$$$$$$$$$$o                                      $$
     $$$$$$$$$$$$$$$$$$$$o                                     $$
     $$$$$$$$$$$$$$$$$$$$$$o                                   "$
     $$$$$$$$$$$$$$$$$$$$$$$$o                                  $
    $$$$$$$$$$$$$$$$$$$$$$$$$$$                                 $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$                                $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                               $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$o                              $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o                             $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                             $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                             $"
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                            $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                            $"
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                            $
     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                            o$
     $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                            $"
     $$$$$$$$$$$$$$$$$$$$$$$$$$$$"                            $
     $$$$$$$$$$$$$$$$$$$$$$$$$$$"                             $
      $$$$$$$$$$$$$$$$$$$$$$$$$"                             $$
      $$$$$$$$$$$$$$$$$$$$$$$$"                              $$
      $$$$$$$$$$$$$$$$$$$$$$$                                $$
       $$$$$$$$$$$$$$$$$$$$$                                o$$
       $$$$$$$$$$$$$$$$$$$$                                 $$"
       "$$$$$$$$$$$$$$$$$$                                  $$
        $$$$$$$$$$$$$$$$$                                  o$$
        "$$$$$$$$$$$$$$$"                                  $$
         $$$$$$$$$$$$$$$                                   $$
         "$$$$$$$$$$$$$"                                  o$
          $$$$$$$$$$$$"                                   $$
          $$$$$$$$$$$"                                    $$
           $$$$$$$$$"                                    $$"
           $$$$$$$$$                                     $$
           "$$$$$$$"                                    $$
            $$$$$$$o                                    $"
           o$$$$$$$$                                   $$
           $$$$$$$$$                                   $$
          o$$$$$$$$$                                   $"
          $$$$$$$$$$                                  $$
          "$$$$$$$$$                                o$""
           "$$$$$$$$                          ooooo$$oo
              ""$$$$$o                oooo$$$$$$$$$$$$$$ooo
                 "$$$$$ooooooo     """""""""$$$""""$$o   ""
                                                      "
    '''
    print("Non, je plaistante ! ;-)")


