# Kursside for ProFag:VGS
[![Build Status](https://travis-ci.org/uio-profag/vgs.svg?branch=master)](https://travis-ci.org/uio-profag/vgs)

`index.md` inneholder forsiden

Resten av innholdet legges i `pages` (og underdirectories). Sider med `sidebar_link=true` kommer opp i venstremenyen. Resten må eksplisitt lenkes opp fra andre sider for å kunne navigeres til. 

På denne siden har vi 

1. Introduksjon/kom i gang 
2. Moduler (inneholder alle delene av kurset som vi underviser)
3. Veien videre (etterarbeid)

Delene med moduler og veien videre lenker videre til flere sider som vi lager med jupyter notebooks. 

Man kan legge inn enten markdown-dokumenter eller jupyter notebooks. I tilfellet jupyter notebook vil denne automatisk konverteres til markdown på travis CI før publisering av nettsiden. 

For at integreringen med github deployment skal fungere trenger man å legge til en github token i Travis. 
