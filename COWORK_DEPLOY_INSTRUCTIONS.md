# הוראות פריסה אוטומטית — דף הנחיתה של מרכולית אל markolitly.co.il
### מסמך הנחיה לסוכן Cowork · גרסה 1.2

---

## 🚨🚨 אזהרה כללית — קרא לפני כל פעולה 🚨🚨

**הייצור הקיים חי ומשרת לקוחות עכשיו. אסור לגעת בו בשום אופן.**

אנחנו בונים **מערכת מקבילה חדשה** על `markolitly.co.il` (Plesk) — **בלי לגעת בישן.** הישן ממשיך לרוץ כרגיל עד שתינתן החלטה מפורשת אחרת.

**שתי מערכות ייצור קיימות שאסור לגעת בהן:**

| מערכת | מיקום ייצור | כתובת חיה | סטטוס |
|---|---|---|---|
| **דף הנחיתה (ישן)** | **Vercel** (פרויקט `markolit_landing_page`, team `rordan-ais-projects`) | `markolitlandingpage.vercel.app` | חי, קפוא על commit `8972468` |
| **שלישוק / מבצעים** | **GitHub Pages** (`rordan-ai/rordan-ai.github.io`) | `rordan-ai.github.io` ‏(short-link `l5k.me/avn6C` → `/SHLISHUK/`) | חי |

**אסור בתכלית האיסור:**
- ❌ **אל תפעיל deploy ב-Vercel**, אל תחבר מחדש את אינטגרציית ה-Git שלו, אל תשנה הגדרות/דומיינים/משתני סביבה בפרויקט Vercel. שהוא יישאר קפוא בדיוק כפי שהוא.
- ❌ **אל תדחוף שום דבר ל-`main` של `rordan-ai.github.io`** — זה מפרס שלישוק חי ללקוחות. גיבוי/עבודה תמיד ל-branch נפרד (סעיף 9).
- ❌ **אל תיגע ב-DNS** של אף דומיין קיים.
- ❌ **אל תשנה את ה-short-links** (`l5k.me/avn6C`, `lp6.me/w0plE`) עד שהיעד החדש אומת ועובד.
- ❌ אל תמחק/תכבה שום פריסה ישנה — גם לא "כדי לנקות".

**כל העבודה שלך מתרחשת אך ורק בערוץ החדש:** ריפו `Yula-Digital/markolit-landing-page` → GitHub Actions → FTPS → Plesk (`markolitly.co.il`). הערוץ הזה **מנותק** מה-Vercel הישן (לכן push לא נוגע בו) — וזה רצוי.

> עקרון מנחה: **"מקביל, לא במקום."** מוסיפים מערכת חדשה לצד הישנה. הישן מושבת רק בהחלטה אנושית מפורשת, ורק אחרי שהחדש אומת מקצה לקצה.

---

## ✅ סטטוס ביצוע (עודכן 2026-06-10)

**גיבוי התחלתי בוצע — הכל שמור ברימוט:**
- **ריפו דף הנחיתה** — commit `0da64c7` נדחף ל-`main` (כולל `production_deploy/`, ה-workflow, ה-.htaccess, המסמך הזה וכל ה-assets). ⚠️ הריפו **עבר** ל-`Yula-Digital/markolit-landing-page` (ה-remote עודכן בהתאם).
- **ריפו שלישוק/מבצעים** (`rordan-ai/rordan-ai.github.io`) — ה-WIP גובה ל-branch‏ `backup/pre-domain-move-2026-06-10` (commit `7971682`). **main לא נגעו בו** כדי לא להפעיל deploy חי ב-GitHub Pages. גיבויי ה-DB המקומיים (`setup/backups/`, ~22MB) נשארו מקומיים בכוונה.

**מה שעדיין פתוח (ראה רשימת המשימות בסעיף 0.1):** פרטי FTP, הגדרת Secrets, הרצת הפריסה הראשונה ואימות — אלה המשימות שלך.

---

## 0. קונטקסט — קרא קודם

אתה עומד להפעיל **פריסה אוטומטית** של דף הנחיתה של "מרכולית" אל הדומיין `markolitly.co.il`.

