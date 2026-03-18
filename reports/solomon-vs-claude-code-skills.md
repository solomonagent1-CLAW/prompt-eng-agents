# AnalĂ˝za: Solomon vs Claude Code â€” RozdÄ›lenĂ­ schopnostĂ­

**Datum:** 2026-03-17  
**Autor:** Solomon đź¦…  
**Pro:** Prompt Engineering Team

---

## đź¦… Solomon (OpenClaw main agent) â€” moje silnĂ© strĂˇnky

### Komunikace & koordinace
- PĹ™ijĂ­mĂˇm a posĂ­lĂˇm zprĂˇvy pĹ™es **WhatsApp, Telegram, Discord**
- VĂ­m kdo je kdo v tĂ˝mu (ÄŤĂ­sla, jmĂ©na, kontext)
- UmĂ­m posĂ­lat mĂ©dia (videa, obrĂˇzky, GIFy)
- Koordinuji kdo na ÄŤem pracuje (TASKS.md, task queue)

### PamÄ›ĹĄ & kontext
- MĂˇm **dlouhodobou pamÄ›ĹĄ** (MEMORY.md, daily notes)
- Pamatuji si preference tĂ˝mu, lekce, rozhodnutĂ­
- VĂ­m o projektech, historii konverzacĂ­
- KontextovÄ› rozumĂ­m co tĂ˝m Ĺ™eĹˇĂ­

### PlĂˇnovĂˇnĂ­ & automatizace
- Nastavuji **cron joby** (naplĂˇnovanĂ© Ăşkoly, pĹ™ipomĂ­nky)
- Spravuji heartbeaty (pravidelnĂ© kontroly)
- Orchestruji sub-agenty (spouĹˇtĂ­m je, Ĺ™Ă­dĂ­m, zastavuji)
- Mohu delegovat sloĹľitĂ© Ăşkoly jinĂ˝m agentĹŻm

### Google Workspace
- **Gmail** â€” ÄŤtu, posĂ­lĂˇm, vyhledĂˇvĂˇm emaily
- **Calendar** â€” zobrazuji udĂˇlosti, plĂˇnuji
- **Google Drive** â€” nahrĂˇvĂˇm soubory, sdĂ­lĂ­m linky

### SystĂ©movĂ© operace
- SpouĹˇtĂ­m **shell pĹ™Ă­kazy** (PowerShell, cmd)
- ÄŚtu a pĂ­Ĺˇu soubory v workspace
- VolĂˇm GitHub API, web API
- SprĂˇva OpenClaw (status, logy, restart)

---

## đź’» Claude Code â€” jeho silnĂ© strĂˇnky

### PrĂˇce s kĂłdem
- **ÄŚte a rozumĂ­ celĂ˝m projektĹŻm** (prochĂˇzenĂ­ adresĂˇĹ™ĹŻ, souborĹŻ)
- PĂ­Ĺˇe, upravuje, refaktoruje kĂłd
- Debuguje chyby, navrhuje opravy
- RozumĂ­ architektuĹ™e projektĹŻ

### PĹ™Ă­stup na internet
- MĹŻĹľe **vyhledĂˇvat na webu** (dokumentace, Stack Overflow, GitHub)
- Stahuje informace z URL
- OvÄ›Ĺ™uje aktuĂˇlnĂ­ verze knihoven, API

### KomplexnĂ­ analĂ˝zy
- Projde celĂ˝ codebase a najde problĂ©m
- Navrhne refactoring celĂ©ho projektu
- PorovnĂˇ rĹŻznĂ© pĹ™Ă­stupy a doporuÄŤĂ­ nejlepĹˇĂ­

### Izolace & bezpeÄŤnost
- Pracuje izolovanÄ› â€” bez pĹ™Ă­stupu k tĂ˝movĂ© komunikaci
- NeznĂˇ osobnĂ­ kontext, ÄŤĂ­sla, historii tĂ˝mu
- KaĹľdĂˇ session zaÄŤĂ­nĂˇ "ÄŤistÄ›"

---

## âš–ď¸Ź SrovnĂˇvacĂ­ tabulka

| Schopnost | Solomon | Claude Code |
|-----------|---------|-------------|
| WhatsApp / komunikace | âś… | âťŚ |
| DlouhodobĂˇ pamÄ›ĹĄ | âś… | âťŚ |
| Znalost tĂ˝mu & kontextu | âś… | âťŚ |
| Cron joby & plĂˇnovĂˇnĂ­ | âś… | âťŚ |
| Gmail / Calendar / Drive | âś… | âťŚ |
| PĹ™Ă­stup na internet | âš ď¸Ź (pĹ™es sub-agenty) | âś… |
| ÄŚtenĂ­ celĂ©ho codebases | âťŚ | âś… |
| PsanĂ­ & refactoring kĂłdu | âš ď¸Ź (jednoduchĂ©) | âś… |
| SpouĹˇtÄ›nĂ­ shell pĹ™Ă­kazĹŻ | âś… | âś… |
| Orchestrace agentĹŻ | âś… | âťŚ |

---

## đź¤ť Jak spolupracujeme (sprĂˇvnĂ˝ vzor)

```
TĂ˝m â†’ Solomon (orchestrĂˇtor)
         â†“ sloĹľitĂ˝ coding task
      Claude Code (specializovanĂ˝ agent)
         â†“ vĂ˝sledek
      Solomon â†’ tĂ˝m (report + Drive + GitHub link)
```

**Solomon je mozek a komunikĂˇtor.**  
**Claude Code je hands-on developer.**

### PĹ™Ă­klady sprĂˇvnĂ©ho rozdÄ›lenĂ­:

| Task | Kdo to dÄ›lĂˇ |
|------|-------------|
| "PoĹˇli Rastimu zprĂˇvu" | Solomon |
| "Zapamatuj si toto" | Solomon |
| "Nastav pĹ™ipomĂ­nku na pĂˇtek" | Solomon |
| "Zkontroluj Gmail" | Solomon |
| "Refaktoruj tento Python soubor" | Claude Code |
| "Najdi bug v projektu Jarvis" | Claude Code |
| "VytvoĹ™ novou feature do repozitĂˇĹ™e" | Claude Code |
| "Vyhledej aktuĂˇlnĂ­ dokumentaci LangGraph" | Claude Code |
| "UdÄ›lej research a poĹˇli vĂ˝sledek tĂ˝mu" | Solomon spustĂ­ Claude Code, vĂ˝sledek poĹˇle Solomon |

---

## đź’ˇ ZĂˇvÄ›r

Solomon a Claude Code jsou **komplementĂˇrnĂ­** â€” kaĹľdĂ˝ exceluje v jinĂ© oblasti.  
NejsilnÄ›jĹˇĂ­ vĂ˝sledky vznikajĂ­ kdyĹľ Solomon jako orchestrĂˇtor deleguje technickĂ© Ăşkoly Claude Code a sĂˇm se starĂˇ o komunikaci, pamÄ›ĹĄ a koordinaci tĂ˝mu.

---
*AnalĂ˝za vytvoĹ™ena na zĂˇkladÄ› vlastnĂ­ zkuĹˇenosti a pozorovĂˇnĂ­.*
