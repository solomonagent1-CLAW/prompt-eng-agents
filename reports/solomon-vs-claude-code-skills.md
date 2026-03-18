# Analýza: Solomon vs Claude Code — Rozdělení schopností

**Datum:** 2026-03-17  
**Autor:** Solomon 🦅  
**Pro:** Prompt Engineering Team

---

## 🦅 Solomon (OpenClaw main agent) — moje silné stránky

### Komunikace & koordinace
- Přijímám a posílám zprávy přes **WhatsApp, Telegram, Discord**
- Vím kdo je kdo v týmu (čísla, jména, kontext)
- Umím posílat média (videa, obrázky, GIFy)
- Koordinuji kdo na čem pracuje (TASKS.md, task queue)

### Paměť & kontext
- Mám **dlouhodobou paměť** (MEMORY.md, daily notes)
- Pamatuji si preference týmu, lekce, rozhodnutí
- Vím o projektech, historii konverzací
- Kontextově rozumím co tým řeší

### Plánování & automatizace
- Nastavuji **cron joby** (naplánované úkoly, připomínky)
- Spravuji heartbeaty (pravidelné kontroly)
- Orchestruji sub-agenty (spouštím je, řídím, zastavuji)
- Mohu delegovat složité úkoly jiným agentům

### Google Workspace
- **Gmail** — čtu, posílám, vyhledávám emaily
- **Calendar** — zobrazuji události, plánuji
- **Google Drive** — nahrávám soubory, sdílím linky

### Systémové operace
- Spouštím **shell příkazy** (PowerShell, cmd)
- Čtu a píšu soubory v workspace
- Volám GitHub API, web API
- Správa OpenClaw (status, logy, restart)

---

## 💻 Claude Code — jeho silné stránky

### Práce s kódem
- **Čte a rozumí celým projektům** (procházení adresářů, souborů)
- Píše, upravuje, refaktoruje kód
- Debuguje chyby, navrhuje opravy
- Rozumí architektuře projektů

### Přístup na internet
- Může **vyhledávat na webu** (dokumentace, Stack Overflow, GitHub)
- Stahuje informace z URL
- Ověřuje aktuální verze knihoven, API

### Komplexní analýzy
- Projde celý codebase a najde problém
- Navrhne refactoring celého projektu
- Porovná různé přístupy a doporučí nejlepší

### Izolace & bezpečnost
- Pracuje izolovaně — bez přístupu k týmové komunikaci
- Nezná osobní kontext, čísla, historii týmu
- Každá session začíná "čistě"

---

## ⚖️ Srovnávací tabulka

| Schopnost | Solomon | Claude Code |
|-----------|---------|-------------|
| WhatsApp / komunikace | ✅ | ❌ |
| Dlouhodobá paměť | ✅ | ❌ |
| Znalost týmu & kontextu | ✅ | ❌ |
| Cron joby & plánování | ✅ | ❌ |
| Gmail / Calendar / Drive | ✅ | ❌ |
| Přístup na internet | ⚠️ (přes sub-agenty) | ✅ |
| Čtení celého codebases | ❌ | ✅ |
| Psaní & refactoring kódu | ⚠️ (jednoduché) | ✅ |
| Spouštění shell příkazů | ✅ | ✅ |
| Orchestrace agentů | ✅ | ❌ |

---

## 🤝 Jak spolupracujeme (správný vzor)

```
Tým → Solomon (orchestrátor)
         ↓ složitý coding task
      Claude Code (specializovaný agent)
         ↓ výsledek
      Solomon → tým (report + Drive + GitHub link)
```

**Solomon je mozek a komunikátor.**  
**Claude Code je hands-on developer.**

### Příklady správného rozdělení:

| Task | Kdo to dělá |
|------|-------------|
| "Pošli Rastimu zprávu" | Solomon |
| "Zapamatuj si toto" | Solomon |
| "Nastav připomínku na pátek" | Solomon |
| "Zkontroluj Gmail" | Solomon |
| "Refaktoruj tento Python soubor" | Claude Code |
| "Najdi bug v projektu Jarvis" | Claude Code |
| "Vytvoř novou feature do repozitáře" | Claude Code |
| "Vyhledej aktuální dokumentaci LangGraph" | Claude Code |
| "Udělej research a pošli výsledek týmu" | Solomon spustí Claude Code, výsledek pošle Solomon |

---

## 💡 Závěr

Solomon a Claude Code jsou **komplementární** — každý exceluje v jiné oblasti.  
Nejsilnější výsledky vznikají když Solomon jako orchestrátor deleguje technické úkoly Claude Code a sám se stará o komunikaci, paměť a koordinaci týmu.

---
*Analýza vytvořena na základě vlastní zkušenosti a pozorování.*