**מה זה הפרויקט:**
- ריפו GitHub: `Yula-Digital/markolit-landing-page` (לשעבר `rordan-ai/markolit-landing-page` — עבר מיקום).
- **דף הנחיתה** הוא אתר **סטטי** — קובץ `index.html` יחיד + תמונות. אין build, אין Node, אין framework. מה שיש בתיקייה זה מה שעולה לשרת.
- הקבצים המוכנים לייצור נמצאים בתיקייה **`production_deploy/`** (index.html + assets + .htaccess). **רק התיקייה הזו נפרסת.**

**איפה הכל יושב כרגע (אל תיגע בזה):**
| רכיב | מיקום נוכחי | האם נוגעים? |
|---|---|---|
| דף הנחיתה | Vercel | משאירים חי כ-fallback |
| שלישוק / מבצעים | GitHub Pages (`rordan-ai.github.io`) — פרויקט React נפרד | **לא נוגעים בכלל** |
| היעד החדש | `markolitly.co.il` על **Plesk / אינטרוויז'ן** (פאנל בפורט 8443) | זה היעד שלנו |

**עובדות חשובות:**
- הדומיין `markolitly.co.il` **כבר** מצביע על אינטרוויז'ן (המייל `tova@markolitly.co.il` פעיל) — **אסור לגעת ב-DNS**.
- שלישוק נפרד לחלוטין — העברת דף הנחיתה לא שוברת אותו.
- הקישורים בדף לשלישוק/מועדון הם short-links (`l5k.me/avn6C`, `lp6.me/w0plE`) — ניתנים להפניה מחדש, לא נשברים.

**שיטת הפריסה שנבחרה:** GitHub Actions → **FTPS** אל Plesk. כל push ל-`main` שנוגע ב-`production_deploy/` מסנכרן אוטומטית לשרת. הקבצים הדרושים כבר קיימים בריפו (ראה סעיף 2).

**מטרת המשימה:** להפעיל את הצינור הזה מקצה לקצה ולאמת שהדף עולה תקין על `https://markolitly.co.il`.

---

## 0.1 ★ רשימת משימות מרוכזת לסוכן Cowork ★
*(כל ההסתייגויות וההערות הפכו כאן למשימות מפורשות. בצע לפי הסדר. כל פרט מורחב בסעיפים שבהמשך.)*

### א. הקמת הפריסה של דף הנחיתה
- [ ] **M1.** השג מהמשתמש את פרטי ה-FTP מ-Plesk (host, user, password) — סעיף 3.
- [ ] **M2.** הגדר 3 Secrets בריפו **`Yula-Digital/markolit-landing-page`** (לא rordan-ai!): `FTP_SERVER`, `FTP_USERNAME`, `FTP_PASSWORD` — סעיף 4.
- [ ] **M3.** הפעל את ה-workflow (`workflow_dispatch` בטאב Actions, או push קטן). הקוד כבר ב-main — אין צורך ב-commit ראשוני.
- [ ] **M4.** ודא שה-workflow הסתיים בירוק. אם נכשל על "אימות Secrets" → חזור ל-M2.

### ב. אימות (חובה — אל תסמן "בוצע" בלי זה)
- [ ] **M5.** טען `https://markolitly.co.il` — דף הנחיתה מופיע, התמונות נטענות, HTTPS נכפה. צ'קליסט מלא בסעיף 6.
- [ ] **M6.** אם תמונות שבורות → תקן את `server-dir` ב-`deploy-plesk.yml` (`./httpdocs/` ↔ `./`) לפי מה שראית ב-File Manager — סעיף 6.
- [ ] **M7.** ודא ש-"שלישוק במרכולית" / "מועדון" פותחים את ה-short-links כרגיל.

