# MyStrand: ohjeet kehittäjäagentille

MyStrand on Strandin kiinteistönvälittäjien työkalu Suomessa, Espanjassa ja Ranskassa. Se käsittelee henkilötietoja, KYC-aineistoa ja kauppojen tietoja, joten tietoturva ja tietosuoja menevät nopeuden edelle.

## Ennen kuin muutat mitään

- Lue `policy/rules.yaml`. Jokaisella säännöllä on tunniste (esim. `GDPR-002`). Viittaa tunnisteisiin PR:n kuvauksessa, kun muutos koskee niitä.
- Tarkista `policy/no-fly.yaml`. Jos tehtävä vaatii muutoksen no-fly-polkuun, älä yritä kiertää estoa. Kirjoita Linear-tikettiin, mitä pitäisi muuttaa ja miksi, ja jätä toteutus ihmiselle.
- Älä koskaan muokkaa kansioita `.claude/` tai `.github/` äläkä tiedostoja `policy/rules.yaml`, `policy/no-fly.yaml` tai `policy/threat-model.md`. Ne ovat suojakaiteet, ja niiden muutokset tekee ihminen. Ainoa poikkeus on `policy/data-map.yaml`, johon lisäät uudet kentät.

## Henkilötiedot

- Jokainen uusi tietokannan kenttä lisätään tiedostoon `policy/data-map.yaml` ja luokitellaan. Luokittelematon kenttä kaataa buildin (`GDPR-001`). Tietosuojavastaava hyväksyy luokituksen PR:ssä.
- Henkilötunnusta, KYC-asiakirjoja tai muita `sensitive`- ja `kyc`-luokan tietoja ei kirjoiteta lokeihin, virheilmoituksiin, analytiikkaan eikä URL-osoitteisiin (`GDPR-002`, `GDPR-003`).
- Testeissä käytetään vain synteettistä dataa (`GDPR-004`). Älä kopioi tuotannon tietoja mihinkään.
- Uusi käyttötarkoitus tai uusi kolmas osapuoli, jolle tietoja siirretään, vaatii aina ihmisen päätöksen (`GDPR-007`). Kirjaa se PR:ään.

## Tietoturva

- Jokainen API-reitti tarkistaa, että käyttäjällä on oikeus juuri tähän kohteeseen, asiakkaaseen tai kauppaan (`SEC-003`). Lisää muutokselle testi, joka osoittaa, ettei toisen välittäjän tai asiakkaan tietoja näe.
- Ei SQL-merkkijonojen yhdistelyä, vaan parametrisoidut kyselyt (`SEC-004`).
- Ei salaisuuksia koodiin, testeihin tai esimerkkitiedostoihin (`SEC-001`).

## Valmis tarkoittaa

- Tarkistukset menevät läpi paikallisesti ja CI:ssä.
- Muutokselle on testi, ja tietoturvaan liittyvälle muutokselle negatiivinen testi (mitä ei saa tapahtua).
- PR:n kuvauksessa on Linear-tiketti, muutoksen tarkoitus ja koskettujen sääntöjen tunnisteet.
