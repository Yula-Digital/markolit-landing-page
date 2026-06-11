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
- **`main`** — ייצור. **push אליו פורס את שלישוק חי ללקוחות** (GitHub Pages).
- **`backup/<תאריך>`** — ענפי גיבוי. **גיבוי שלישוק תמיד לכאן, לעולם לא ל-main.**

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

## 5. כללי זהב

- ✅ עריכת האתר = שינוי ב-`production_deploy/` + commit + push ל-main. זהו.
- ✅ גיבוי שלישוק = ענף `backup/<תאריך>` בלבד.
- ❌ אל תערוך ידנית את ענף `plesk-deploy` (נדרס אוטומטית).
- ❌ אל תדחוף ל-`main` של שלישוק אלא אם אתה **מכוון** לפרוס חי.
- ❌ אל תיגע ב-Vercel הישן (`markolit_landing_page`) ולא ב-DNS.
- ❌ משתמש המערכת `imarkolitl` ב-Plesk משותף עם חברה אחרת — אל תשנה סיסמתו.

📄 פירוט מלא של ארכיטקטורת הפריסה: `COWORK_DEPLOY_INSTRUCTIONS.md`.