### ג. תקופת מעבר / דומיין כפול
- [ ] **M8.** השאר את ה-deploy ב-**Vercel חי** עד אימות מלא של הדף החדש (אל תכבה).
- [ ] **M9.** אם נדרש redirect מהדומיין הישן — הפעל את התבנית המוערת בסוף `production_deploy/.htaccess` (החלף `OLD-DOMAIN`, 302).
- [ ] **M10.** עדכן את ה-short-links (`l5k.me/avn6C`, `lp6.me/w0plE`) ליעד הסופי בעת הצורך.
- [ ] **M11.** **תזכורת ידנית:** ב-Plesk/Apache אין פקיעת redirect אוטומטית — בתאריך היעד הסר ידנית את שורות ה-RewriteRule מ-`.htaccess` (או הסר את הדומיין הישן). תזמן תזכורת.
- [ ] **M12.** רק אחרי שהכל אומת — כבה/הסר את ה-deploy הישן ב-Vercel.
- [ ] **M13.** ⚠️ **Vercel מנותק מה-Git החדש:** הריפו עבר ל-`Yula-Digital` אך אינטגרציית ה-Git של Vercel עדיין קשורה ל-`rordan-ai`, כך ש-push חדש **לא** מעדכן את Vercel (הייצור קפוא על commit `8972468` — וזה תקין לתקופת המעבר). אם בעתיד תרצה לעדכן את גרסת ה-Vercel — חבר מחדש את הפרויקט `markolit_landing_page` לריפו `Yula-Digital/markolit-landing-page` ב-Vercel → Settings → Git. (בדרך כלל לא נדרש — היעד הוא markolitly.co.il.)

### ה. עתידי — איחוד שלישוק לאותו דומיין
- [ ] **M14.** העברת שלישוק/מבצעים גם הם אל `markolitly.co.il` (למשל `markolitly.co.il/shlishuk`) — ראה סעיף 10 לפרטים מלאים. כרגע שלישוק חי על GitHub Pages וה-short-link `l5k.me/avn6C` מפנה אליו (302 → `rordan-ai.github.io/SHLISHUK/`).

### ד. גבולות גזרה (אסור!)
- [ ] **G1.** ❌ אל תיגע בתיקיית `SHLISHUK/` ובפריסת GitHub Pages שלה. גיבוי שלה = סעיף 9 בלבד.
- [ ] **G2.** ❌ אל תשנה רשומות DNS.
- [ ] **G3.** ❌ אל תמחק קבצים ב-`httpdocs/` לפני שראית מה קיים שם.
- [ ] **G4.** ❌ אל תוסיף `dangerous-clean-slate` ל-workflow בריצה הראשונה.
- [ ] **G5.** ❌ אל תדחוף שינויי שלישוק ל-`main` של `rordan-ai.github.io` — זה מפעיל deploy חי. גיבוי תמיד ל-branch (סעיף 9).
- [ ] **G6.** ❌ אל תיגע בפרויקט ה-Vercel `markolit_landing_page` — לא deploy, לא חיבור Git מחדש, לא הגדרות. הוא ייצור חי וקפוא. בונים מקביל, לא במקום. (ראה האזהרה הכללית בראש המסמך.)

---

## 1. מבנה התיקיות (כך זה אמור להיראות)

```
markolit-landing-page/                ← שורש הריפו
├── .github/
│   └── workflows/
│       └── deploy-plesk.yml          ← workflow הפריסה (כבר קיים)
├── production_deploy/                ← ★ התיקייה היחידה שנפרסת ★
│   ├── index.html
│   ├── .htaccess                     ← HTTPS + caching (כבר קיים)
│   └── assets/
│       ├── markolit-composed.png
│       ├── markolit-icones-strip.svg
│       ├── main-photo-transparent.png
│       ├── hero-title-transparent.png
│       └── images/
│           ├── trans_logo_marcolit.png
│           ├── countryside_transparent.png
│           ├── countryside_clean.png
│           ├── weekly_sale2.png
│           ├── employee.png
│           ├── fresh_final.png
│           ├── join_club_combined.svg
│           └── join_the_club.png
└── COWORK_DEPLOY_INSTRUCTIONS.md     ← המסמך הזה
```

על השרת (Plesk) היעד הוא: `httpdocs/` — לשם מסונכרן **תוכן** `production_deploy/`.

---

## 2. קבצים שכבר הוכנו עבורך (אמת שהם קיימים)

שני קבצים כבר נוצרו בריפו — **אמת שהם שם, אל תיצור מחדש**:
1. `.github/workflows/deploy-plesk.yml` — workflow הפריסה.
2. `production_deploy/.htaccess` — כפיית HTTPS + caching + תבנית redirect לדומיין כפול.

