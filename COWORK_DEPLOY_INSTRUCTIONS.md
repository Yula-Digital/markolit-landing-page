# הוראות פריסה — דף הנחיתה של מרכולית אל markolitly.co.il
### מסמך הנחיה עצמאי לסוכן Cowork · גרסה 2.0
### (כתוב מתוך הנחה שאין לך שום זיכרון או הקשר קודם — קרא מההתחלה לפי הסדר)

---

## 🚨 חלק 1 · אזהרת ייצור — קרא לפני שאתה נוגע בכלום

יש **שתי מערכות חיות שמשרתות לקוחות אמיתיים ברגע זה.** המשימה שלך היא לבנות מערכת **שלישית, חדשה ומקבילה** — **בלי לגעת בשתי הקיימות.**

| # | המערכת | איפה היא רצה | כתובת חיה | מצב |
|---|---|---|---|---|
| 1 | **דף הנחיתה (הישן)** | **Vercel** | `https://markolitlandingpage.vercel.app` | חי. אסור לגעת. |
| 2 | **שלישוק / מבצעים** | **GitHub Pages** | `https://rordan-ai.github.io` | חי. אסור לגעת. |
| 3 | **דף הנחיתה (החדש)** ← *המשימה שלך* | **Plesk** | `https://markolitly.co.il` | עדיין לא פעיל. זה מה שתקים. |

**העיקרון: "מקביל, לא במקום."** הישן ממשיך לרוץ בדיוק כמו שהוא. הוא יושבת רק בהחלטה אנושית מפורשת בעתיד — **לא על ידך, ולא עכשיו.**

---

## 🔒 חלק 2 · גבולות גישה — מה מותר לך לגעת ומה אסור

אין לך הרשאה לגעת בשום דבר מחוץ למה שמפורט כאן כ"מותר". אם משהו לא מופיע ברשימת ה"מותר" — **הנח שהוא אסור** ועצור לשאול.

