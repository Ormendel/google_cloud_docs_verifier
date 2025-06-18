import fitz  # pymupdf
import os

# שדות חובה למסמך תקני
REQUIRED_FIELDS = ["שם:", "כתובת:", ":תאריך הוצאה"]


def extract_text_from_pdf(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        print(f"The text is: {text}")
        return text
    except Exception as e:
        print(f"❌ שגיאה בקריאת הקובץ {path}: {e}")
        return ""


def validate_pdf(path):
    text = extract_text_from_pdf(path)
    missing_fields = [field for field in REQUIRED_FIELDS if field not in text]

    if missing_fields:
        return False, missing_fields
    return True, []


def validate_all_pdfs(folder_path="data"):
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]
    print(f"\n📂 בודק {len(pdf_files)} קבצי PDF בתיקייה: {folder_path}\n")

    for file_name in pdf_files:
        file_path = os.path.join(folder_path, file_name)
        is_valid, missing = validate_pdf(file_path)
        if is_valid:
            print(f"✅ {file_name} תקין.")
        else:
            print(f"⚠️ {file_name} לא תקין. חסרים שדות: {', '.join(missing)}")


if __name__ == "__main__":
    validate_all_pdfs()
