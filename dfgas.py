import os
import shutil
from datetime import datetime

def delete_okx_dirs(base_path):
    count = 0
    log_entries = []

    for root, dirs, files in os.walk(base_path):
        for dir_name in dirs:
            if dir_name == "mcohilncbfahbmgdjkbpemcciiolgcge":
                parent = os.path.basename(root)
                if parent == "Local Extension Settings":
                    full_path = os.path.join(root, dir_name)
                    try:
                        shutil.rmtree(full_path)
                        msg = f"✅ Đã xóa: {full_path}"
                        print(msg)
                        log_entries.append(msg)
                        count += 1
                    except Exception as e:
                        msg = f"❌ Lỗi khi xóa {full_path}: {e}"
                        print(msg)
                        log_entries.append(msg)

    summary = f"🗑️ Tổng cộng đã xóa {count} thư mục OKX."
    print(summary)
    log_entries.append(summary)

    # Ghi log ra file
    log_filename = f"log_delete_okx_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(log_filename, "w", encoding="utf-8") as log_file:
        log_file.write(f"--- Log chạy lúc {datetime.now()} ---\n")
        for entry in log_entries:
            log_file.write(entry + "\n")
    
    print(f"📄 Log chi tiết đã ghi vào: {log_filename}")

if __name__ == "__main__":
    BASE_DIR = r"D:\\"  # 💡 Thay bằng thư mục gốc chứa các profile
    delete_okx_dirs(BASE_DIR)
    input("Nhấn Enter để thoát...")