### ✅ מותר לך (ורק זה):
- **תיקייה מקומית אחת בלבד:** `C:\markolit_landing_page\` וכל מה שבתוכה. זו תיקיית העבודה היחידה שלך.
- **ריפו GitHub אחד לעבודה מלאה:** `Yula-Digital/markolit-landing-page` — מותר commit ו-push ל-`main`.
- **ריפו שלישוק — לקריאה וגיבוי-לענף בלבד:** `rordan-ai/rordan-ai.github.io` (יושב בתת-התיקייה `C:\markolit_landing_page\SHLISHUK\`). מותר רק push ל-**ענף גיבוי**, ראה חלק 13. **לעולם לא ל-`main`.**
- **שרת Plesk אחד:** הדומיין `markolitly.co.il`, תיקיית `httpdocs/` בלבד.

### ❌ אסור לך בתכלית האיסור:
- ❌ **כל תיקייה מקומית אחרת** מחוץ ל-`C:\markolit_landing_page\` — כולל תיקיית הבית של המשתמש, פרויקטים אחרים, או כל נתיב אחר בדיסק. אל תקרא, אל תכתוב, אל תריץ שם כלום.
- ❌ **תיקיות "פרויקטים אחרים" שכבר חסומות ב-gitignore כאן:** `SHLISHUK/` (פרט לגיבוי-לענף), `skilles/`, `main_landing_page/`.
- ❌ **כל ריפו Git אחר** מלבד שני אלה שלמעלה. אל תעשה clone, push, או שינוי לשום ריפו אחר.
- ❌ **פרויקט ה-Vercel** `markolit_landing_page` (team `rordan-ais-projects`) — אל תפרוס, אל תחבר מחדש Git, אל תיגע בהגדרות. וגם לא בשום פרויקט Vercel אחר באותו חשבון.
- ❌ **DNS** של כל דומיין שהוא.
- ❌ **ה-short-links** (`l5k.me/avn6C`, `lp6.me/w0plE`) — אל תשנה עד שהיעד החדש אומת.

> אם משימה כלשהי נראית כאילו היא דורשת לחרוג מהגבולות האלה — **עצור ושאל את המשתמש.** אל תניח הרשאה.

---

## 📖 חלק 3 · מילון מונחים (כדי שלא תצטרך לנחש)

- **דף הנחיתה** — אתר **סטטי**: קובץ `index.html` יחיד + תמונות. אין קוד שרת, אין build. מה שיש בתיקייה = מה שעולה לאוויר.
- **שלישוק / מבצעים** — אפליקציה **נפרדת** (React/Vite + Supabase) שמציגה מבצעים שבועיים. דורשת `build`. ריפו נפרד. **לא** חלק מדף הנחיתה.
- **Plesk** — לוח ניהול אחסון (של חברת אינטרוויז'ן). שם מתארח `markolitly.co.il`. הקבצים של האתר יושבים בתיקייה בשם `httpdocs`.
- **FTP / FTPS** — פרוטוקול להעלאת קבצים לשרת. FTPS = הגרסה המוצפנת. כך ה-workflow מעלה קבצים ל-Plesk.
- **GitHub Actions / workflow** — אוטומציה שרצה ב-GitHub. אצלנו: בכל push ל-`main`, היא מעלה את `production_deploy/` ל-Plesk אוטומטית.
- **Secret** — ערך מוצפן ששמור ב-GitHub (כמו סיסמת FTP), שה-workflow קורא בזמן ריצה. לא נשמר בקוד.
- **short-link** — קישור מקוצר (`l5k.me/...`) שמפנה ליעד. ניתן לשנות את היעד בלי לשנות את הקישור עצמו — לכן כתובות שפורסמו ללקוחות לא נשברות.

---

## 🧭 חלק 4 · נקודת התחלה — ודא איפה אתה (הרץ את זה ראשון)

לפני כל פעולה, ודא שאתה במקום הנכון. הרץ את הפקודות הבאות ובדוק שהפלט תואם:

```bash
# 1. אתה צריך להיות בתיקייה הזו:
cd /c/markolit_landing_page && pwd
#   צפוי: /c/markolit_landing_page

# 2. ה-remote של ריפו דף הנחיתה חייב להיות Yula-Digital:
git remote -v
#   צפוי: origin  https://github.com/Yula-Digital/markolit-landing-page.git

# 3. ודא שהקבצים שכבר הוכנו קיימים:
ls production_deploy/index.html production_deploy/.htaccess .github/workflows/deploy-plesk.yml
#   צפוי: שלושת הקבצים קיימים (בלי שגיאה)
```

אם משהו מהשלושה לא תואם — **עצור ושאל את המשתמש.** אל תמשיך.

---

## ✅ חלק 5 · מה כבר בוצע (אתה לא מתחיל מאפס)

עבודת ההכנה כבר נעשתה ונדחפה ל-GitHub. **אינך צריך לחזור על זה:**

1. **תיקיית `production_deploy/`** — דף הנחיתה המוכן לייצור (index.html + assets + .htaccess) — נוצרה ונדחפה.
2. **`.github/workflows/deploy-plesk.yml`** — ה-workflow לפריסה אוטומטית — נוצר ונדחף.
3. **גיבוי התחלתי** — כל הריפו של דף הנחיתה נדחף ל-`main` (commit `0da64c7` ואילך).
4. **גיבוי שלישוק** — ה-WIP של שלישוק גובה לענף `backup/pre-domain-move-2026-06-10` (לא ל-main, כדי לא לפרוס בטעות).

**מה שנשאר לך לעשות** (החלק האנושי + ההפעלה): חלק 6 והלאה.

---

## 🎯 חלק 6 · המטרה שלך, בשורה אחת

לגרום לכך ש-`https://markolitly.co.il` יציג את דף הנחיתה של מרכולית, באמצעות הפעלת ה-workflow שכבר מוכן — **ולאמת שזה עובד.**

