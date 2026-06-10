# הוראות פריסה אוטומטית — דף הנחיתה של מרכולית אל markolitly.co.il
### מסמך הנחיה לסוכן Cowork · גרסה 1.0

---

## 0. קונטקסט — קרא קודם

אתה עומד להפעיל **פריסה אוטומטית** של דף הנחיתה של "מרכולית" אל הדומיין `markolitly.co.il`.

**מה זה הפרויקט:**
- ריפו GitHub: `rordan-ai/markolit-landing-page`.
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

ב-`github.com/rordan-ai/markolit-landing-page` → **Settings** → **Secrets and variables** → **Actions** → **New repository secret**. הוסף שלושה:

| שם ה-Secret | ערך |
|---|---|
| `FTP_SERVER`   | ה-FTP host מסעיף 3 |
| `FTP_USERNAME` | שם המשתמש |
| `FTP_PASSWORD` | הסיסמה |

> ⚠️ אם הסוכן יכול לגשת ל-GitHub עם `gh` CLI ובהרשאה מתאימה, אפשר להגדיר כך:
> ```
> gh secret set FTP_SERVER   --repo rordan-ai/markolit-landing-page --body "<host>"
> gh secret set FTP_USERNAME --repo rordan-ai/markolit-landing-page --body "<user>"
> gh secret set FTP_PASSWORD --repo rordan-ai/markolit-landing-page --body "<pass>"
> ```
> אחרת — הנחה את המשתמש לעשות זאת ידנית דרך ה-UI.

---

## 5. הפעלה ראשונה — צעד אחר צעד

1. **ודא ש-`production_deploy/` ו-`.github/workflows/deploy-plesk.yml` נמצאים תחת git** (בסטטוס ההתחלתי הם היו untracked):
   ```
   git add production_deploy .github/workflows/deploy-plesk.yml COWORK_DEPLOY_INSTRUCTIONS.md
   git commit -m "Add Plesk auto-deploy for landing page (production_deploy → markolitly.co.il)"
   git push origin main
   ```
2. ה-push יפעיל אוטומטית את ה-workflow. עקוב ב-**Actions** בריפו (או `gh run watch`).
3. אם ה-workflow נכשל ב"אימות Secrets" — ה-Secrets לא הוגדרו (סעיף 4). הגדר והרץ מחדש (`workflow_dispatch` או push חוזר).

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
