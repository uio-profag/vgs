# Kursside for ProFag:VGS

[![Build Status](https://travis-ci.com/uio-profag/vgs.svg?branch=master)](https://travis-ci.com/uio-profag/vgs)

Innhold, i form av jupyter notebooks og markdown-filer, legges i `content` (og underdirectories). 

Dette innholdet lenkes til med innholdsfortegnelsen i `toc.yml`. Denne kan se noe frastøtende ut ved første øyekast, men hovedregelen er å følge mønsteret fra det andre som allede står der. Om man gjør noe feil får det bare konsekvense om feilen var å fjerne oppføringer (slik at innhold blir borte fra nettsiden). Alle feil som har med syntakt å gjøre fører bare til at nettsiden ikke publiseres, altså forblir nettsiden som den var. 

Man kan legge inn enten markdown-dokumenter eller jupyter notebooks. I tilfellet jupyter notebook vil denne automatisk konverteres til markdown før nettsiden blir til. 

Mappen `_includes` finnes for at vi skal kunne ha innholdstyper som ikke støttes av `jupyter-book`. I skrivende stund bruker vi det kun for å kunne embede youtube-videoer med fornuftig skalering med viduet. 

Mappen `assets` inneholder filer som brukes til design av siden. I skrivende stund ligger det kun en uio-logo der. 

Filen `.gitignore` er en fil som forteller hvilke filer som git skal ignorere. Dette er vanlig å ha i ethvert git-repository. 

`Makefile` inneholder de terminalkommandoene som må kjøres for å bygge en nettside av notebooks og markdown-filer i dette repositoriet. I hovedsak dreier det seg om å laste ned `jupyter-book`, kopiere litt filer, og kjøre kode fra `jupyter-book`. 

`_config.yml` inneholder konfigurasjonen av denne nettsiden. Det er der man setter f. eks om nettsiden heter ProFag:U eller ProFag:VGS, og hvilken fil som inneholder logoen til nettsiden. 

`favicon.ico` er logoen som kommer i fanelinja i nettleseren når man åpner nettsiden. 

`requirements.txt` inneholder lista over python-pakker som trengs for å bygge nettsiden.

