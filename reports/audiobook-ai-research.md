# Research: AI modely pro tvorbu audioknih z textu

> **Datum:** 23. března 2026 | **Autor:** Orel 🦅 | **Tým:** Prompt Eng, Kutná Hora

---

## Executive Summary

Současné AI modely **dokáží plnohodnotně převést text na audioknihu** — technologie za poslední 2 roky dramaticky pokročila. ElevenLabs je zlatým standardem pro kvalitu hlasu, Narratemi je jedinou platformou postavenou přímo pro audioknihy (parsování EPUB, detekce kapitol, multi-hlasové přiřazení). OpenAI TTS API nabízí nejlepší poměr cena/výkon pro vývojáře s limitem 4 096 znaků/request (vyžaduje dělení textu). Čeština je podporována primárně přes ElevenLabs, Google Cloud TTS a Microsoft Azure TTS — ostatní nástroje mají češtinu omezenou nebo nulovou. Kokoro TTS je nejlepší open-source alternativa pro team, který chce provozovat TTS lokálně bez API nákladů (nicméně češtinu zatím nepodporuje). Trh nabízí jak hotové SaaS produkty (ElevenLabs Studio, Narratemi, Murf, Play.ht), tak výkonné API přístupy (OpenAI, Google Cloud, Azure) — volba závisí na use-case: SaaS pro rychlé výsledky, API pro vlastní pipeline a škálovatelnost.

---

## Nejlepší dostupné nástroje

### 1. ElevenLabs Studio

- **Co umí:** Nahrání textu/skriptu → výběr hlasu → generování audioknihy. Má Studio funkci pro long-form obsah (knihy, podcasty, skripty). Supports voice cloning, multi-character casting, emotion controls. Nejpřirozenější hlasy na trhu.
- **Čeština:** ✅ ANO — dedikovaná Czech TTS stránka, model Flash v2.5 podporuje 32 jazyků, model Eleven v3 podporuje 74 jazyků
- **Cena:**
  - Free: 10 000 znaků/měsíc
  - Starter: ~$5/měsíc (30 000 znaků)
  - Creator: ~$22/měsíc (100 000 znaků)
  - Pro: ~$99/měsíc (500 000 znaků)
  - Typická 80 000 slovná kniha: **$50–150** (Creator/Pro plán)
- **Limity:**
  - Cenová fakturace per-karakter (nepředvídatelné náklady při iteracích)
  - Žádné nativní parsování EPUB/PDF
  - Ruční správa kapitol
  - Žádný automatický multi-character dialogue systém
- **Hodnocení:** ⭐⭐⭐⭐⭐ (nejlepší hlas na trhu, ale dražší pro long-form)

---

### 2. Narratemi

- **Co umí:** Platforma postavená **přímo pro audioknihy** — nativní EPUB upload, automatická detekce kapitol, přiřazení různých hlasů postavám, optimalizace pro dlouhé poslechové sezení, one-click generování.
- **Čeština:** ❓ Nepotvrzena (platforma je nová, 2025/2026, jazyková podpora není plně zdokumentována)
- **Cena:**
  - Free tier: 10 000 znaků (zdarma, bez kreditní karty)
  - Knihová fakturace (ne per-karakter — předvídatelné náklady bez ohledu na délku)
- **Limity:**
  - Nová platforma (méně komunitní dokumentace)
  - Menší výběr hlasů než ElevenLabs
- **Hodnocení:** ⭐⭐⭐⭐⭐ (nejlepší pro audioknihy specificky, nejintuitivnější workflow)

---

### 3. OpenAI TTS API (tts-1, tts-1-hd, gpt-4o-mini-tts)

- **Co umí:** REST API pro TTS. Tři modely:
  - `tts-1`: standard, nižší latence
  - `tts-1-hd`: HD kvalita, profesionální výstup
  - `gpt-4o-mini-tts`: multimodal, token-based, nejnovější
  - 13 hlasů (Alloy, Ash, Ballad, Coral, Echo, Fable, Nova, Onyx, Sage, Shimmer, Verse + Marin, Cedar)
  - Streaming podpora, výstupní formáty: MP3, Opus, AAC, FLAC, WAV, PCM
- **Čeština:** ✅ ANO — API automaticky detekuje jazyk, čeština funguje (bez explicitního nastavení)
- **Cena:**
  - tts-1: **$15 / 1M znaků**
  - tts-1-hd: **$30 / 1M znaků**
  - gpt-4o-mini-tts: $0.60 input + $12 audio output / 1M tokenů (~$0.015/min)
  - Audiobook kapitola (2 500 min/měs): ~$75–150/měsíc (HD)
- **Limity:**
  - **Maximum 4 096 znaků per request** → text je nutné dělit na chunky
  - Žádné nativní SaaS rozhraní (čistě API)
  - Žádný voice cloning
  - Omezená kontrola nad emocemi/dramatickými pauzami
