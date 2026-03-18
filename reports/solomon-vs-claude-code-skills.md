# Analyza: Solomon vs Claude Code - Rozdeleni schopnosti

**Datum:** 2026-03-17
**Autor:** Solomon
**Pro:** Prompt Engineering Team

---

## Solomon (OpenClaw main agent) - moje silne stranky

### Komunikace & koordinace
- Prijimam a posilam zpravy pres **WhatsApp, Telegram, Discord**
- Vim kdo je kdo v tymu (cisla, jmena, kontext)
- Umim posilat media (videa, obrazky, GIFy)
- Koordinuji kdo na cem pracuje (TASKS.md, task queue)

### Pamet & kontext
- Mam **dlouhodobou pamet** (MEMORY.md, daily notes)
- Pamatuji si preference tymu, lekce, rozhodnuti
- Vim o projektech, historii konverzaci
- Kontextove rozumim co tym resi

### Planovani & automatizace
- Nastavuji **cron joby** (naplanovane ukoly, pripominky)
- Spravuji heartbeaty (pravidelne kontroly)
- Orchestruji sub-agenty (spoustim je, ridim, zastavuji)
- Mohu delegovat slozite ukoly jinym agentum

### Google Workspace
- **Gmail** - ctu, posilam, vyhledavam emaily
- **Calendar** - zobrazuji udalosti, planuji
- **Google Drive** - nahravem soubory, sdilim linky

### Systemove operace
- Spoustim **shell prikazy** (PowerShell, cmd)
- Ctu a pisu soubory v workspace
- Volam GitHub API, web API
- Sprava OpenClaw (status, logy, restart)

---

## Claude Code - jeho silne stranky

### Prace s kodem
- **Cte a rozumi celym projektum** (prochazeni adresaru, souboru)
- Pise, upravuje, refaktoruje kod
- Debuguje chyby, navrhuje opravy
- Rozumi architekture projektu

### Pristup na internet
- Muze **vyhledavat na webu** (dokumentace, Stack Overflow, GitHub)
- Stahuje informace z URL
- Overuje aktualni verze knihoven, API

### Komplexni analyzy
- Projde cely codebase a najde problem
- Navrhne refactoring celeho projektu
- Porovna ruzne pristupy a doporuci nejlepsi

### Izolace & bezpecnost
- Pracuje izolovaně - bez pristupu k tymove komunikaci
- Nezna osobni kontext, cisla, historii tymu
- Kazda session zacina "ciste"

---

## Srovnavaci tabulka

| Schopnost | Solomon | Claude Code |
|-----------|---------|-------------|
| WhatsApp / komunikace | YES | NO |
| Dlouhodoba pamet | YES | NO |
| Znalost tymu & kontextu | YES | NO |
| Cron joby & planovani | YES | NO |
| Gmail / Calendar / Drive | YES | NO |
| Pristup na internet | cástečne (pres sub-agenty) | YES |
| Cteni celeho codebases | NO | YES |
| Psani & refactoring kodu | cástečne (jednoduche) | YES |
| Spousteni shell prikazu | YES | YES |
| Orchestrace agentu | YES | NO |

---

## Jak spolupracujeme (spravny vzor)

```
Tym -> Solomon (orchestrator)
         | slozity coding task
      Claude Code (specializovany agent)
         | vysledek
      Solomon -> tym (report + Drive + GitHub link)
```

**Solomon je mozek a komunikator.**
**Claude Code je hands-on developer.**

### Priklady spravneho rozdeleni:

| Task | Kdo to dela |
|------|-------------|
| "Posli Rastimu zpravu" | Solomon |
| "Zapamatuj si toto" | Solomon |
| "Nastav pripominku na patek" | Solomon |
| "Zkontroluj Gmail" | Solomon |
| "Refaktoruj tento Python soubor" | Claude Code |
| "Najdi bug v projektu Jarvis" | Claude Code |
| "Vytvor novou feature do repozitare" | Claude Code |
| "Vyhledej aktualni dokumentaci LangGraph" | Claude Code |
| "Udelej research a posli vysledek tymu" | Solomon spusti Claude Code, vysledek posle Solomon |

---

## Zaver

Solomon a Claude Code jsou **komplementarni** - kazdy exceluje v jine oblasti.
Nejsilnejsi vysledky vznikaji kdyz Solomon jako orchestrator deleguje technicke ukoly Claude Code
a sam se stara o komunikaci, pamet a koordinaci tymu.

---
*Analyza vytvorena na zaklade vlastni zkusenosti a pozorovani.*