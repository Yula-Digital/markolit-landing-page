# BACKUP_PROS — פלואו גיבוי ופריסה אחרי שינויים
### (נטען אוטומטית בתחילת כל שיחה בפרויקט הזה דרך hook)

מסמך זה מסביר **איך מגבים ומפרסמים שינויים** בפרויקט מרכולית: אילו ענפים קיימים, איפה כל דבר יושב, ואיך מבצעים commit + push אחרי שינוי.

---

## 1. שני ריפו נפרדים — דע באיזה אתה

| ריפו | מיקום מקומי | Remote | מה זה |
|---|---|---|---|
| **דף הנחיתה** | `C:\markolit_landing_page\` (השורש) | `Yula-Digital/markolit-landing-page` | האתר הסטטי של מרכולית |
| **שלישוק / מבצעים** | `C:\markolit_landing_page\SHLISHUK\` | `rordan-ai/rordan-ai.github.io` | אפליקציית Vite נפרדת (gitignored בריפו הראשי) |

> ⚠️ `SHLISHUK/` הוא ריפו git **נפרד לחלוטין**. פקודות git בשורש משפיעות רק על דף הנחיתה.

---

## 2. ענפים ומה תפקידם

### ריפו דף הנחיתה (`Yula-Digital/markolit-landing-page`)
- **`main`** — ענף העבודה. **כאן אתה עורך ודוחף.** מקור האמת.
- **`plesk-deploy`** — ענף פריסה **אוטומטי**. השורש שלו = תוכן `production_deploy/`. **אסור לערוך אותו ידנית** — הוא נדרס בכל סנכרון על ידי GitHub Action.

### ריפו שלישוק (`rordan-ai/rordan-ai.github.io`)
- **`main`** — ייצור על **GitHub Pages**. **push אליו פורס את שלישוק חי ללקוחות.**
- **`backup/<תאריך>`** — ענפי גיבוי. **גיבוי שלישוק תמיד לכאן, לעולם לא ל-main.**
- **`plesk-shlishuk-ci`** — ענף CI לפריסה אל **תת-הדומיין** `shlishuk.markolitly.co.il`. push אליו מריץ build ובונה את ה-`plesk-shlishuk`. (מכיל את הקוד + workflow `build-plesk-shlishuk.yml`.)
- **`plesk-shlishuk`** — האתר ה**בנוי** (שורש = dist). Plesk Git של תת-הדומיין מושך ומפרסם אותו אוטומטית. **אסור לערוך ידנית** — נדרס בכל build.

---

## 3. איך מבצעים commit + push אחרי שינוי — דף הנחיתה

עורכים קבצים תחת **`production_deploy/`** (זה מה שמתפרסם לאתר), ואז:

```bash
cd /c/markolit_landing_page
git add -A
git commit -m "תיאור השינוי"
git push origin main
```

**מה קורה אוטומטית אחרי ה-push** (הצינור המלא — אין צורך לעשות כלום נוסף):
```
push ל-main
  → GitHub Action "sync-plesk-deploy-branch" ממפה production_deploy/ → ענף plesk-deploy
  → GitHub webhook מודיע ל-Plesk
  → Plesk Git מושך plesk-deploy ומפרסם ל-httpdocs
  → חי על https://markolitly.co.il (תוך ~דקה)
