# Tele2026 - Somali AI Course Telegram Bot

Mashruucan waa chatbot Telegram ah oo lagu dhisay Python (pyTelegramBotAPI) iyo SQLite (SQLAlchemy) si loo maareeyo macluumaadka koorsooyinka AI iyo Chatbot-yada ee Af-Soomaaliga.

## Sida Loo Isticmaalo

### 1. Diyaarinta Deegaanka (Setup)

1.  **Ku rakib Python:** Hubi in kombuyuutarkaaga uu ku rakiban yahay Python 3.8+.
2.  **Abuur Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Ku rakib Dependencies:**
    ```bash
    pip install pyTelegramBotAPI SQLAlchemy
    ```

### 2. Habaynta Bot-ka (Configuration)

1.  **Hel Token-kaaga:** Ka hel token-kaaga bot-kaaga cusub ee Telegram adigoo la hadlaya **@BotFather**.
2.  **Beddel Token-ka:** Fur faylka `bot.py` oo beddel xariiqda koowaad ee `TOKEN` oo ku beddel token-kaaga dhabta ah:
    ```python
    TOKEN = 'YOUR_BOT_TOKEN' # FADLAN BEDDEL
    ```
3.  **Beddel Links-ka:** Faylka `bot.py` waxaa ku jira links badan oo *placeholder* ah (tusaale: `WHATSAPP_COMMUNITY_LINK`, `REGISTRATION_LINK`). Fadlan beddel links-kan oo ku beddel links-kaaga dhabta ah.

### 3. Ku Dar Casharradaada

Faylka `bot.py` wuxuu ku jiraa qayb la yiraahdo `populate_data()`. Halkan waxaad ku arki doontaa sida loo buuxiyo xogta koorsooyinka iyo casharrada.

*   **Fiiro Gaar Ah:** Waxaan ku xaddidnay fiidyowyada 5MB si loo hubiyo in Telegram uu si fudud u maareeyo. Fiidyowyada ka weyn 5MB, waxaad u baahan tahay inaad ku shubto meel kale (tusaale: YouTube, Vimeo, ama Google Drive) oo aad isticmaasho link-ga fiidyowgaas.

### 4. Ku Orodsiinta Bot-ka (Running the Bot)

1.  **Hubi in Virtual Environment-ka uu shaqaynayo:**
    ```bash
    source venv/bin/activate
    ```
2.  **Ku orodsi bot-ka:**
    ```bash
    python bot.py
    ```

### 5. Ku Shubista GitHub (Push to GitHub)

**Tallaabooyinka ku shubista GitHub:**

1.  **Abuur Repository Cusub:** Tag GitHub oo abuur repository cusub oo magaciisu yahay **Tele2026**.
2.  **Ku dar Faylasha:** Ku dar faylasha mashruucaaga:
    ```bash
    git init
    git add .
    git commit -m "Initial commit: Somali AI Course Telegram Bot"
    git branch -M main
    git remote add origin https://github.com/YOUR_USERNAME/Tele2026.git # FADLAN BEDDEL
    git push -u origin main
    ```

### 6. Ku Orodsiinta Live (Live Deployment Guide)

Si aad bot-kaaga ugu orodsiiso 24/7, waxaad u baahan tahay inaad isticmaasho adeeg *hosting* ah. Waxaan kuu soo jeedinayaa laba doorasho oo caan ah:

#### Doorashada 1: Heroku (Fudud)

1.  **Abuur `Procfile`:** Ku dar fayl cusub oo magaciisu yahay `Procfile` (oo aan lahayn wax *extension* ah) oo ku qor xariiqdan:
    ```
    worker: python bot.py
    ```
2.  **Ku shub Heroku:** Isticmaal Heroku CLI si aad u geyso mashruucaaga.

#### Doorashada 2: Render (Wanaagsan)

1.  **Ku xir GitHub:** Ku xir Render GitHub repository-gaaga.
2.  **Abuur Web Service:** Dooro *Web Service* oo u sheeg inuu isticmaalo amarka: `python bot.py`.

**Talo Muhiim Ah:** Waxaad u baahan tahay inaad isticmaasho **Webhooks** halkii aad ka isticmaali lahayd *Polling* (sida hadda loo sameeyay) marka aad ku orodsiinayso *live* server. Tani waxay u baahan tahay in aad hesho **SSL Certificate** oo aad u sheegto Telegram URL-kaaga.

**Tallaabada Xigta:** Waxaan kuu dhisay code-ka. Hadda waxaan u gudbi doonaa inaan kuu abuuro repository-ga GitHub oo aan ku shubo code-ka.
