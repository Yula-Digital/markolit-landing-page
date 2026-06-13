# מיפוי שכבות — דף הנחיתה (הירו) · production_deploy/index.html

> מסמך עזר לתיקוני UI. הדף בנוי כ**artboard צרוב + overlays חדים**.

## העיקרון המבני
`base-art` = **`markolit-composed.png` (2160×3840)** — תמונה אחת שמכילה את **כל העיצוב הצרוב**, חתוכה לפרוסות (`.svg-slice` עם `data-y`/`data-h` + `overflow:hidden`). מעליה יושבות שכבות overlay חדות שמכסות אזורים ספציפיים.

## שכבות סקשן ההירו (`.svg-slice[data-y="0"]`), מלמטה למעלה

| z | מחלקה | סוג | תפקיד | יחידת מידה |
|---|---|---|---|---|
| 1 | `.base-art` | IMG (העיצוב הצרוב המלא) | רקע — **הכול צרוב כאן** | `width:100%` של הבמה |
| 2 | `.landscape-cover` | div + **תמונת נוף** (bg) | מכסה את הנוף הצרוב בגרסה חדה | % |
| 2 | `.hero-main-photo` | PNG שקוף | תמונת משפחה חדה | % + `transform` |
| 3 | `.hero-headline-wrap` | PNG כותרת | כותרת חדה | % + `transform` |
| 3 | `.hero-tagline-wrap` | טקסט HTML | תגית חדה | % + `transform` |
| 4 | `.slice-top-bar` | מכל הנווט | מכיל את הנווט; ממוקם 124%/135px (דסקטופ) | **px קבוע** |
| 4 | `.slice-top-bar > .nav-bg` | div לבן | **רקע הבר הלבן — שכבה עצמאית** (בודד מהתפריט) | % / px |
| 4 | `.slice-top-bar > .main-menu-svg` | SVG inline | 5 פריטי התפריט (ה-`<rect>` הלבן הוסר → שקוף) | viewBox |
| 4 | `.slice-top-bar > .strip-logo` | IMG | לוגו (ימין) | % |
| 5 | `.slice-top-bar > .special-offer-badge` | button+IMG | אייקון SPECIAL OFFER (שמאל) | % |
| 4 | `.benefits-strip-svg` | IMG (4 סמלים+טקסט) | רצועת היתרונות; רקע בז' מכסה שאריות base-art | % |
| 5 | `.club-cover` + `.club-icon-replace` | div + IMG | מחליפים את הסמל ה-3 ("מועדון") — **overlay נפרד!** | % |
| 5 | `.benefits-seps` | div | מפרידים (מוסתר: `display:none`) | % |
| 5 | `a.hit` | קישורים שקופים | אזורי לחיצה | % |

## תלויות והתנגשויות ידועות (מקור באגים)
- **כפל איור** (ליד "חוויה כפרית"): `.base-art` מכיל נוף צרוב **+** `.landscape-cover` תמונת נוף שנייה. בהגדלת הדף הן נפרדות → שתיהן נראות.
- **קווי גבול שלא זזים בהגדלה**: ה-overlays ביחידות מעורבות (px קבוע בבר הלבן 135px מול % ב-base-art) → מתפצלים ונחשף ה-base-art הצרוב.
- **המסגרת מתיישרת מושלם רק ברוחב אחד** — זו מהות ה-artboard+overlays.
- **הסמל ה-3 ברצועה** הוא `.club-icon-replace` נפרד (לא בתוך `.benefits-strip-svg`) — להזיז את הרצועה צריך להזיז את כל 3 השכבות יחד.

## כלל זהב לתיקונים
כל overlay חייב להתיישר על ה-base-art שמאחוריו. שינוי יחידות (px↔%) שובר את ההתאמה בהגדלה. לרובסטיות בהגדלה — **כל ה-overlays צריכים אותה יחידה (% של הבמה)**.
