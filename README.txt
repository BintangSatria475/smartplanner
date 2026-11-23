SMART KANTIN PLANNER - PERBAIKAN CSS

Struktur folder wajib:
smartplanner/
  app.py
  templates/
    index.html
  static/
    style.css

Cara menjalankan:
1. Pastikan Python dan Flask sudah terpasang.
2. Buka terminal di folder smartplanner.
3. Jalankan: python -m pip install flask
4. Jalankan: python app.py
5. Buka alamat http://127.0.0.1:5000

PENTING:
- Jangan meletakkan index.html sejajar dengan app.py. Flask mencari template di folder templates.
- Jangan meletakkan style.css sejajar dengan app.py. Flask mencari CSS di folder static.
- File HTML sudah memanggil CSS menggunakan url_for('static', filename='style.css').
- Data menu pada app.py saat ini masih disimpan di memori. Data akan kembali ke data awal jika server dimatikan/restart.