אם אחד מהם חסר — צור אותו מהתוכן שבסוף המסמך (נספח A / נספח B).

---

## 3. מה שהמשתמש האנושי חייב לספק (אינך יכול להשיג זאת בעצמך)

פרטי ה-FTP מתוך פאנל Plesk. בקש מהמשתמש להוציא אותם כך:

> בפאנל Plesk → **Websites & Domains** → `markolitly.co.il` → **FTP Access** →
> או ליצור חשבון FTP חדש, או להשתמש בקיים. רשום:
> - **FTP host** (לרוב `markolitly.co.il` או `ftp.markolitly.co.il` או IP של השרת)
> - **שם משתמש FTP**
> - **סיסמת FTP**

---

## 4. הגדרת Secrets ב-GitHub (פעולה של המשתמש, אתה מנחה)

ב-`github.com/Yula-Digital/markolit-landing-page` → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**. הוסף שלושה:

| שם ה-Secret | ערך |
|---|---|
| `FTP_SERVER`   | ה-FTP host מסעיף 3 |
| `FTP_USERNAME` | שם המשתמש |
| `FTP_PASSWORD` | הסיסמה |

> ⚠️ אם הסוכן יכול לגשת ל-GitHub עם `gh` CLI ובהרשאה מתאימה, אפשר להגדיר כך:
> ```
> gh secret set FTP_SERVER   --repo Yula-Digital/markolit-landing-page --body "<host>"
> gh secret set FTP_USERNAME --repo Yula-Digital/markolit-landing-page --body "<user>"
> gh secret set FTP_PASSWORD --repo Yula-Digital/markolit-landing-page --body "<pass>"
> ```
> אחרת — הנחה את המשתמש לעשות זאת ידנית דרך ה-UI.

---

## 5. הפעלה ראשונה — צעד אחר צעד

> ✅ **כבר בוצע:** הקבצים (`production_deploy/`, ה-workflow, ה-.htaccess, המסמך) כבר עברו commit ו-push ל-`main` (commit `0da64c7`). **אינך צריך לעשות commit ראשוני.** לכן:

1. הגדר את ה-Secrets (סעיף 4) — בלעדיהם ה-workflow ייכשל בכוונה עם הודעה ברורה.
2. הפעל את ה-workflow: טאב **Actions** → "Deploy landing page to Plesk" → **Run workflow** (`workflow_dispatch`). לחלופין כל push קטן ל-`main` שנוגע ב-`production_deploy/` יפעיל אותו.
3. עקוב ב-**Actions** (או `gh run watch`). אם נכשל ב"אימות Secrets" — חזור לשלב 1.

---

## 6. אימות הצלחה (חובה — אל תסיים בלי זה)

- [ ] ה-workflow ב-Actions הסתיים ב-✅ ירוק.
- [ ] טען `https://markolitly.co.il` — דף הנחיתה של מרכולית מופיע (רקע קרם, לוגו ירוק, כותרת "מרכולית - חוויית כפרית").
- [ ] התמונות נטענות (הירו, רצועת האייקונים, כרטיסי מבצעים/טריים/דרושים) — אין "תמונה שבורה".
- [ ] הגלישה עברה ל-HTTPS אוטומטית (גם אם הקלדת `http://`).
- [ ] לחיצה על "שלישוק במרכולית" / "מועדון" פותחת את ה-short-links כרגיל.

**אם התמונות לא נטענות** → סביר שיעד ה-FTP שגוי. ב-`deploy-plesk.yml`, שדה `server-dir`:
- ברירת מחדל: `./httpdocs/`.
- אם חשבון ה-FTP כבר "נכנס" ישירות לתוך httpdocs → שנה ל-`./`.
- אמת מול File Manager ב-Plesk היכן נחתו הקבצים בפועל.

---

## 7. דומיין כפול / תקופת מעבר (מה שהמשתמש ביקש)

הדף החדש על `markolitly.co.il` עולה **בלי לגעת** ב-Vercel ובשלישוק — שלוש שכבות הגנה מפני שבירת כתובות:
1. **ה-deploy ב-Vercel נשאר חי** במקביל. שתי הכתובות עובדות. מסירים את הישנה ידנית כשתחליט.
2. **short-links** — מפנים מחדש ליעד החדש בעת הצורך. אפס שבירה.
3. **Redirect ברמת שרת** — תבנית כבר מוכנה ומוערת ב-`production_deploy/.htaccess` (סוף הקובץ): הסר הערה, החלף `OLD-DOMAIN`, והוא יפנה 302 מהישן לחדש.

