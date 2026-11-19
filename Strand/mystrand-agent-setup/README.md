# MyStrand: agenttisen kehityksen suojakaiteet (pohja)

Ehdotus MyStrandin koodirepoon. Kansion sisältö kopioidaan sellaisenaan MyStrand-repon juureen. Pohja on tehty 19.11.2026 tueksi keskusteluun Ville Hjeltin kanssa, eikä sitä ole vielä sovitettu MyStrandin teknologiapinoon.

## Periaate

Agentille kirjoitettu ohje on toive, ei suojakaide. Jokainen sääntö kirjoitetaan kerran tiedostoon `policy/rules.yaml`, ja sen noudattaminen varmistetaan koneellisesti useassa kerroksessa, joita agentti ei voi itse ohittaa:

| Kerros | Tiedosto | Pakottaako |
| --- | --- | --- |
| 1. Säännöt ja luokittelu | `policy/` | Lähde kaikelle muulle |
| 2. Agentin ohjeet | `CLAUDE.md` | Ei, ohjaa |
| 3. Agentin ajonaikaiset rajoitukset | `.claude/settings.json`, `.claude/hooks/` | Kyllä: estää lukemisen ja muokkaukset ennen kuin ne tapahtuvat |
| 4. Repon portit | `.github/workflows/security.yml`, `semgrep/`, `scripts/` | Kyllä: pakolliset tarkistukset ennen mergeä |
| 5. Riippumaton katselmointi | `.claude/agents/security-reviewer.md`, `.github/workflows/agent-review.yml` | Kyllä: hylkäys estää mergen |
| 6. Ihmisen hyväksyntä | `.github/CODEOWNERS` | Kyllä: no-fly-alueet ja suojakaiteet itse |
| 7. Julkaisu ja todisteet | `.github/workflows/release-evidence.yml` | Kyllä: julkaisusta jää todistusaineisto |

## Sisältö

```
CLAUDE.md                              agentin pysyvät ohjeet
policy/rules.yaml                      sääntörekisteri: tunniste, omistaja, valvonta, todiste
policy/data-map.yaml                   henkilötietojen luokittelu kentittäin
policy/no-fly.yaml                     polut, joihin agentti ei koske
policy/threat-model.md                 uhkamallin runko
.claude/settings.json                  oikeudet ja hookit
.claude/hooks/guard_paths.py           estää no-fly- ja suojakaidetiedostojen muokkauksen
.claude/hooks/guard_bash.py            estää vaaralliset komennot
.claude/agents/security-reviewer.md    riippumaton tietoturva- ja tietosuojakatselmoija
.github/CODEOWNERS                     ihmisen hyväksyntä herkkiin polkuihin
.github/workflows/security.yml         pakolliset tarkistukset jokaiseen PR:ään
.github/workflows/agent-review.yml     katselmointiagentti jokaiseen PR:ään
.github/workflows/release-evidence.yml julkaisun todistusaineisto
semgrep/gdpr-security.yml              omat staattisen analyysin säännöt
scripts/policy_check.py                tarkistaa sääntörekisterin ja tuottaa vaatimusmatriisin
scripts/check_data_map.py              tarkistaa, että jokainen kenttä on luokiteltu
```

## Käyttöönotto

1. **Sovita polut.** Korvaa `policy/no-fly.yaml`:n ja `CODEOWNERS`:n esimerkkipolut (`src/kyc/**` jne.) MyStrandin todellisilla poluilla.
2. **Täytä tietoluokittelu.** Käy `policy/data-map.yaml` läpi tietosuojavastaavan kanssa.
3. **Lisää pinokohtainen kenttälistaus.** `scripts/check_data_map.py` lukee tiedoston `build/schema-fields.txt` (yksi `taulu.kenttä` per rivi). Sen tuottaa pinon oma skripti, esim. ORM-skeemasta.
4. **Ota haarasuojaus käyttöön** `main`-haaraan: pakolliset tarkistukset `security` ja `agent-review`, CODEOWNERS-hyväksyntä, ei suoria pusheja, ei force pushia. Agentin GitHub-tokenilla ei saa olla ylläpitäjän oikeuksia.
5. **Aseta salaisuudet:** `ANTHROPIC_API_KEY` sekä todistearkiston tunnukset. Agentin ympäristöön ei tuotannon tunnuksia.
6. **Aloita varovasti.** Aja katselmointia ensin raportoivana kaksi viikkoa, säädä väärät hälytykset pois, ja tee siitä vasta sitten pakollinen.

## Avoimet kohdat (TODO)

- MyStrandin teknologiapino: Semgrep-säännöt on kirjoitettu TypeScript/JavaScript-oletuksella.
- Todistearkiston sijainti (esim. tallennussäilö, jossa tiedostoja ei voi muuttaa säilytysaikana).
- Tietosuojavastaavan nimeäminen sääntöjen hyväksyjäksi.
- `claude-code-action`-version ja syötteiden tarkistus käyttöönottohetkellä.
