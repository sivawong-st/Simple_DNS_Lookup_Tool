# Simple_DNS_Lookup_Tool

โปรแกรมค้นหา DNS ด้วย Python และ Tkinter แบบง่าย ๆ  
สามารถค้นหา DNS records ของโดเมน หรือแปลง IP เป็นชื่อโดเมน (Reverse DNS Lookup) ผ่าน GUI ใช้งานสะดวก

---

## คุณสมบัติหลัก

- Lookup Domain → แสดง DNS Records ได้แก่ A, MX, CNAME  
- Reverse IP → แปลง IP Address เป็นชื่อโดเมน (Reverse DNS Lookup)  
- ใช้งานแบบ Multi-threading ไม่ทำให้ GUI ค้าง  
- GUI สวยงาม ใช้งานง่ายด้วย Tkinter  
- แสดงผลลัพธ์ในกล่องข้อความพร้อม scrollbar  

---

## วิธีใช้งาน

1. ติดตั้ง Python 3.x และไลบรารีที่จำเป็น  
   ```bash
   pip install dnspython