- **Hodnocení:** ⭐⭐⭐⭐ (výborný pro vývojáře a vlastní pipeline, cenově dostupný)

---

### 4. Google Cloud TTS (WaveNet / Chirp / Gemini-TTS)

- **Co umí:** Enterprise-grade TTS. Nejnovější model **Gemini-TTS** (Gemini 2.5 Flash TTS) umožňuje:
  - Přirozený jazyk pro kontrolu tónu, tempa, emocí a stylu
  - Single i multi-speaker výstup
  - Long-form narration (knihy, vzdělávací obsah)
  - Streaming i unary výstup
  - Formáty: LINEAR16, ALAW, MULAW, MP3, OGG_OPUS, PCM
- **Čeština:** ✅ ANO — Google Cloud TTS podporuje češtinu (WaveNet hlasy)
- **Cena:**
  - WaveNet: ~$16 / 1M znaků
  - Neural2 / Chirp: vyšší cena (dle modelu)
  - Free tier: 1M WaveNet znaků/měsíc gratis
- **Limity:**
  - Složitější setup (GCP projekt, credentials, billing)
  - Gemini-TTS je nový (méně dokumentace pro audiobooks workflow)
  - Voice cloning není dostupný v základní verzi
- **Hodnocení:** ⭐⭐⭐⭐ (skvělý pro enterprise, čeština funguje, Gemini-TTS slibný)

---

### 5. Microsoft Azure TTS (Neural)

- **Co umí:** 400+ hlasů, 140+ jazyků, neural TTS s SSML podporou pro kontrolu pauz, tempa, emocí. Fine-tuning vlastního hlasu přes Custom Neural Voice.
- **Čeština:** ✅ ANO — Azure TTS má dedikované české neural hlasy (cs-CZ)
- **Cena:**
  - Standard Neural: ~$16 / 1M znaků
  - Custom Neural Voice: vyšší cena
  - Free tier: 500K znaků/měsíc
- **Limity:**
  - Vyžaduje Azure účet a billing setup
  - SSML tagging pro pokročilé kontroly (vyžaduje technické znalosti)
  - SaaS rozhraní pro audioknihy neexistuje — čistě API
- **Hodnocení:** ⭐⭐⭐⭐ (solidní pro enterprise a česky mluvící projekty)

---

### 6. Murf AI

- **Co umí:** 120+ AI hlasů v 20+ jazycích. Timeline editor pro synchronizaci s videem. Team workspaces, prezentační mód. Dobré pro marketing a e-learning.
- **Čeština:** ⚠️ OMEZENÁ — primárně anglicky, čeština není v hlavní nabídce
- **Cena:**
  - Starter: $29/měsíc
  - Pro: $39/měsíc
- **Limity:**
  - Není optimalizováno pro long-form (>10 000 slov)
  - Žádný EPUB upload, žádná detekce kapitol
  - Méně přirozené hlasy než ElevenLabs
- **Hodnocení:** ⭐⭐⭐ (dobré pro krátký obsah, marketing, videonarrace — ne pro audioknihy)

---

### 7. Play.ht (PlayAI)

- **Co umí:** Ultra-realistic hlasy s emotion controls. WordPress plugin pro blog-to-audio. Built-in podcast hosting. API pro automatizaci. Dobré pro long-form obsah a podcasty.
- **Čeština:** ⚠️ OMEZENÁ — není v primárním jazykovém výběru
- **Cena:**
  - Creator: $31/měsíc
  - Unlimited: $49/měsíc
- **Limity:**
  - Designováno pro články a blogy (ne knihy)
  - Žádné book-specific features (kapitoly, EPUB)
  - Character-based pricing pro dlouhý obsah
- **Hodnocení:** ⭐⭐⭐½ (dobrý pro podcasty a dlouhé články, limitovaný pro celé audioknihy)

---

### 8. Kokoro TTS (Open Source)

- **Co umí:** Open-weight TTS model, 82M parametrů, Apache 2.0 licence. CLI nástroj pro lokální provoz. Kaggle notebook pro generování audioknih z DOCX/PDF do FLAC souborů. Streamingová generace, phoneme notation system.
- **Čeština:** ❌ NE — podporuje: americká/britská angličtina, španělština, francouzština, japonština, korejština, čínština
- **Cena:** **ZDARMA** (self-hosted, žádné API poplatky)
- **Limity:**
  - Čeština nepodporována
  - Vyžaduje setup Python prostředí
  - Méně přirozené hlasy než ElevenLabs (ale nejlepší z open-source)
  - Žádné SaaS rozhraní
- **Hodnocení:** ⭐⭐⭐⭐ (výborný pro vývojáře, kteří chtějí zdarma lokální TTS bez češtiny)

