# פריסת דף הנחיתה של מרכולית — markolitly.co.il
### מסמך ייחוס · גרסה 3.0 · ✅ הפריסה האוטומטית הוקמה ועובדת

---

## ✅ סטטוס: חי ואוטומטי (אומת מקצה לקצה ב-2026-06-11)

דף הנחיתה **חי על `https://markolitly.co.il`** ומתעדכן **אוטומטית** בכל שינוי. אומת מקצה לקצה: שינוי ל-`production_deploy/` → הופיע על האתר החי תוך פחות מדקה, ללא התערבות.

**אין צורך לעשות כלום כדי לפרוס — רק לערוך ולדחוף ל-`main`.**

---

## 🔄 איך הפריסה עובדת (הצינור)

```
עריכה ב-production_deploy/  →  git push origin main
        ↓
GitHub Action "sync-plesk-deploy-branch"  (מסנכרן production_deploy/ → ענף plesk-deploy)
        ↓
GitHub webhook  →  Plesk  (uuid מאובטח)
        ↓
Plesk Git מושך את ענף plesk-deploy ומפרסם אוטומטית ל-httpdocs
        ↓
חי על https://markolitly.co.il
```

**למה ענף `plesk-deploy`?** התוכן לייצור נמצא בתת-התיקייה `production_deploy/`, אבל Plesk Git מפרסם את **שורש** הענף. ה-Action ממפה את תוכן `production_deploy/` לשורש ענף `plesk-deploy`, כך ש-Plesk מפרסם בדיוק את הקבצים הנכונים (index.html, .htaccess, assets/) — בלי לשבור כלום.

---

## 🧩 הרכיבים (לתחזוקה עתידית)

| רכיב | מיקום | תפקיד |
|---|---|---|
| מקור האתר | `production_deploy/` בריפו `Yula-Digital/markolit-landing-page` (ענף `main`) | מה שעורכים |
| Action סנכרון | `.github/workflows/sync-plesk-deploy-branch.yml` | מסנכרן production_deploy/ → ענף `plesk-deploy` |
| ענף פריסה | `plesk-deploy` (שורש = קבצי האתר) | מה ש-Plesk מושך. **לא לערוך ידנית** — נוצר אוטומטית |
| webhook | GitHub repo → Settings → Webhooks (id 639715544) | מודיע ל-Plesk על push |
| Plesk Git | פאנל Plesk → markolitly.co.il (site_id 351) → Git | מושך plesk-deploy ומפרסם ל-httpdocs. מצב **אוטומטי** |
| שרת | Plesk/אינטרוויז'ן, `httpdocs/` של markolitly.co.il (IP 80.244.168.70) | מארח את האתר החי |

---

## 🛠️ פעולות נפוצות

- **לעדכן את הדף:** ערוך קובץ ב-`production_deploy/`, `git push origin main`. זהו. תוך ~דקה זה חי.
- **לפרוס ידנית (בלי לחכות ל-webhook):** פאנל Plesk → markolitly.co.il → Git → markolit-landing-page.git → "פרוס כעת".
- **לעצור פריסה אוטומטית זמנית:** באותו מסך Git → הגדרות → מצב פריסה → "ידני" (אז פריסה רק בלחיצה ידנית).

---

## 🚨 גבולות גזרה (עדיין בתוקף)

- ❌ **אל תיגע בפרויקט ה-Vercel הישן** (`markolit_landing_page`, team `rordan-ais-projects`) — הוא נשאר חי כ-fallback, קפוא על commit `8972468`. בונים מקביל, לא במקום.
- ❌ **אל תדחוף ל-`main` של `rordan-ai/rordan-ai.github.io`** (שלישוק) — זה פורס שלישוק חי. גיבוי תמיד לענף (ראה למטה).
- ❌ אל תיגע ב-DNS.
- ❌ אל תערוך ידנית את ענף `plesk-deploy` — הוא נדרס בכל סנכרון.
- ⚠️ **משתמש המערכת `imarkolitl` ב-Plesk משותף עם חברה אחרת** — אל תשנה את סיסמתו. (לכן בחרנו Plesk Git ולא FTP.)

---

## 💾 גיבוי שלישוק / מבצעים (ריפו נפרד)

שלישוק = ריפו נפרד `rordan-ai/rordan-ai.github.io` בתיקייה `SHLISHUK/`, חי על GitHub Pages. ה-short-link `l5k.me/avn6C` מפנה אליו (302 → `rordan-ai.github.io/SHLISHUK/`). גיבוי **תמיד לענף, לעולם לא ל-main** (push ל-main פורס חי):
```bash
cd SHLISHUK
git checkout -b backup/<תאריך>
git add -A -- . ':!setup/backups'
git commit -m "Backup shlishuk WIP <תאריך>"
git push -u origin backup/<תאריך>
git checkout main; git checkout backup/<תאריך> -- .; git reset -q HEAD .
```

---

## 🔮 עתידי — שלישוק תחת markolitly.co.il

קיים כבר תת-דומיין `shlishuk.markolitly.co.il` בפאנל Plesk (site_id 352, DNS עדיין לא מכוון). אפשר בעתיד לפרוס אליו את אפליקציית שלישוק (Vite — דורש `npm run build`, base נכון, ו-SPA fallback), ולהפנות את ה-short-link. לא דחוף — שלישוק עובד היום על GitHub Pages.
