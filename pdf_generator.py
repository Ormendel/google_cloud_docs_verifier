from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from bidi.algorithm import get_display
import arabic_reshaper
import os
import random
from datetime import datetime, timedelta

# רשום את הפונט
pdfmetrics.registerFont(TTFont('Alef', 'fonts/Alef-Regular.ttf'))


# פונקציה לעיבוד טקסט בעברית (כדי שיראה נכון מימין לשמאל)
def prepare_hebrew_text(text):
    reshaped_text = arabic_reshaper.reshape(text)
    return get_display(reshaped_text)


# נתונים לדוגמה
NAMES = ["דניאל לוי", "משה כהן", "נועה ישראלי", "אורי רביב", "שירה גולד"]
ADDRESSES = [
    "הרצל 12, תל אביב", "העצמאות 5, חיפה", "דוד המלך 33, ירושלים",
    "רוטשילד 20, ראשון לציון", "הגליל 9, באר שבע"
]


def random_date(start_year=2015, end_year=2023):
    start = datetime(year=start_year, month=1, day=1)
    end = datetime(year=end_year, month=12, day=31)
    random_days = random.randint(0, (end - start).days)
    return (start + timedelta(days=random_days)).strftime("%d/%m/%Y")


def create_fake_id_pdf(name, address, issue_date, save_path):
    c = canvas.Canvas(save_path)
    c.setFont("Alef", 14)
    c.drawRightString(500, 750, prepare_hebrew_text(f"שם: {name}"))
    c.drawRightString(500, 730, prepare_hebrew_text(f"כתובת: {address}"))
    c.drawRightString(500, 710, prepare_hebrew_text(f"תאריך הוצאה: {issue_date}"))
    c.save()


def generate_batch(num_files=5, output_folder="data"):
    os.makedirs(output_folder, exist_ok=True)

    for i in range(num_files):
        name = random.choice(NAMES)
        address = random.choice(ADDRESSES)
        issue_date = random_date()
        file_path = os.path.join(output_folder, f"id_{i + 1}.pdf")
        create_fake_id_pdf(name, address, issue_date, file_path)
        print(f"✅ נוצר קובץ: {file_path}")


if __name__ == "__main__":
    generate_batch()
