# MyStrand: uhkamalli (runko)

Täydennetään ensimmäisessä tietoturvatyöpajassa. Katselmointiagentti lukee tämän tiedoston jokaisen PR:n yhteydessä.

## Mitä suojataan

| Kohde | Miksi | Luokka |
| --- | --- | --- |
| Asiakkaiden ja kuolinpesien henkilötiedot | GDPR, luottamus | pii, sensitive |
| KYC-aineisto | Rahanpesulaki, viranomaisvalvonta | kyc |
| Kauppojen ja tarjousten tiedot | Liikesalaisuus, asiakkaan etu | internal |
| DIAS- ja maksuintegraatiot | Rahaliikenne, kaupan pätevyys | no-fly |
| Välittäjien tunnukset ja oikeudet | Pääsy kaikkeen yllä olevaan | no-fly |

## Keneltä

- Ulkopuolinen hyökkääjä (tunnusten kalastelu, haavoittuvuudet riippuvuuksissa)
- Toinen välittäjä tai asiakas, joka näkee tietoja, joihin hänellä ei ole oikeutta
- Virheellinen tai liian laaja agentin muutos (Claude Code, Linearin agentit tai muut)
- Tiketin, palautteen tai PR-kommentin kautta agentille syötetty ohje (prompt injection)
- Kolmannen osapuolen palvelu, jolle tietoja siirretään

## Tärkeimmät riskit ja vastatoimet

| Riski | Vastatoimi | Sääntö |
| --- | --- | --- |
| Asiakas tai välittäjä näkee toisen tiedot | Valtuutus jokaisessa reitissä, eristystestit | SEC-003 |
| Henkilötiedot vuotavat lokeihin | Semgrep-säännöt, lokien maskaustesti | GDPR-002 |
| Agentti muuttaa säänneltyä koodia | No-fly-hook, CODEOWNERS | SEC-006 |
| Agentti löysää omia sääntöjään | Suojakaiteet suojattu | SEC-007 |
| Haavoittuva riippuvuus | Dependency review | SEC-002 |
| Tikettiin tai palautteeseen kirjoitettu ohje saa agentin toimimaan väärin | Sisältö on dataa, katselmointi vertaa laajuutta tikettiin | SEC-011 |
| Agentti hyväksyy oman muutoksensa tai ohittaa säännöt | Oma identiteetti, ei ohitusoikeuksia, viimeisen pushin hyväksyntä | SEC-012 |
| Suojausasetuksia heikennetään huomaamatta | Päivittäinen asetusvalvonta ja hälytys | SEC-013 |
| Asiakastietoja päätyy Slackiin tai Lineariin | Ohje, sopimukset ja säilytysajat | GDPR-008 |

## Avoimet kysymykset

- TODO: mitkä kolmannet osapuolet saavat henkilötietoja (portaalit, DIAS, allekirjoituspalvelu, Slack, Linear, AI-palvelut)?
- TODO: mitkä agentit saavat kirjoittaa repoon, ja millä GitHub-identiteetillä kukin toimii?
- TODO: missä maissa tietoja käsitellään ja säilytetään?
