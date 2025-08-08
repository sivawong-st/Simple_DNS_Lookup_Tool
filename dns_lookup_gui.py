import tkinter as tk
from tkinter import scrolledtext,messagebox
import dns.resolver
import threading
import socket

def query_dns(domain, output_widget):
    try:
        output_widget.insert(tk.END, f"--- ผลลัพธ์ของ {domain} ---\n")
        
        #Query A record
        try:
            answers = dns.resolver.resolve(domain, 'A')
            ips = [rdata.to_text() for rdata in answers]
            output_widget.insert(tk.END, f"A records: {', '.join(ips)}\n")
        except Exception:
            output_widget.insert(tk.END, "A records: ไม่พบ\n")
        
        #Query MX record
        try:
            answers = dns.resolver.resolve(domain, 'MX')
            mxs = [rdata.exchange.to_text() for rdata in answers]
            output_widget.insert(tk.END, f"MX records: {', '.join(mxs)}\n")
        except Exception:
            output_widget.insert(tk.END, "MX records: ไม่พบ\n")
        
        #Query CNAME record
        try:
            answers = dns.resolver.resolve(domain, 'CNAME')
            cnames = [rdata.to_text() for rdata in answers]
            output_widget.insert(tk.END, f"CNAME records: {', '.join(cnames)}\n")
        except Exception:
            output_widget.insert(tk.END, "CNAME records: ไม่พบ\n")
        
        output_widget.insert(tk.END, "\n")
        output_widget.see(tk.END)
    except Exception as e:
        output_widget.insert(tk.END, f"เกิดข้อผิดพลาด: {e}\n\n")
        output_widget.see(tk.END)

def reverse_dns_lookup(ip, output_widget):
    try:
        domain = socket.gethostbyaddr(ip)[0]
        output_widget.insert(tk.END, f"--- ผลลัพธ์ของ IP {ip} ---\n")
        output_widget.insert(tk.END, f"Domain name: {domain}\n\n")
        output_widget.see(tk.END)
    except socket.herror:
        output_widget.insert(tk.END, f"ไม่พบชื่อโดเมนสำหรับ IP: {ip}\n\n")
        output_widget.see(tk.END)
    except Exception as e:
        output_widget.insert(tk.END, f"เกิดข้อผิดพลาด: {e}\n\n")
        output_widget.see(tk.END)

def start_lookup():
    mode = mode_var.get()
    input_value = entry_input.get().strip()
    if not input_value:
        messagebox.showwarning("คำเตือน", "กรุณาใส่ข้อมูลก่อนครับ")
        return
    
    text_output.delete('1.0', tk.END)

    if mode == "domain":
        threading.Thread(target=query_dns, args=(input_value, text_output), daemon=True).start()
    else:
        threading.Thread(target=reverse_dns_lookup, args=(input_value, text_output), daemon=True).start()

#สร้าง GUI
root = tk.Tk()
root.title("DNS Lookup Tool")
root.geometry("600x450")
root.configure(bg="#f0f4f8")

#ฟอนต์ที่ใช้
FONT_LABEL = ("Segoe UI", 11)
FONT_ENTRY = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI Semibold", 12)
FONT_OUTPUT = ("Consolas", 11)

#Frame โหมดเลือก
frame_mode = tk.LabelFrame(root, text="เลือกโหมดการค้นหา", bg="#f0f4f8", font=("Segoe UI Semibold", 12))
frame_mode.pack(fill="x", padx=15, pady=10)

mode_var = tk.StringVar(value="domain")

rb1 = tk.Radiobutton(frame_mode, text="Lookup Domain → DNS Records", variable=mode_var, value="domain", bg="#f0f4f8", font=FONT_LABEL)
rb1.pack(side=tk.LEFT, padx=20, pady=5)

rb2 = tk.Radiobutton(frame_mode, text="Reverse IP → Domain", variable=mode_var, value="reverse", bg="#f0f4f8", font=FONT_LABEL)
rb2.pack(side=tk.LEFT, padx=20, pady=5)

#Frame ใส่ข้อมูล
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(fill="x", padx=15, pady=5)

label = tk.Label(frame_input, text="กรอกโดเมน หรือ IP (ได้ครั้งละ 1 รายการ):", bg="#f0f4f8", font=FONT_LABEL)
label.pack(anchor="w")

entry_input = tk.Entry(frame_input, font=FONT_ENTRY)
entry_input.pack(fill="x", pady=5)
entry_input.focus()

#ปุ่มค้นหา
btn_lookup = tk.Button(root, text="ค้นหา DNS", font=FONT_BUTTON, bg="#4a90e2", fg="white", activebackground="#357ABD", activeforeground="white", command=start_lookup)
btn_lookup.pack(pady=10)

#กล่องแสดงผลลัพธ์
text_output = scrolledtext.ScrolledText(root, width=70, height=15, font=FONT_OUTPUT, bg="white", fg="#333333", relief="sunken", bd=2)
text_output.pack(padx=15, pady=5, fill="both", expand=True)

root.mainloop()