---

### 9. Amazon Polly

- **Co umí:** AWS TTS service, Neural TTS hlasy, SSML podpora, REST API, streaming. Integrace s ostatními AWS službami.
- **Čeština:** ❌ NE — Czech není v seznamu podporovaných jazyků (Neural TTS)
- **Cena:**
  - Standard: $4 / 1M znaků
  - Neural: $16 / 1M znaků
  - Free tier: 5M znaků/měsíc po dobu 12 měsíců
- **Limity:**
  - Žádná podpora češtiny
  - Méně přirozené než ElevenLabs nebo Google Cloud
  - Čistě API (žádné SaaS pro audioknihy)
  - Limit 100 000 znaků per request (asynchronní)
- **Hodnocení:** ⭐⭐⭐ (levné a spolehlivé pro angličtinu v AWS ekosystému)

---

## Podpora češtiny

| Nástroj | Čeština | Kvalita | Poznámka |
|---|---|---|---|
| **ElevenLabs** | ✅ ANO | ⭐⭐⭐⭐⭐ | Dedikovaná Czech TTS, 32–74 jazyků dle modelu |
| **Google Cloud TTS** | ✅ ANO | ⭐⭐⭐⭐ | WaveNet cs-CZ hlasy, free tier 1M znaků |
| **Microsoft Azure TTS** | ✅ ANO | ⭐⭐⭐⭐ | Dedikované cs-CZ neural hlasy, SSML |
| **OpenAI TTS API** | ✅ ANO | ⭐⭐⭐½ | Automatická detekce, funguje, ale limitovaná kontrola |
| **Murf AI** | ⚠️ Omezená | ⭐⭐ | Není v hlavní nabídce |
| **Play.ht** | ⚠️ Omezená | ⭐⭐ | Není primárně podporována |
| **Kokoro TTS** | ❌ NE | — | Pouze en/es/fr/ja/ko/zh |
| **Amazon Polly** | ❌ NE | — | Czech chybí v neural hlasech |
| **Narratemi** | ❓ Neznámo | — | Nová platforma, nepotvrzeno |

**Doporučení pro česky mluvící projekty:**
1. **ElevenLabs** — nejlepší česká kvalita hlasu
2. **Azure TTS** — enterprise řešení s cs-CZ hlasy, SSML kontrola
3. **Google Cloud TTS** — solidní, levnější alternativa s free tier

---

## Workflow: Jak vytvořit audioknihu

### Metoda A — SaaS (bez kódování): ElevenLabs + Narratemi

```
1. PŘÍPRAVA TEXTU
   → Vyčisti rukopis (oprav překlepy, diakritiku, zkratky)
   → Přidej pronunciation notes (jména, odborné termíny)
   → Rozděl na kapitoly (každá jako samostatný soubor nebo sekce)

2. VOLBA PLATFORMY
   → Fiction s dialogy → Narratemi (multi-character) nebo ElevenLabs
   → Non-fiction → ElevenLabs Studio nebo Play.ht

3. GENEROVÁNÍ (ElevenLabs Studio)
   → Nahraj text / vlož do editoru
   → Vyber hlas (zkus sample first!)
   → Pro dialogy: přiřaď různé hlasy postavám
   → Nastav rychlost, pauzy, styl (calm / dramatic / cheerful)
   → Spusť generování po kapitolách

4. REVIEW & EDITING
   → Poslechni celý výstup
   → Oprav chybnou výslovnost (pronunciation dictionary)
   → Re-renderuj jen opravené sekce (šetří kredity)

5. POST-PROCESSING
   → Normalizace hlasitosti (Auphonic, Adobe Audition, Audacity)
   → ACX standardy: MP3 192kbps+, RMS -23dB až -18dB
   → Přidej úvod/outro, kapitolové markery

6. DISTRIBUCE
   → ACX (Audible/Amazon) / Findaway Voices / Author's Republic
   → Zkontroluj licenční podmínky (commercial use ✅)
```

### Metoda B — API Pipeline (pro vývojáře)

```python
# Pseudokód: OpenAI TTS API pro audioknihu

import openai, os

client = openai.OpenAI()

def text_to_audiobook(text: str, voice="nova", model="tts-1-hd"):
    # Rozděl text na chunky (max 4096 znaků, na přirozených breaks)
    chunks = split_text(text, max_chars=4000)
    
    audio_files = []
    for i, chunk in enumerate(chunks):
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=chunk
        )
        filepath = f"chapter_{i:03d}.mp3"
        response.stream_to_file(filepath)
        audio_files.append(filepath)
    
    # Spoj MP3 soubory (ffmpeg)
    merge_audio_files(audio_files, "audiobook_final.mp3")
    return "audiobook_final.mp3"
```

---

