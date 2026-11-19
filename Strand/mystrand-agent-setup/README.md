# MyStrand: agenttisen kehityksen suojakaiteet (pohja)

Ehdotus MyStrandin agenttiseen kehitykseen, tehty 19.11.2026 tueksi keskusteluun Ville Hjeltin kanssa. Pohjaa ei ole vielä sovitettu MyStrandin teknologiapinoon.

## Periaate

Agentille kirjoitettu ohje on toive, ei suojakaide. Repoa muuttaa useampi työkalu (Claude Code, Linearin agentit, ihmiset omilla työkaluillaan), eikä niitä kaikkia voi pakottaa samoihin asetuksiin. Siksi takuu rakennetaan paikkaan, jonka kautta jokaisen muutoksen on pakko kulkea: GitHubiin ja julkaisuputkeen.

| Taso | Missä | Voiko ohittaa | Rooli |
| --- | --- | --- | --- |
| 1. Työkalun sisällä | `AGENTS.md`, `CLAUDE.md`, `.claude/` | Kyllä | Pysäyttää virheet aikaisin ja halvalla |
| 2. GitHub | Organisaation ruleset, keskitetyt työnkulut, CODEOWNERS | Ei | Varsinainen takuu: mikään ei pääse päähaaraan ilman näitä |
| 3. Julkaisu | Tuotantoympäristö ja alkuperätarkistus | Ei | Tuotantoon menee vain CI:ssä rakennettu ja tarkistettu versio |
| Valvonta | Päivittäinen asetusvalvonta | Ei | Hälyttää, jos tasoja 2–3 heikennetään |

## Kaksi repoa

**`app-repo/`** kopioidaan MyStrand-repon juureen. Se sisältää tuotteen omat säännöt ja agenttien ohjeet:

```
AGENTS.md                              ohjeet kaikille koodaaville agenteille
CLAUDE.md                              tuo AGENTS.md:n ja lisää Claude Coden erityisohjeet
policy/rules.yaml                      sääntörekisteri (21 sääntöä)
policy/data-map.yaml                   henkilötietojen luokittelu kentittäin
policy/no-fly.yaml                     polut, joihin agentti ei koske
policy/threat-model.md                 uhkamallin runko
.claude/settings.json, .claude/hooks/  Claude Coden oikeudet ja estot
.github/CODEOWNERS                     ihmisen hyväksyntä herkkiin polkuihin
.github/workflows/release-deploy.yml   julkaisu, todistepaketti ja alkuperätarkistus ennen deployta
```

**`security-repo/`** on oma, lukittu repo (esim. `strand/security-workflows`). MyStrandin PR ei voi muuttaa sen sisältöä, joten tarkistuksia ei voi heikentää muokkaamalla niitä samassa PR:ssä:

```
.github/workflows/mystrand-security.yml      pakolliset tarkistukset jokaiseen PR:ään
.github/workflows/mystrand-agent-review.yml  riippumaton katselmointiagentti jokaiseen PR:ään
.github/workflows/settings-drift.yml         päivittäinen asetusvalvonta ja Slack-hälytys
reviewer/security-reviewer.md                katselmoijan ohjeet
semgrep/gdpr-security.yml                    staattisen analyysin säännöt
scripts/                                     policy_check, check_data_map, check_drift
settings/ruleset-mystrand-main.json          organisaation ruleset koodina
```

## Käyttöönotto

1. **Luo security-workflows-repo** organisaatioon. Vain CTO:lla on kirjoitusoikeus, eikä yksikään agentti saa oikeuksia siihen.
2. **Ota organisaation ruleset käyttöön** tiedostosta `settings/ruleset-mystrand-main.json` GitHubin rajapinnan tai käyttöliittymän kautta. Korvaa `repository_id: 0` security-workflows-repon tunnisteella. Ohitusoikeuksien lista pidetään tyhjänä, myös ylläpitäjiltä.
3. **Anna jokaiselle agentille oma GitHub-identiteetti** (Claude Coden GitHub-sovellus, Linearin agentin integraatio). Oikeus avata PR, mutta ei hyväksyä, ohittaa tai muuttaa asetuksia (SEC-012). Käy oikeudet läpi neljännesvuosittain.
4. **Sovita polut ja pino:** `no-fly.yaml`, `CODEOWNERS`, Semgrep-säännöt (nyt TypeScript-oletus) ja pinokohtainen kenttälistaus tiedostoon `build/schema-fields.txt`.
5. **Täytä tietoluokittelu** tietosuojavastaavan kanssa ja lisää Slack, Linear ja AI-palvelut käsittelytoimien selosteeseen (GDPR-008).
6. **Aseta salaisuudet:** `ANTHROPIC_API_KEY`, `SECURITY_REPO_READ_TOKEN`, asetusvalvonnan GitHub-sovellus (`DRIFT_APP_ID`, `DRIFT_APP_PRIVATE_KEY`) ja `SLACK_SECURITY_WEBHOOK`.
7. **Suojaa tuotantoympäristö:** GitHub Environment `production` ja vaadittu hyväksyjä no-fly-alueita koskeville julkaisuille.
8. **Aloita varovasti:** aja katselmointia ensin raportoivana pari viikkoa ja tee siitä vasta sitten pakollinen rulesetissä.

## Avoimet kohdat (TODO)

- MyStrandin teknologiapino ja todelliset polut
- Todistearkiston sijainti (tallennussäilö, jossa tiedostoja ei voi muuttaa säilytysaikana)
- Tietosuojavastaavan nimeäminen
- Tarkista käyttöönottohetkellä `claude-code-action`-version syötteet sekä rulesetin `workflows`- ja `pull_request`-sääntöjen parametrit GitHubin ajantasaisesta dokumentaatiosta
- Mitkä Linearin agentit saavat kirjoittaa repoon, ja millä identiteetillä