הזרימה: `push ל-main` → GitHub Actions מתעורר → מעלה את `production_deploy/` ב-FTPS ל-Plesk → הדף עולה על `markolitly.co.il`.

---

## 📋 חלק 7 · רשימת משימות מלאה (בצע לפי הסדר)

### שלב א — הקמת הפריסה
- [ ] **M1.** בקש מהמשתמש את פרטי ה-FTP של Plesk (host, שם משתמש, סיסמה) — חלק 8.
- [ ] **M2.** הגדר 3 Secrets בריפו `Yula-Digital/markolit-landing-page`: `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD` — חלק 9.
- [ ] **M3.** הפעל את ה-workflow (`workflow_dispatch` בטאב Actions). הקוד כבר ב-main — אין צורך ב-commit — חלק 10.
- [ ] **M4.** ודא שה-workflow הסתיים בירוק. נכשל על "אימות Secrets"? → חזור ל-M2.

### שלב ב — אימות (חובה, אל תדלג)
- [ ] **M5.** פתח `https://markolitly.co.il` — הדף מופיע, התמונות נטענות, HTTPS נכפה — חלק 11.
- [ ] **M6.** תמונות שבורות? תקן את `server-dir` ב-`deploy-plesk.yml` — חלק 11.
- [ ] **M7.** ודא ש"שלישוק במרכולית" / "מועדון" פותחים את ה-short-links כרגיל.

### שלב ג — תקופת מעבר (מקביל לישן)
- [ ] **M8.** השאר את Vercel ושלישוק חיים — אל תיגע בהם (חלק 1 + 2).
- [ ] **M9.** נדרש redirect מדומיין ישן? הפעל את התבנית בסוף `production_deploy/.htaccess` (302) — חלק 12.
- [ ] **M10.** עדכן את ה-short-links ליעד החדש — **רק אחרי** שהחדש אומת.
- [ ] **M11.** תזכורת: ב-Plesk אין פקיעת redirect אוטומטית. בתאריך היעד הסר ידנית — חלק 12.

### שלב ד — עתידי (לא דחוף, רק בהחלטה מפורשת)
- [ ] **M12.** איחוד שלישוק תחת `markolitly.co.il/shlishuk` — חלק 14.