## Doporučení pro tým

### Pro rychlé experimenty a produkci audioknih v češtině:
**→ ElevenLabs** (Creator plán, ~$22/měsíc)
- Nejlepší česká výslovnost
- Studio UI pro long-form workflow
- Voice cloning pro konzistentní hlas napříč projekty

### Pro vlastní pipeline bez opakujících se nákladů:
**→ OpenAI TTS API (tts-1-hd)** + Python script pro dělení textu
- $30/1M znaků — 80K slovná kniha (~480K znaků) = **~$14**
- Plně automatizovatelné
- Integruje se snadno s existujícími OpenAI projekty

### Pro lokální / open-source bez API costs (anglicky):
**→ Kokoro TTS** (self-hosted, Apache 2.0)
- Zdarma, instalace přes pip
- Nejlepší open-source kvalita (82M param model)
- Ideální pro prototypy a interní obsah v angličtině

### Pro enterprise česky mluvící projekty:
**→ Microsoft Azure TTS** (cs-CZ neural hlasy)
- SSML pro plnou kontrolu (pauzy, emoce, tempo)
- 500K znaků/měsíc zdarma
- SOC 2 / GDPR compliance

### Konkrétní tip pro Prompt Eng tým:
Postavte si **jednoduchý Python script** nad OpenAI TTS API:
1. Input: `.txt` nebo `.epub` soubor (česky)
2. Automatické dělení na kapitoly/chunks
3. Generování MP3 per kapitola
4. Merge přes ffmpeg
5. Output: hotová audiokniha

Cena za 300-stránkovou knihu: **~$10–20** (tts-1-hd). Pokud chcete lepší český hlas → swap za ElevenLabs API. Celý pipeline lze provozovat lokálně a verzovat v Githubu.

---

## Konsenzus vs Kontroverze

**✅ Konsenzus (všechny zdroje shodné):**
- ElevenLabs = nejlepší kvalita AI hlasu 2025/2026
- AI audioknihy jsou teď technicky i komerčně realizovatelné
- Čeština je "second-tier" jazyk (podporována, ale méně hlasů než angličtina)
- Long-form workflow vyžaduje dělení textu a post-processing

**⚠️ Kontroverze:**
- **SaaS vs API**: Narratemi tvrdí, že je nejlepší pro audioknihy — ale ElevenLabs komunita má lepší ekosystém
- **AI vs. lidský narrátor**: Pro dramatickou fikci stále preferovaný člověk (AI je "příliš hladké")
- **Audible/ACX přijetí**: Audible (Amazon) je v roce 2026 stále rezervovaný ohledně AI-narrated audioknih — policy se vyvíjí

---

## Zdroje

1. **ElevenLabs Czech TTS** — https://elevenlabs.io/text-to-speech/czech
2. **ElevenLabs Audiobook Workflow** — https://blog.humanizeaudio.com/elevenlabs-audiobook-workflow/
3. **Best AI Audiobook Generators 2026** — https://narratemi.com/articles/comparisons/best-ai-audiobook-generators-2025
4. **OpenAI TTS API Pricing** — https://costgoat.com/pricing/openai-tts
5. **ElevenLabs vs Play.ht vs Murf** — https://nextaicompare.com/articles/elevenlabs-vs-playht-vs-murf/
6. **Best TTS Tools for Audiobooks 2025** — https://pdmipublishing.com/best-text-to-speech-tools-for-audiobook-creation-2025-edition/
7. **Google Cloud Gemini-TTS** — https://docs.cloud.google.com/text-to-speech/docs/gemini-tts
8. **Kokoro TTS Guide** — https://codybontecou.com/writing/kokoro-tts-open-source-text-to-speech-guide
9. **Kokoro TTS Audiobook Kaggle Notebook** — https://www.kaggle.com/code/kisarak/kokoro-tts-audiobook-git
10. **ElevenLabs Language Support 2026** — https://deepgram.com/learn/elevenlabs-languages-vs-accents-support
11. **Best TTS APIs 2026** — https://www.speechmatics.com/company/articles-and-news/best-tts-apis-in-2025-top-12-text-to-speech-apis
12. **ElevenLabs vs OpenAI TTS** — https://cartesia.ai/vs/elevenlabs-vs-openai-tts
13. **OpenAI TTS API Docs** — https://developers.openai.com/api/docs/models/tts-1-hd

---

*Queries použité: "AI text to audiobook 2025 2026", "ElevenLabs audiobook creation long form", "OpenAI TTS API pricing limitations", "Czech text to speech AI audiobook", "Kokoro TTS open source quality", "Murf PlayHT audiobook comparison 2025", "Google Cloud Gemini-TTS audiobook", "Amazon Polly Microsoft Azure TTS audiobook comparison" | Research datum: 23. března 2026*