> אין ב-Plesk/Apache פקיעה אוטומטית של redirect. בתאריך היעד צריך להסיר ידנית את שורות ה-RewriteRule מ-`.htaccess` (או להסיר את הדומיין הישן). שווה לתזמן תזכורת.

---

## 8. גבולות גזרה — מה אסור לעשות

- ❌ אל תיגע בתיקיית `SHLISHUK/` ובפריסת ה-GitHub Pages שלה.
- ❌ אל תשנה רשומות DNS.
- ❌ אל תמחק קבצים קיימים ב-`httpdocs/` לפני שראית מה יש שם (ייתכן אתר/דף קיים).
- ❌ אל תוסיף `dangerous-clean-slate` ל-workflow בריצה הראשונה.
- ❌ אל תכבה את Vercel עד שאומת שהדף החדש תקין במלואו.

---

## 9. גיבוי נפרד לשלישוק / מבצעים (ריפו אחר!)

**חשוב:** שלישוק ("מבצעים") הוא **ריפו git נפרד לחלוטין** מדף הנחיתה — גם אם בעתיד הכל ישב על אותו דומיין. הגיבוי שלו נעשה בנפרד, ולעולם **לא** דרך ריפו דף הנחיתה.

| פרט | ערך |
|---|---|
| מיקום מקומי | `SHLISHUK/` (gitignored בריפו דף הנחיתה) |
| Remote | `github.com/rordan-ai/rordan-ai.github.io` |
| ענף ייצור | `main` — **push אליו מפעיל deploy חי ל-GitHub Pages** |
| טכנולוגיה | React/Vite + Supabase (`npm run build`) |

### ✅ מה כבר בוצע
ה-WIP (שינויים ב-`src/App.tsx`, `src/draftStorage.ts`, `.gitignore`) גובה לענף **`backup/pre-domain-move-2026-06-10`** (commit `7971682`). main לא נגעו בו. גיבויי DB מקומיים (`setup/backups/`, ~22MB) נשארו מקומיים בכוונה (ה-`.gitignore` של שלישוק חוסם את ה-`*-full.json`).

### איך לבצע גיבוי שלישוק בעתיד (נוסחה קבועה — בלי deploy בטעות)
```bash
cd SHLISHUK
# גבה תמיד לענף, לעולם לא ל-main:
git checkout -b backup/<תאריך>
git add -A -- . ':!setup/backups'        # אל תכלול גיבויי DB כבדים
git commit -m "Backup shlishuk WIP <תאריך>"
git push -u origin backup/<תאריך>
# החזר את עץ העבודה למצב המקורי (main + WIP לא-מקומיט):
git checkout main
git checkout backup/<תאריך> -- .          # מחזיר את ה-WIP לעץ העבודה
git reset -q HEAD .                        # משאיר אותו לא-staged כמו שהיה
```

> **למה ענף ולא main?** דחיפה ל-`main` של `rordan-ai.github.io` מפעילה את `pages-public.yml` ופורסת את שלישוק חי ללקוחות. ענף גיבוי שומר הכל ברימוט **בלי** להפעיל deploy.

> **פריסה חיה של שלישוק (כשבאמת רוצים):** רק אז עושים merge/‏push ל-`main`, והבנייה רצה אוטומטית. דורש שה-Secrets `VITE_SUPABASE_URL` / `VITE_SUPABASE_ANON_KEY` מוגדרים בריפו של שלישוק.

---

## 10. עתידי — איחוד שלישוק/מבצעים אל markolitly.co.il (משימה M14)

**מצב נוכחי:** שלישוק חי על GitHub Pages; ה-short-link `l5k.me/avn6C` מפנה (302) אל `rordan-ai.github.io/SHLISHUK/`. **לא דחוף** — עובד בייצור כפי שהוא. בצע רק כשמחליטים לאחד הכל תחת דומיין אחד.

