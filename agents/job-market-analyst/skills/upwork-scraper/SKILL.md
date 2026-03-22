# Skill: Remote Work Platforms — Job Scraper & Market Analyzer
**Agent:** job-market-analyst  
**Verzia:** 2.0  
**Naposledy aktualizovaný:** 2026-03-22  

---

## Čo tento skill robí
Analyzuje aktuálne job postingy na remote work platformách (primárne Upwork, ale aj ďalších 24 platformách) podľa zadanej kategórie alebo kľúčového slova. Vracia štatistiky o dopyte, budgetoch, požadovaných skillsoch a frekvencii postingov. Obsahuje aj knowledge bázu o dostupných vzdelávacích zdrojoch.

---

## 📂 Knowledge Base — Remote Work Platforms (2026)

### 🔥 Primárne freelance platformy (USD platby)
| Platforma | URL | Typ | Poznámka |
|-----------|-----|-----|----------|
| Upwork | upwork.com | Freelance marketplace | Najväčší, hodinovka + fixed |
| Freelancer | freelancer.com | Freelance marketplace | Súťaže + projekty |
| Toptal | toptal.com | Premium freelance | Top 3% freelancerov |
| Fiverr | fiverr.com | Gig marketplace | Fixed-price gigs |

### 🌍 Remote job boards (plné úväzky + kontrakty)
| Platforma | URL | Špecializácia |
|-----------|-----|---------------|
| Remote OK | remoteok.com | Tech + marketing |
| We Work Remotely | weworkremotely.com | Tech + design |
| Remote.co | remote.co | Všetky kategórie |
| FlexJobs | flexjobs.com | Vetované remote pozície |
| Working Nomads | workingnomads.com | Developer-focused |
| Jobspresso | jobspresso.co | Tech + marketing |
| AngelList | angel.co | Startupy + tech |
| LinkedIn | linkedin.com | B2B network + jobs |
| SimplyHired | simplyhired.com | Aggregátor |
| Virtual Vocations | virtualvocations.com | Remote-only |
| Outsourcely | outsourcely.com | Remote teams |
| Remotive | remotive.com | Tech remote jobs |
| NoDesk | nodesk.co | Remote lifestyle + jobs |
| Remote4Me | remote4me.com | Remote job aggregátor |
| Pangian | pangian.com | Remote community |
| Remotees | remotees.com | Developer jobs |
| justremote | justremote.co | Vetované remote |
| Remotecrew | remotecrew.io | Remote teams |

### 🌐 Regionálne platformy
| Platforma | URL | Región |
|-----------|-----|--------|
| Europe Remotely | europeremotely.com | Európa |
| Remote OK Europe | remoteok.io/europe | Európa |
| Remote of Asia | remoteok.io/asia | Ázia |
| RemoteHabits | remotehabits.com | Globálne (lifestyle) |

---

## 🎓 Knowledge Base — Free Courses 2026 (Google, IBM, Microsoft)

### Google kurzy (Coursera — zdarma audit)
- **Google Introduction to Generative AI** — https://lnkd.in/ggbGgmGP
- **Foundations of Project Management** — https://lnkd.in/gP-h_Qpq
- **Google Project Management** (certifikát) — https://lnkd.in/gNAapb_x
- **Google Digital Marketing & E-commerce** — https://lnkd.in/g2i68zzz
- **Google IT Support** (certifikát) — https://lnkd.in/gzvpYfwG
- **Google Data Analytics** (certifikát) — https://lnkd.in/g-tjpeqe
- **Google Cybersecurity** — https://lnkd.in/g6qBj_in
- **Google UX Design** — https://lnkd.in/gcpVd5ng
- **Google Get Started with Python** — https://lnkd.in/gV3ArxMj
- **Google Advanced Data Analytics Capstone** — https://lnkd.in/e5cS_8p2
- **Google AI Essentials** — https://lnkd.in/e_pMiVZD
- **10,000+ kurzov (Google)** — https://lnkd.in/gWtS8UZW

### AI/ML špeciálizácie (Coursera)
- **Machine Learning Specialization** (Andrew Ng) — https://lnkd.in/gqmHE_T2
- **Deep Learning Specialization** (Andrew Ng) — https://lnkd.in/gSb_nCPT
- **AI for Everyone** — https://lnkd.in/e3GyxQKV
- **Generative AI with Large Language Models** — https://lnkd.in/e_7s-aUu
- **Generative AI for Everyone** — https://lnkd.in/e_7s-aUu
- **Introduction to Generative AI Learning Path** (Google Cloud) — https://lnkd.in/eQ8BDA5B
- **Prompt Engineering for ChatGPT** — https://lnkd.in/erdE5Snz

### IBM kurzy
- **IBM Python for Data Science, AI & Development** — https://lnkd.in/ggG5suCz
- **IBM Generative AI Engineering** — https://lnkd.in/epbuc7Qd
- **IBM RAG and Agentic AI** — https://lnkd.in/ezuiGRB2

### Microsoft kurzy
- **Microsoft AI Product Manager** — https://lnkd.in/efbXbxds
- **Microsoft AI & ML Engineering** — https://lnkd.in/eHEwy_-v

### Web Development
- **Web Applications for Everybody Specialization** — https://lnkd.in/gHQY-yWm

---

## Vstup
- Kategória alebo kľúčové slovo (napr. "Python developer", "AI content writer")
- Platforma (default: Upwork; alebo "all" pre multi-platform scan)
- Časové okno (napr. "posledných 30 dní")
- Nepovinné: geografický filter (US, EU, global)

## Postup (krok za krokom)
1. Vyhľadaj na Upwork.com daný keyword (search URL: `https://www.upwork.com/nx/search/jobs/?q=[keyword]`)
2. Zaznameň: počet postingov, budget range (hourly/fixed), required skills, klient rating
3. Identifikuj top 10 postingov podľa popularity (počet applicants)
4. Štatisticky zhrň: priemerný budget, medián, top skillsy, typy kontraktov
5. Porovnaj s predchádzajúcim obdobím ak existujú historické dáta v lessons-learned.md

## Výstup (formát súboru)
```markdown
# Upwork Analysis: [Keyword]
Dátum: [dátum]
Analyzovaných postingov: [N]

## Kľúčové štatistiky
- Priemerný hodinový rate: $X–$Y
- Priemerný fixed budget: $X–$Y
- Typ kontraktu: X% hourly / Y% fixed

## Top požadované skills
1. [skill] — [frekvencia]
2. ...

## Odporúčanie
[čo to znamená pre freelancera]
```

## Nástroje
- Web search pre aktuálne dáta
- Invoke-WebRequest pre priamy scraping (ak nie je blokovaný)
- Manuálna analýza top 10 výsledkov
- ESPN / TheSportsDB API (vzorový príklad pre štruktúrované dáta)

## Chyby a riešenia
- **Upwork blokuje scraping:** Použi Google search `site:upwork.com [keyword]`
- **Málo dát:** Rozšír keyword (napr. "Python" namiesto "Python Django REST API")
- **Platforma nedostupná:** Skús alternatívu z knowledge base (pozri sekciu platformy vyššie)

## Odporúčané platformy pre konkrétne profily
- **Developer/AI engineer:** Upwork, Toptal, We Work Remotely, AngelList
- **Designer/UX:** Upwork, Fiverr, justremote
- **Marketing/Content:** Upwork, Freelancer, Jobspresso, Remote.co
- **Data Analyst:** Upwork, LinkedIn, FlexJobs, Working Nomads
- **European candidates:** Europe Remotely, Remote OK Europe, LinkedIn