### גבולות גזרה (תקף לאורך כל המשימה)
- [ ] **G1.** ❌ אל תיגע בפרויקט Vercel (חלק 1).
- [ ] **G2.** ❌ אל תדחוף לשום מקום מלבד שני הריפו המורשים (חלק 2).
- [ ] **G3.** ❌ אל תדחוף שינויי שלישוק ל-`main` — רק לענף גיבוי (חלק 13).
- [ ] **G4.** ❌ אל תיגע ב-DNS.
- [ ] **G5.** ❌ אל תמחק קבצים ב-`httpdocs/` לפני שראית מה קיים שם.
- [ ] **G6.** ❌ אל תוסיף `dangerous-clean-slate` ל-workflow.
- [ ] **G7.** ❌ אל תצא מהתיקייה `C:\markolit_landing_page\` לשום פעולה מקומית.

---

## 📁 חלק 8 · בקשת פרטי FTP מהמשתמש (משימה M1)

אתה לא יכול להשיג את אלה לבד — בקש מהמשתמש. נסח לו כך:

> כדי לחבר את הפריסה האוטומטית ל-Plesk, אני צריך שלושה פרטים. הוצא אותם מהפאנל:
> פאנל Plesk → **Websites & Domains** → `markolitly.co.il` → **FTP Access**
> (אפשר ליצור חשבון FTP חדש או להשתמש בקיים). רשום לי:
> 1. **FTP host** — לרוב `markolitly.co.il` או `ftp.markolitly.co.il` או כתובת IP של השרת.
> 2. **שם משתמש FTP**.
> 3. **סיסמת FTP**.

---

## 🔑 חלק 9 · הגדרת ה-Secrets ב-GitHub (משימה M2)

הזן את שלושת הפרטים מחלק 8 כ-Secrets בריפו `Yula-Digital/markolit-landing-page`.

**דרך א — דרך הממשק (הנחה את המשתמש):**
> `github.com/Yula-Digital/markolit-landing-page` → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**. צור שלושה:

| שם ה-Secret (בדיוק כך) | הערך |
|---|---|
| `FTP_SERVER`   | ה-FTP host |
| `FTP_USERNAME` | שם המשתמש |
| `FTP_PASSWORD` | הסיסמה |

**דרך ב — דרך `gh` CLI (אם יש לך גישה והרשאה):**
```bash
gh secret set FTP_SERVER   --repo Yula-Digital/markolit-landing-page --body "<host>"
gh secret set FTP_USERNAME --repo Yula-Digital/markolit-landing-page --body "<user>"
gh secret set FTP_PASSWORD --repo Yula-Digital/markolit-landing-page --body "<pass>"
```

> אזהרת אבטחה: אל תכתוב את הסיסמה לתוך שום קובץ בריפו, ל-`.htaccess`, או ל-workflow. רק כ-Secret.

---

## ▶️ חלק 10 · הפעלת הפריסה הראשונה (משימה M3)

הקוד כבר ב-`main` — **אל תעשה commit ראשוני.** רק הפעל:

1. ודא שה-Secrets מחלק 9 מוגדרים (בלעדיהם ה-workflow ייכשל בכוונה עם הודעה ברורה).
2. הפעל ידנית: `github.com/Yula-Digital/markolit-landing-page` → טאב **Actions** → בחר **"Deploy landing page to Plesk (markolitly.co.il)"** → כפתור **Run workflow** → ענף `main` → **Run**.
   לחלופין דרך CLI: `gh workflow run "deploy-plesk.yml" --repo Yula-Digital/markolit-landing-page`
3. עקוב אחרי הריצה: טאב **Actions** (או `gh run watch --repo Yula-Digital/markolit-landing-page`).
4. נכשל על "אימות Secrets"? → ה-Secrets לא הוגדרו נכון. חזור לחלק 9.

---

## 🔍 חלק 11 · אימות הצלחה (משימות M5–M7 · חובה)

סמן כל שורה רק אחרי שראית אותה בעיניים:

- [ ] ה-workflow ב-Actions הסתיים ב-✅ ירוק.
- [ ] `https://markolitly.co.il` נטען ומציג את דף מרכולית (רקע קרם, לוגו ירוק, כותרת "מרכולית - חוויית כפרית").
- [ ] כל התמונות נטענות (הירו, רצועת האייקונים, כרטיסי מבצעים/טריים/דרושים) — אין "תמונה שבורה".
- [ ] גלישה ל-`http://markolitly.co.il` קופצת אוטומטית ל-`https://`.
- [ ] לחיצה על "שלישוק במרכולית" / "הצטרפות למועדון" פותחת את ה-short-links כרגיל.

**אם התמונות שבורות (הדף עולה אך בלי תמונות) — כמעט תמיד יעד ה-FTP שגוי:**
ב-`.github/workflows/deploy-plesk.yml`, שדה `server-dir`:
- ברירת מחדל במסמך: `./httpdocs/`.
- אם חשבון ה-FTP שלך כבר "נוחת" ישירות בתוך `httpdocs` → שנה ל-`./`.
- כדי לדעת בוודאות: פתח **File Manager** ב-Plesk וראה לאן הקבצים הגיעו בפועל. תקן את `server-dir` בהתאם, עשה commit + push, וה-workflow ירוץ שוב.

---

## 🔁 חלק 12 · תקופת מעבר ודומיין כפול (משימות M8–M11)

המטרה: הדף החדש עולה **בלי לשבור** שום כתובת קיימת. שלוש שכבות הגנה:

1. **Vercel נשאר חי** — דף הנחיתה הישן ממשיך לעבוד ב-`markolitlandingpage.vercel.app`. אל תכבה אותו (M8).
2. **short-links** — ממשיכים להצביע לאן שהצביעו. כשתרצה, תפנה אותם לדומיין החדש (M10) — **רק אחרי** אימות.
3. **Redirect ברמת שרת** (אופציונלי, M9) — בתחתית `production_deploy/.htaccess` יש תבנית מוערת. כדי להפעיל: הסר את ההערה, החלף `OLD-DOMAIN` בדומיין הישן, והוא יפנה 302 לחדש.

> ⚠️ **אין ב-Plesk/Apache פקיעת redirect אוטומטית בתאריך.** אם הפעלת redirect זמני — בתאריך היעד תצטרך להסיר ידנית את שורות ה-RewriteRule מ-`.htaccess`. שווה לבקש מהמשתמש לתזמן תזכורת (M11).

---

## 💾 חלק 13 · גיבוי שלישוק / מבצעים (ריפו נפרד — נוהל זהירות)

שלישוק הוא **ריפו Git נפרד לחלוטין**, שיושב בתת-התיקייה `C:\markolit_landing_page\SHLISHUK\`.

| פרט | ערך |
|---|---|
| מיקום מקומי | `C:\markolit_landing_page\SHLISHUK\` |
| Remote | `github.com/rordan-ai/rordan-ai.github.io` |
| ענף ייצור | `main` — **push אליו פורס את שלישוק חי ללקוחות!** |
| טכנולוגיה | React/Vite + Supabase |

**✅ כבר בוצע:** ה-WIP גובה לענף `backup/pre-domain-move-2026-06-10` (commit `7971682`). main לא נגעו בו.

**נוהל גיבוי עתידי (תמיד לענף, לעולם לא ל-main):**
```bash
cd /c/markolit_landing_page/SHLISHUK
git checkout -b backup/<תאריך>
git add -A -- . ':!setup/backups'        # אל תכלול גיבויי DB כבדים (~22MB)
git commit -m "Backup shlishuk WIP <תאריך>"
git push -u origin backup/<תאריך>
# החזרת עץ העבודה למצב המקורי (main + WIP לא-מקומיט):
git checkout main
git checkout backup/<תאריך> -- .
git reset -q HEAD .
```

> **למה לא ל-main?** push ל-`main` של `rordan-ai.github.io` מפעיל את ה-workflow `pages-public.yml` ופורס את שלישוק חי. ענף גיבוי שומר הכל ברימוט **בלי** לפרוס.

---

## 🔮 חלק 14 · עתידי — איחוד שלישוק תחת markolitly.co.il (משימה M12)

**לא דחוף.** שלישוק עובד בייצור על GitHub Pages, וה-short-link `l5k.me/avn6C` מפנה אליו (302 → `rordan-ai.github.io/SHLISHUK/`). בצע רק כשמחליטים במפורש לאחד הכל תחת דומיין אחד.

שלישוק הוא אפליקציית Vite — **חייב build** (בניגוד לדף הנחיתה הסטטי). הצעדים:

1. **נתיב יעד מומלץ:** תת-תיקייה `markolitly.co.il/shlishuk/`.
2. **תקן `base` ב-Vite:** ב-`SHLISHUK/vite.config.ts` שנה `base: '/'` ל-`base: '/shlishuk/'`. ⚠️ זה ישבור את פריסת GitHub Pages הנוכחית — לכן עבוד על ענף נפרד, או נהל לפי משתנה סביבה.
3. **בנה:** `cd /c/markolit_landing_page/SHLISHUK && npm ci && npm run build` → נוצר `SHLISHUK/dist/`. דרושים `VITE_SUPABASE_URL` ו-`VITE_SUPABASE_ANON_KEY` בסביבה.
4. **SPA fallback:** הוסף `.htaccess` בתוך `httpdocs/shlishuk/`:
   ```apache
   RewriteEngine On
   RewriteBase /shlishuk/
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteCond %{REQUEST_FILENAME} !-d
   RewriteRule . /shlishuk/index.html [L]
   ```
5. **פרוס:** העלה את תוכן `SHLISHUK/dist/` אל `httpdocs/shlishuk/` (אפשר workflow FTP נפרד: `local-dir: ./SHLISHUK/dist/`, `server-dir: ./httpdocs/shlishuk/`, אחרי שלב build).
6. **הפנה short-link:** עדכן `l5k.me/avn6C` → `https://markolitly.co.il/shlishuk/`.
7. **Supabase:** ודא שהדומיין החדש מורשה (Auth → URL Configuration / CORS).

