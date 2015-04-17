#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os 
import re

def IPv4iter(Tuple):
    ''' Reçoit un tuple en entrée. Devrait être IP/masque ou bien (ip, masque)
    Renvoie la liste des IPs correspondant au masque.
    '''
    if type(Tuple) is not tuple:
        print(type(Tuple))
        Tuple = str(Tuple)
    l = len(Tuple)

    if l == 1:
        try:
            Liste = Tuple.split('/')
            ip = Liste[0]
            masque = Liste[1]
        except:
            return False
    elif l == 2:
        ip = Tuple[0]
        masque = Tuple[1]
    else:
        return False
    try:
        Liste = ip.split('.')
    except:
        return False
    if masque == 32:
        return ip
    elif ip <32 and ip >= 0:
        Liste2 = ip2bit(Liste, masque)
    else:
        return False
    
    
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
    return Liste2


IPv4iter(("toto", 1))

#~ IPv4iter("192.168.1.10/32")



def ip2bit(Liste):
    '''
    '''
    l = len(Liste)
    print(l, Liste)

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


