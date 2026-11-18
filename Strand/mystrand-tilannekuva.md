# MyStrand – tilannekuva

Elävä dokumentti MyStrandista ja sen kehittämisestä. Jokainen MyStrandia koskeva keskustelu, tapaaminen ja dokumentti päivittää tätä tiedostoa: uusi tieto lisätään oikeaan osioon ja lähde kirjataan lokiin. Merkintä **(tarkista)** tarkoittaa tulkintaa, jota ei ole vielä vahvistettu.

Päivitetty: 18.11.2026

## Ihmiset ja roolit

| Henkilö | Rooli | Huomioita |
| --- | --- | --- |
| Anssi | Strandin perustaja | Hakee yhtiölle uutta toimitusjohtajaa. Vahva myyjä ja visionääri, hyvä saamaan asioita käyntiin. Luottaa Villeen, joka on hänen vanha tuttunsa. |
| Ville Hjelt | Strandin CTO ja MyStrandin product owner, roadmapin tekijä | Tuonut perustoiminnallisuudet välittäjille modernilla tavalla. Kaipaa vahvistusta omille ajatuksilleen. Mikan mukaan Villen näkemyksiä pitää kyseenalaistaa. |
| CFO | Strandin talousjohtaja | Sanoo asiat suoraan. Tuntee Anssin pitkältä ajalta. |
| Mika Viskari | Strandin hallituksen jäsen | Ajaa siirtymää agenttiseen kehitykseen. Omistaa Pataluhan yhdessä Antti Mäkelän (Reaktorin perustaja) kanssa. |
| Pataluhan CTO | Ulkopuolinen apu | Pataluha on Mika Viskarin ja Antti Mäkelän yhtiö. Sen CTO on auttanut Villeä. |
| Reaktor | Kehityskumppani sweat equity -mallilla | 3–4 henkeä nyt, 1–2 siirtymävaiheessa. |

## Nykytila

- **Tekeminen:** 3–5 hengen tiimi on rakentanut MyStrandin käsin, osin Reaktorin sweat equity -mallilla. Mikan mukaan malli on luonut vääristyneet kannustimet, eikä kiirettä ole ollut.
- **Tekoäly:** AI-natiivia ajattelua on tuotu viimeisen 3–6 kuukauden aikana, mutta AI-ominaisuudet ovat päälle liimattuja.
- **Tuote:** roadmapin mukaan FI I (Kivin korvaaminen) on lähes valmis: 26 ominaisuutta valmiina, 7 kesken. Ks. [`arvio-mystrand-roadmapista.md`](./arvio-mystrand-roadmapista.md).
- **Edessä:** koodin refaktorointi AI-natiiviksi.

## Tavoitetila kehitykselle

- Nopeammin tehoja irti ja nopeammat julkaisut.
- Ville product ownerina ja yksi seniorikoodari pyörittävät kokonaisuutta agenttien avulla.
- Reaktorin työ siirretään nopeasti pois (1–2 henkeä siirtymävaiheessa).
- Mikan vertailukohta: SolidMaint, tekoälypohjainen kiinteistönhallintajärjestelmä. Siinä on kenttähenkilöstön sovellus, asiakkaiden sovellus (property vault) ja laaja ERP/HQ-sovellus, yhteensä noin 1,4 miljoonaa riviä koodia. Viskarin dekki ([`presenting-how-we-work-deck.md`](./presenting-how-we-work-deck.md)) kuvaa todennäköisesti SolidMaintin kehitystä.
- **Kehitykseen mukaan välittäjät:** välittäjien palaute, nauhoitetut haastattelut ja ideat puuttuvista ominaisuuksista, jotka hyväksytään ennen toteutusta.

## Arvolupaus välittäjälle

- Välittäjä, joka tekee muualla 100 000 € välityspalkkioita, tekee Strandilla 200 000 €, koska Strand tehostaa työtä.
- Välittäjä keskittyy välittämiseen, ei admin-työhön, esimerkiksi uuden kohteen listaamiseen.
- Kivijalkaan ei tarvitse laittaa rahaa.

## Strandin vahvuudet ja painopisteet (Mikan näkemys)

- Teknologia on hyvä, brändi on hyvä.
- Rekrytointi on avain: välittäjien houkuttelu perustuu markkinadataan, ja se vaatii todisteita ("show me the truth").
- Jatkuva markkinadatan keräys (crawlaus) tukee rekrytointia.
- Uuden toimitusjohtajan kannattaa sopia Anssin kanssa, missä Anssi tuo eniten arvoa: välittäjien rekrytoinnissa ja sen ymmärtämisessä, miksi kentältä kannattaa tulla Strandille.

## Avoimet kysymykset

- Mikä on Sowise, josta roadmapissa siirretään dataa?
- Mitä "valmis" tarkoittaa roadmapissa?
- Rakennetaanko vai ostetaanko perustoiminnot markkina kerrallaan? Ks. markkina-analyysi.
- Miten Reaktorin sweat equity -sopimus puretaan tai muutetaan siirtymässä?

## Lähteet ja loki

| Päivä | Lähde | Mitä lisättiin |
| --- | --- | --- |
| 18.11.2026 | Tapaaminen Mika Viskarin kanssa | Ihmiset ja roolit, nykytila, tavoitetila, arvolupaus, painopisteet |
| 18.11.2026 | CTO:n roadmap ([`mystrand-roadmap.pdf`](./mystrand-roadmap.pdf)) ja [arvio](./arvio-mystrand-roadmapista.md) | Tuotteen tila |
| 18.11.2026 | Viskarin dekki ja [arvio](./arvio-viskarin-dekista.md) | Vertailukohta agenttiselle kehitykselle |
| 18.11.2026 | [Markkina-analyysi FI/ES/FR](https://claude.ai/artifact/MCP2yynpSirwNwZY4TYZSL) | Roadmapin aukot markkinoittain |