```

> רק שינויים תחת `production_deploy/**` מפעילים פריסה לאתר. שינוי בקבצים אחרים (מסמכים, מקור) — נשמר ב-main אבל לא משנה את האתר.

---

## 4. איך מבצעים גיבוי — שלישוק (נוהל זהירות)

**לעולם לא דוחפים שינויי-עבודה ל-`main` של שלישוק** (זה פורס חי). גיבוי תמיד לענף:

```bash
cd /c/markolit_landing_page/SHLISHUK
git checkout -b backup/<תאריך>            # למשל backup/2026-06-11
git add -A -- . ':!setup/backups'          # לא לכלול גיבויי DB כבדים (~22MB)
git commit -m "Backup shlishuk WIP <תאריך>"
git push -u origin backup/<תאריך>
# החזרת עץ העבודה למצב המקורי (main + WIP לא-מקומיט):
git checkout main
git checkout backup/<תאריך> -- .
git reset -q HEAD .
```

---

## 4.1 פריסת שלישוק אל תת-הדומיין (build → push) — markolitly.co.il/shlishuk

שלישוק על תת-הדומיין הוא אפליקציית Vite — **חייב build** (בניגוד לדף הנחיתה הסטטי). הצינור עובד דרך GitHub Actions, **בלי לגעת ב-main / GitHub Pages**:

```
push ל-ענף  plesk-shlishuk-ci   (בריפו שלישוק)
  → GitHub Action "build-plesk-shlishuk.yml" מריץ npm run build (3 דפים + אדמין)
  → דוחף את ה-dist לענף  plesk-shlishuk
  → GitHub webhook מודיע ל-Plesk
  → Plesk Git של תת-הדומיין מושך plesk-shlishuk ומפרסם אוטומטית
  → חי על https://shlishuk.markolitly.co.il
```

**איך לפרוס מחדש שלישוק לתת-הדומיין** (אחרי שינוי **קוד**):
```bash
# מענף main העדכני, מעדכנים את ה-CI ומריצים build:
cd /c/markolit_landing_page/SHLISHUK
git fetch origin main
git push origin origin/main:plesk-shlishuk-ci --force   # מסנכרן את ה-CI ל-main ומריץ build
```
לחלופין: בטאב **Actions** של ריפו שלישוק → "Build shlishuk for Plesk subdomain" → **Run workflow**.

> **שים לב:** תוכן (טקסטים/תמונות שעורכים באדמין) נשמר ב-**Supabase** ונטען חי — **לא דורש build**. הוא מופיע מיד גם ב-GitHub Pages וגם בתת-הדומיין. build נדרש **רק לשינויי קוד**.

---

## 5. כללי זהב

- ✅ עריכת האתר = שינוי ב-`production_deploy/` + commit + push ל-main. זהו.
- ✅ גיבוי שלישוק = ענף `backup/<תאריך>` בלבד.
- ❌ אל תערוך ידנית את הענפים `plesk-deploy` ו-`plesk-shlishuk` (נדרסים אוטומטית).
- ✅ פריסת שלישוק לתת-הדומיין = push ל-`plesk-shlishuk-ci` (סעיף 4.1). לא נוגע ב-GitHub Pages.
- ❌ אל תדחוף ל-`main` של שלישוק אלא אם אתה **מכוון** לפרוס חי.
- ❌ אל תיגע ב-Vercel הישן (`markolit_landing_page`) ולא ב-DNS.
- ❌ משתמש המערכת `imarkolitl` ב-Plesk משותף עם חברה אחרת — אל תשנה סיסמתו.

---

## 6. סביבת פיתוח (DEV מול PROD) — דף הנחיתה

ריפו אחד, שני ענפים:
- **`main`** = **פרוד (חי)**. כל push לכאן עולה ל-`markolitly.co.il` תוך ~דקה.
- **`dev`** = **פיתוח (סנדבוקס)**. דוחפים לכאן כמה שרוצים — **לא מתפרסם** לאתר החי.

**תצוגה מקדימה מקומית:** הרץ (דאבל-קליק) את **`preview.cmd`** בשורש → פתח `http://localhost:8765`. מה שרואים = בדיוק מה שיעלה.

**זרימת עבודה:**
```bash
cd /c/markolit_landing_page
git checkout dev                 # עוברים לסביבת הפיתוח
# ... עורכים production_deploy/ ...  (preview.cmd לתצוגה)
git add -A && git commit -m "תיאור" && git push origin dev    # נשמר, לא חי

# כשמרוצים — מעלים לאוויר:
git checkout main
git merge dev
git push origin main             # → מתפרסם חי
git checkout dev                 # חוזרים לפיתוח
```

> כלל: עובדים תמיד על `dev`. `main` מתעדכן רק במיזוג מכוון = שום הפתעות חיות.

---

📄 פירוט מלא של ארכיטקטורת הפריסה: `COWORK_DEPLOY_INSTRUCTIONS.md`.