> ⚠️ עד שהכל אומת — **אל תכבה** את פריסת GitHub Pages של שלישוק. היא הייצור הנוכחי.

---

## 📎 נספח A — תוכן `.github/workflows/deploy-plesk.yml`
*(הקובץ כבר קיים בריפו. השתמש בזה רק אם הוא חסר — אחרת דלג.)*

```yaml
name: Deploy landing page to Plesk (markolitly.co.il)

on:
  push:
    branches: [main]
    paths:
      - 'production_deploy/**'
      - '.github/workflows/deploy-plesk.yml'
  workflow_dispatch:

concurrency:
  group: deploy-plesk
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: אימות שה-Secrets הנדרשים מוגדרים
        run: |
          if [ -z "${{ secrets.FTP_SERVER }}" ];   then echo "::error::הגדר FTP_SERVER";   exit 1; fi
          if [ -z "${{ secrets.FTP_USERNAME }}" ]; then echo "::error::הגדר FTP_USERNAME"; exit 1; fi
          if [ -z "${{ secrets.FTP_PASSWORD }}" ]; then echo "::error::הגדר FTP_PASSWORD"; exit 1; fi

      - name: פריסה אוטומטית ב-FTPS אל Plesk
        uses: SamKirkland/FTP-Deploy-Action@v4.3.5
        with:
          server: ${{ secrets.FTP_SERVER }}
          username: ${{ secrets.FTP_USERNAME }}
          password: ${{ secrets.FTP_PASSWORD }}
          protocol: ftps
          port: 21
          local-dir: ./production_deploy/
          server-dir: ./httpdocs/
```

## 📎 נספח B — מבנה התיקיות שנפרסת
```
C:\markolit_landing_page\
├── .github\workflows\deploy-plesk.yml   ← ה-workflow (כבר קיים)
├── production_deploy\                    ← ★ רק זה נפרס ל-httpdocs/ ★
│   ├── index.html
│   ├── .htaccess                         ← HTTPS + caching (כבר קיים)
│   └── assets\
│       ├── markolit-composed.png
│       ├── markolit-icones-strip.svg
│       ├── main-photo-transparent.png
│       ├── hero-title-transparent.png
│       └── images\ (trans_logo_marcolit, countryside_transparent,
│                    countryside_clean, weekly_sale2, employee,
│                    fresh_final, join_club_combined, join_the_club)
├── SHLISHUK\                             ← ריפו נפרד (חלק 13) — לא נפרס לכאן
└── COWORK_DEPLOY_INSTRUCTIONS.md         ← המסמך הזה
```

---

## ✔️ בדיקה עצמית של המסמך
- ✅ מניח אפס זיכרון: פותח באזהרה, גבולות גישה, מילון, ואימות סביבה לפני כל פעולה.
- ✅ כל פקודה ניתנת להעתקה; כל יעד מצוין במלואו (ריפו, נתיב, שם Secret).
- ✅ מפריד בין מה שכבר בוצע (חלק 5) למה שנשאר (חלק 7+).
- ✅ מפריד בין פעולות הסוכן לפעולות שדורשות אדם (FTP, Secrets).
- ✅ גבולות גישה קונקרטיים — מותר/אסור מקומי, ריפו, Vercel, DNS.
- ✅ אימות חובה + טיפול בכשל הנפוץ (תמונות שבורות).

**תלות אנושית יחידה:** פרטי FTP + הגדרת Secrets (חלקים 8–9). כל השאר אוטומטי.