שלישוק הוא אפליקציית **Vite/React + Supabase** — בניגוד לדף הנחיתה הסטטי, **חייב build** לפני העלאה. הצעדים:

1. **החלט על נתיב יעד.** המומלץ: תת-תיקייה `markolitly.co.il/shlishuk/` (פשוט יותר מ-subdomain ב-Plesk).
2. **תקן את ה-base ב-Vite.** בקובץ `SHLISHUK/vite.config.ts` שנה `base: '/'` ל-`base: '/shlishuk/'` (אחרת ה-assets ייטענו מנתיב שגוי). ⚠️ זה ישבור את פריסת ה-GitHub Pages הנוכחית שמשתמשת ב-`base: '/'` — לכן עשה זאת על ענף נפרד, או נהל את ה-base לפי משתנה סביבה.
3. **בנה:** `cd SHLISHUK && npm ci && npm run build` → נוצר `SHLISHUK/dist/`. דרוש `VITE_SUPABASE_URL` ו-`VITE_SUPABASE_ANON_KEY` בסביבה בזמן ה-build.
4. **SPA fallback:** הוסף `.htaccess` בתוך `shlishuk/` ב-Plesk שמפנה כל נתיב לא-קיים ל-`index.html` (כי זו אפליקציית עמוד-יחיד):
   ```apache
   RewriteEngine On
   RewriteBase /shlishuk/
   RewriteCond %{REQUEST_FILENAME} !-f
   RewriteCond %{REQUEST_FILENAME} !-d
   RewriteRule . /shlishuk/index.html [L]
   ```
5. **פרוס:** העלה את תוכן `SHLISHUK/dist/` אל `httpdocs/shlishuk/` בשרת. אפשר ב-workflow FTP נפרד (כמו `deploy-plesk.yml`, עם `local-dir: ./SHLISHUK/dist/` ו-`server-dir: ./httpdocs/shlishuk/`, אחרי שלב build).
6. **הפנה את ה-short-link:** עדכן את `l5k.me/avn6C` שיצביע ל-`https://markolitly.co.il/shlishuk/`. ברגע שזה עובד — אפס שבירה ללקוחות.
7. **Supabase:** ודא שהדומיין החדש מורשה ב-Supabase (Auth → URL Configuration / CORS) אם יש התחברות.
8. עדכן את הקישורים בדף הנחיתה (`production_deploy/index.html`) משלוש מופעי `https://l5k.me/avn6C` — רק אם תרצה קישור ישיר במקום ה-short-link.

> **גבול גזרה:** עד שכל זה אומת, **אל תכבה** את פריסת ה-GitHub Pages של שלישוק — היא הייצור הנוכחי.

---

## נספח A — תוכן `.github/workflows/deploy-plesk.yml`
(רק אם הקובץ חסר — אחרת דלג)

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

## נספח B — תוכן `production_deploy/.htaccess`
ראה את הקובץ הקיים בריפו תחת `production_deploy/.htaccess` (כבר נוצר).

---

## בדיקה עצמית — האם המסמך מובן ושלם?

- ✅ **קונטקסט בהתחלה** — מה הפרויקט, איפה כל רכיב, מה היעד, מה אסור לגעת.
- ✅ **מבנה תיקיות מפורש** — כולל מה נפרס ולאן.
- ✅ **קבצים מוכנים** — workflow + .htaccess כבר בריפו, עם נספח לשחזור.
- ✅ **הפרדה ברורה** בין מה שהסוכן עושה (קוד, commit, push, אימות) למה שדורש אדם (פרטי FTP, Secrets).
- ✅ **שלב אימות מפורש** עם רשימת תיוג — הסוכן לא יסיים בלי לוודא שהדף חי.
- ✅ **טיפול בכשל הנפוץ** (יעד FTP שגוי → תמונות שבורות → תיקון server-dir).
- ✅ **דומיין כפול + תקופת מעבר** מכוסה, כולל המגבלה שאין פקיעה אוטומטית.
- ✅ **גבולות גזרה** — שלישוק, DNS, מחיקות, Vercel.

**נקודת תלות יחידה שדורשת אדם:** פרטי ה-FTP וה-Secrets (סעיפים 3–4). כל השאר אוטומטי.
