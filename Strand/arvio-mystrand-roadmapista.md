# Arvio: MyStrand-roadmap ja siirtymä agenttiseen kehitykseen

Strandin CTO:n tekemä MyStrand-sovelluksen roadmap: [`mystrand-roadmap.pdf`](./mystrand-roadmap.pdf). Tavoitteena on siirtyä käsin rakentamisesta agenttiseen kehitystapaan. Vertailukohta on Mika Viskarin dekki: [`arvio-viskarin-dekista.md`](./arvio-viskarin-dekista.md).

Päivitetty 18.11.2026.

Lyhyesti: roadmap on hyvä kuva siitä, mitä on tekeillä, mutta se ei ole vielä suunnitelma siitä, miten tehdään. Agenttiseen tapaan siirtymistä siinä ei ole mukana lainkaan.

## Mitä roadmapissa on

Siinä on noin 70 ominaisuutta neljälle markkinalle (FI I, FI II, ES, FR+n), ja jokaiselle tila konseptista valmiiseen.

- **FI I (Kivin korvaaminen) on lähes maalissa.** 26 ominaisuutta on valmiina ja 7 kesken:
  - viimeistelyssä: KYC, kuolinpesäasiakkaat, sähköiset allekirjoitukset ja varainsiirtoveroilmoitus
  - kehityksessä: välittäjän kohdeportfolionäkymä, hintaseurantaintegraatio ja portaalien mainosnostot
- **Keskeneräistä työtä on paljon yhtä aikaa.** Noin 16 ominaisuutta on kehityksessä ja 10 viimeistelyssä, vaikka must have -lista ei ole vielä valmis. Esimerkiksi FR-arkkitehtuuri, FR-organisaatio, seitsemän FI→ES-ominaisuutta, AI-agenttialusta, ad creator ja uutiskirjeet ovat kaikki kehityksessä samaan aikaan.
- **AI on roadmapissa tuotteen ominaisuutena, ei tekemisen tapana.** AI-videot, dokumenttien AI-luenta ja AI-agenttialusta ovat asioita, joita välittäjä käyttäisi. Siitä, miten softaa tehdään, roadmap ei sano mitään.

## Mitä roadmapista puuttuu agenttisen tavan kannalta

- **Ei aikatauluja, vastuuhenkilöitä, työmääriä eikä tavoitteita.** Mittarina on vain tila. Viskarin dekin oma neuvo on mitata lopputuloksia, ei aktiivisuutta: esimerkiksi kuinka moni välittäjä on siirtynyt Kivistä, tai kuinka nopeasti kohde saadaan julkaistua.
- **Ei käyttäjäpolkuja eikä käsitteiden määrittelyä.** Välittäjän, ostajan, myyjän, isännöitsijän ja kuolinpesän polut kannattaa kirjoittaa auki. Agentit tuottavat nopeasti juuri sitä, mitä niille on määritelty, joten määrittely on agenttisessa tavassa koko kapasiteetti.
- **ES/FR-laajennus on se kohta, jossa johdonmukaisuus ratkaisee.** FI→ES-rivit näyttävät rakentavan KYC:n, tarjouksen ja kauppakirjan jokaiselle maalle uudelleen. Roadmapin oma kohta "markkinakohtaisten yhteneväisyyksien ja erityispiirteiden erottaminen" on oikea, ja se kannattaa tehdä ennen kuin agentit monistavat rakenteen kolmeen maahan.
- **Ihmisille jätettäviä alueita ei ole tunnistettu.** Iso osa keskeneräisistä on säänneltyä: KYC ja rahanpesän estäminen, sähköiset allekirjoitukset, varainsiirtovero ja DIAS. Ne kuuluvat agenttisessa mallissa alueille, joihin automaattinen korjaaja ei koske.

## Ehdotus siirtymän järjestykseksi

1. **Annetaan FI I:n valmistua nykyisellä tavalla.** Seitsemää viimeistä kohtaa ei kannata häiritä, koska Kivin korvaaminen on liiketoiminnan kannalta tärkein yksittäinen asia.
2. **Pilotoidaan rajatulla alueella.** Hyviä ehdokkaita ovat MML-, PRH- ja KVKL-integraatiot, joissa on selkeä ulkoinen rajapinta ja testattava lopputulos. Toinen vaihtoehto on markkinoinnin työkalut (uutiskirjeet, tapahtumakutsut), joissa sääntelyriski on pieni.
3. **Rakennetaan perusta ennen vauhtia.** Siihen kuuluvat testit, automaattiset tarkistukset ja kirjatut päätökset. Ilman niitä agentit lisäävät tuotosta ja heikentävät vakautta, juuri kuten DORA-tutkimus kuvaa.
4. **Määritellään ES/FR-tietomalli kerran**, maakohtaiset erot erotettuina, ja vasta sitten skaalataan.

## Kysymyksiä CTO:lle

1. Kuka koodin tekee tällä hetkellä: oma tiimi vai ulkoistettu, ja kuinka monta ihmistä?
2. Millainen testikattavuus ja julkaisuputki on, ja kuinka usein tuotantoon viedään?
3. Käytetäänkö AI-työkaluja kehityksessä jo nyt?
4. Mitä "valmis" tarkoittaa? Onko se testattu, tuotannossa vai välittäjien käytössä?
5. Mikä estää FI I:n seitsemää viimeistä kohtaa valmistumasta?

## Muutoksen avaamisesta

CTO on tehnyt tämän roadmapin itse, ja agenttinen tapa muuttaa ennen kaikkea hänen omaa rooliaan, rakentamisesta päättämiseen ja tarkistamiseen. Siksi muutos kannattaa avata yhteisenä kehityssuuntana eikä korjauksena hänen tapaansa tehdä.
