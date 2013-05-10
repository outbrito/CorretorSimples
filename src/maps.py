# -*- coding: UTF-8 -*-

import urllib2
import urllib

query = "Trav. Antônio Ângelo, 43 Cruz das Armas João Pessoa PB"

query = urllib.quote(query)
print query

mapreq = "http://maps.google.com.br/maps?f=q&source=s_q&output=js&hl=pt-BR&geocode=&q="+query+"&btnG=Pesquisar+no+Mapa&vps=3&jsv=166d&sll=-7.152781%2C-34.891441&sspn=0.010411%2C0.01929&g=Travessa+Ant%C3%B4nio+%C3%82ngelo+43%2C+Cruz+das+Armas%2C+Jo%C3%A3o+Pessoa&abauth=1438d4b7%3A5bE3obziYMNT3gqCEseKMiZ6-is&absince=69"

response = urllib2.urlopen(mapreq)
print response.read()