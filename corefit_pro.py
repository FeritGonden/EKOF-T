
from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import hashlib

BG_MAIN = "#111827"
BG_CARD = "#1F2937"
TEXT_MAIN = "#F9FAFB"
TEXT_SUB = "#D1D5DB"
ACCENT_COLOR = "#22D3EE"
PREMIUM_COLOR = "#F472B6"
DANGER_COLOR = "#EF4444"
SUCCESS_COLOR = "#10B981"

FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_SUBTITLE = ("Segoe UI", 12)
FONT_BODY = ("Segoe UI", 10)
FONT_BOLD = ("Segoe UI", 10, "bold")
FONT_BTN = ("Segoe UI", 11, "bold")


def veritabani_baslat():

    con = sqlite3.connect("corefit_final.db")
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            membership TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS programs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            program_name TEXT,
            goal TEXT,
            content_std TEXT,
            content_prem TEXT,
            min_bmi REAL,
            max_bmi REAL
        )
    """)

    cur.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cur.fetchone():
        pw_hash = hashlib.sha256("1234".encode()).hexdigest()
        cur.execute(
            "INSERT INTO users (username, password, role, membership) VALUES (?, ?, ?, ?)",
            ("admin", pw_hash, "admin", "premium")
        )

    cur.execute("SELECT count(*) FROM programs")
    if cur.fetchone()[0] == 0:
        programlar = [
            ("Mr. Olympia Hazırlık (Pro Cycle)", "Yarışmacı (Hardcore)",
             "Günde çift antrenman sistemi: Sabah 06:00 Aç Karnına Kardiyo (45dk) - Akşam 18:00 Hipertrofi Antrenmanı,"
             "Makro takibi: %60 Protein - %20 Yağ - %20 Karbonhidrat,"
             "Tuz Tüketimi: Son 4 hafta kademeli azaltılacak,"
             "Zorunlu Poz Pratiği: Her antrenman sonu 15 dakika ayna karşısında kas kasma,"
             "Su Tüketimi: Günde 6-7 litre,"
             "Uyku: Gece en az 8 saat + Öğlen 1 saat şekerleme",
             "ANABOLİK PROTOKOL: Haftalık 400mg Trenbolone Enanthate (Pzt-Per),"
             "KURUMA: Günlük 50mg Winstrol (Son 6 hafta),"
             "TESTOSTERON: Propionat 100mg (Gün aşırı enjeksiyon),"
             "KORUMA: Östrojen kontrolü için Arimidex + Karaciğer için NAC 600mg,"
             "SU ATIMI: Yarışma haftası Aldactone/Lasix protokolü,"
             "KAN TESTİ: Her 3 haftada bir Karaciğer Enzimleri (ALT/AST) kontrolü zorunlu!",
             19.0, 45.0),

            ("Miami Beach Shredded (Estetik)", "Plaj Vücudu",
             "Antrenman: Haftada 4 gün 'Push-Pull-Legs' + 1 gün 'Weak Point' çalışması,"
             "Karın Kası: Haftada 3 gün antrenman sonu 'Vacuum',"
             "Beslenme: Akşam 18:00'den sonra karbonhidrat alımını tamamen kes,"
             "Yasaklar: Şeker, Alkol ve Basit karbonhidratlar,"
             "Kahve: Günde 2 fincan sütsüz şekersiz filtre kahve,"
             "Cilt Bakımı: Deri incelmesi için haftada 1 kese ve sauna",
             "YAĞ YAKICI: Sabah aç karnına Clenbuterol (Piramit sistemi),"
             "BÖLGESEL: İnatçı alt karın yağları için Yohimbine HCL (Kardiyo öncesi),"
             "DAMARLANMA: Antrenman öncesi 5g Arjinin + 5g Sitrülin Malat,"
             "DİÜRETİK: Su atımı için Kiraz Sapı ve Mısır Püskülü çayı kürü,"
             "PEPTİD: Bronzlaşma ve yağ yakımı için Melanotan II desteği,"
             "L-CARNITINE: Antrenmandan 30dk önce 3000mg likit ampul",
             18.5, 29.0),

            ("Elit Crossfit & Atlet Performans", "Atletik Performans",
             "Güç: Patlayıcı kuvvet için Plyometrics ve Olympic Lifts,"
             "Dayanıklılık: Laktik asit toleransı için HIIT ve Tabata protokolleri,"
             "Isınma: Dinamik ısınma ve Foam Roller ile fasya gevşetme,"
             "Recovery: Antrenman sonrası buz banyosu veya kontrast duş,"
             "Beslenme: Antrenman hemen sonrası Yüksek Glisemik İndeksli Karbonhidrat",
             "BETA-ALANINE: Kas yanmasını geciktirmek için günlük 3g,"
             "CITRULLINE: Yorgunluk direnci için 6g Citrulline Malate,"
             "ATP: Maksimum enerji yenilenmesi için Kreatin HCL,"
             "UYKU: Derin uyku ve hormon dengesi için ZMA,"
             "EKLEM: Ağır yükler için Glukozamin Chondroitin MSM kompleksi,"
             "OKSİJEN: VO2 Max artışı için Cordyceps mantarı özütü",
             18.5, 30.0),

            ("Skinny Model Look (Podyum Fiziği)", "Zayıf Görünüm",
             "Kalori: Günlük 1200-1400 kalori arası sıkı kontrollü açık,"
             "Egzersiz: Ağırlık antrenmanı yerine Pilates, Reformer ve Yoga,"
             "Aktivite: Günde minimum 10.000 - 15.000 adım tempolu yürüyüş,"
             "Diyet: Şişkinlik yapan bakliyat ve süt ürünlerinden kaçınma,"
             "Akşam: Saat 19:00'dan sonra sadece sıvı detoks veya yeşil salata",
             "İŞTAH KONTROLÜ: Mide doluluğu için Glucomannan (Konjac kökü) lifi,"
             "METABOLİZMA: Günde 3 kapsül yüksek doz EGCG,"
             "ÖDEM: Sindirim ve su atımı için Bromelain,"
             "TATLI KRİZİ: Kan şekerini dengelemek için Krom Pikolinat,"
             "CİLT: Selülit görünümü engellemek için Kolajen Tip 1-3 peptitleri,"
             "YAĞ YAKIMI: Mitokondriyal destek için Asetil L-Carnitine",
             15.0, 25.0),

            ("Clean Bulk: Temiz Hacim", "Genel",
             "Kalori: Günde minimum 3500 Kalori hedefi,"
             "Antrenman: Temel bileşik egzersizler odaklı (Squat - Deadlift - Bench Press),"
             "Süre: Antrenman süresi 50 dakikayı geçmemeli,"
             "Beslenme: Her öğünde kaliteli karbonhidrat (Pirinç-Yulaf),"
             "Gece: Yatmadan önce Kazein proteini kaynağı (Lor peyniri)",
             "GAINER: Antrenman sonrası hemen yüksek kalorili Karbonhidrat tozu,"
             "KREATİN: Kas içi su tutumu ve güç için Monohidrat (Günlük 5g),"
             "İNSÜLİN: Karbonhidrat emilimi için Krom ve Tarçın ekstraktı,"
             "İŞTAH: B12 Vitamini kompleksi,"
             "TESTOSTERON: Doğal artış için Tribulus ve Ashwagandha,"
             "OMEGA-3: Enflamasyon önlemek için günde 3 kapsül Balık yağı",
             0, 18.49),

            ("Fit & Dengeli Yaşam", "Genel",
             "Rutin: Haftada 3 gün Full Body direnç antrenmanı,"
             "Kardiyo: Haftada 2 gün doğada orta tempo yürüyüş,"
             "Su: Günde 2.5 - 3 litre su tüketimi,"
             "Diyet: Paketli, işlenmiş ve trans yağ içeren gıdaların azaltılması,"
             "Kahvaltı: Güne mutlaka yüksek proteinli bir kahvaltı ile başlama",
             "MULTİVİTAMİN: Bağışıklık ve enerji için yüksek potentli kompleks,"
             "WHEY: Kas onarımı için antrenman sonrası İzole Whey Protein,"
             "ADAPTOGEN: Günlük stres yönetimi için Rhodiola Rosea,"
             "MAGNEZYUM: Uyku kalitesi ve kramp önlemek için Magnezyum Bisglisinat,"
             "BAĞIRSAK: Sindirim sistemi sağlığı için Probiyotik",
             18.5, 24.99),

            ("Metabolik Ateşleme (Yağ Yakımı)", "Genel",
             "Beslenme: Beyaz ekmek - Makarna ve Şekerin tamamen kesilmesi,"
             "Yöntem: Aralıklı Oruç (Intermittent Fasting) 16:8 metodu,"
             "Aktivite: Haftada 4 gün sabah aç karnına tempolu yürüyüş,"
             "Porsiyon: Yemeklerde küçük tabak kullanımı,"
             "Alışkanlık: Asansör yerine merdiven kullanımı",
             "YAĞ YAKICI: Termojenik etki için Kafein ve Sinefrin içeren takviyeler,"
             "KAN ŞEKERİ: Dengelemek için Berberine takviyesi,"
             "MİTOKONDRİ: Yağ yakımı için Asetil L-Carnitine,"
             "SABAH: Metabolizma için Elma Sirkesi ve Limon kürü,"
             "ÖDEM: Maydanoz kürü",
             25.0, 29.99),

            ("Yeni Bir Başlangıç (Obezite Kontrolü)", "Genel",
             "Egzersiz: Eklemlere yük bindirmemek için Yüzme ve Su içi egzersizler,"
             "Diyet: Gazlı içecekler ve meyve sularının tamamen bırakılması,"
             "Besin: Glisemik indeksi düşük sebze ağırlıklı beslenme,"
             "Sağlık: Doktor kontrolünde aylık kan değerleri takibi,"
             "Zihin: Psikolojik yeme bozukluğu için farkındalık çalışmaları",
             "İNSÜLİN: Direnci kırmak için Alfa Lipoik Asit (ALA),"
             "CİLT: Sarkmaları önlemek için yüksek doz Hidrolize Kolajen,"
             "VİTAMİN: D Vitamini seviyesini 50ng/mL üzerine çıkarmak için takviye,"
             "ENFLAMASYON: Zerdeçal (Curcumin) özütü,"
             "EKLEM: Ağrılar için Omega-3",
             30.0, 100.0),
        ]

        cur.executemany(
            "INSERT INTO programs (program_name, goal, content_std, content_prem, min_bmi, max_bmi) VALUES (?, ?, ?, ?, ?, ?)",
            programlar
        )

    con.commit()
    con.close()


def sifrele(sifre: str) -> str:
    return hashlib.sha256(sifre.encode()).hexdigest()



class ModernEntry(Entry):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.config(relief="flat", bg=BG_MAIN, fg="white", insertbackground="white", font=FONT_BODY)


class ModernButton(Button):
    def __init__(self, master, bg_color=ACCENT_COLOR, text_color=BG_MAIN, hover_color="#fff", **kw):
        super().__init__(master, **kw)
        self.bg = bg_color
        self.hover = hover_color
        self.config(
            bg=bg_color, fg=text_color, font=FONT_BTN, relief="flat",
            activebackground=hover_color, activeforeground=bg_color,
            cursor="hand2", padx=10, pady=5
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, _e):
        self["background"] = self.hover

    def on_leave(self, _e):
        self["background"] = self.bg


class CoreFitApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CoreFit - Professional")
        self.root.geometry("480x850")
        self.root.configure(bg=BG_MAIN)

        veritabani_baslat()

        self.giris_ekranini_goster()

    def temizle(self):
        for w in self.root.winfo_children():
            w.destroy()

    def nav_bar_ekle(self, geri_fonksiyonu=None):
        nav = Frame(self.root, bg=BG_MAIN, height=50)
        nav.pack(fill="x", side="top", pady=10, padx=10)

        if geri_fonksiyonu:
            btn_back = Button(
                nav, text="❮", font=("Arial", 18), bg=BG_MAIN, fg=TEXT_SUB,
                bd=0, activebackground=BG_MAIN, activeforeground="white",
                cursor="hand2", command=geri_fonksiyonu
            )
            btn_back.pack(side="left")

        Label(nav, text="CoreFit", font=("Segoe UI", 16, "bold"), bg=BG_MAIN, fg=ACCENT_COLOR).pack(side="left", padx=10)

    def create_card(self):
        card = Frame(self.root, bg=BG_CARD, padx=20, pady=30)
        card.place(relx=0.5, rely=0.5, anchor="center", width=380)
        return card

    def giris_ekranini_goster(self):
        self.temizle()

        Label(self.root, text="CORE\nFIT", font=("Segoe UI", 40, "bold"), bg=BG_MAIN, fg=ACCENT_COLOR).pack(pady=(60, 10))
        Label(self.root, text="Train Like a Pro", font=FONT_SUBTITLE, bg=BG_MAIN, fg=TEXT_SUB).pack(pady=(0, 30))

        card = self.create_card()
        card.place(rely=0.6)

        Label(card, text="Kullanıcı Adı", bg=BG_CARD, fg=TEXT_SUB, font=FONT_BODY, anchor="w").pack(fill="x")
        self.entry_user = ModernEntry(card)
        self.entry_user.pack(fill="x", pady=(5, 15), ipady=5)

        Label(card, text="Şifre", bg=BG_CARD, fg=TEXT_SUB, font=FONT_BODY, anchor="w").pack(fill="x")
        self.entry_pass = ModernEntry(card, show="•")
        self.entry_pass.pack(fill="x", pady=(5, 20), ipady=5)

        ModernButton(card, text="GİRİŞ YAP", command=self.giris_yap, bg_color=ACCENT_COLOR, width=20).pack(pady=10, fill="x")
        Frame(card, height=1, bg=BG_MAIN).pack(fill="x", pady=15)
        ModernButton(
            card, text="HESAP OLUŞTUR", command=self.kayit_ekrani_goster,
            bg_color=BG_MAIN, text_color=TEXT_SUB, hover_color=BG_CARD, width=20
        ).pack(fill="x")

    def giris_yap(self):
        kadi = self.entry_user.get()
        sifre_hash = sifrele(self.entry_pass.get())

        con = sqlite3.connect("corefit_final.db")
        cur = con.cursor()
        cur.execute("SELECT role, membership FROM users WHERE username=? AND password=?", (kadi, sifre_hash))
        user = cur.fetchone()
        con.close()

        if user:
            role, membership = user[0], user[1]
            if role == "admin":
                self.admin_ekranini_goster()
            else:
                self.user_ekranini_goster(kadi, membership)
        else:
            messagebox.showerror("Hata", "Giriş başarısız.")

    def kayit_ekrani_goster(self):
        self.temizle()
        self.nav_bar_ekle(geri_fonksiyonu=self.giris_ekranini_goster)

        card = self.create_card()
        Label(card, text="Yeni Üyelik", font=FONT_TITLE, bg=BG_CARD, fg="white").pack(pady=(0, 20))

        Label(card, text="Kullanıcı Adı", bg=BG_CARD, fg=TEXT_SUB, anchor="w").pack(fill="x")
        self.reg_user = ModernEntry(card)
        self.reg_user.pack(fill="x", pady=5, ipady=3)

        Label(card, text="Şifre", bg=BG_CARD, fg=TEXT_SUB, anchor="w").pack(fill="x")
        self.reg_pass = ModernEntry(card, show="•")
        self.reg_pass.pack(fill="x", pady=5, ipady=3)

        Label(card, text="Paket Seçimi", bg=BG_CARD, fg=TEXT_SUB, anchor="w").pack(fill="x")
        self.reg_tip = ttk.Combobox(card, values=["Standart", "Premium"], state="readonly", font=FONT_BODY)
        self.reg_tip.current(0)
        self.reg_tip.pack(fill="x", pady=5, ipady=3)

        Label(card, text="*Premium: Kürler ve detaylı planlar içindir.", bg=BG_CARD, fg=PREMIUM_COLOR, font=("Segoe UI", 9)).pack(pady=10)
        ModernButton(card, text="KAYDI TAMAMLA", command=self.kayit_ol, bg_color=SUCCESS_COLOR).pack(fill="x", pady=10)

    def kayit_ol(self):
        try:
            con = sqlite3.connect("corefit_final.db")
            cur = con.cursor()
            cur.execute(
                "INSERT INTO users (username, password, role, membership) VALUES (?, ?, ?, ?)",
                (self.reg_user.get(), sifrele(self.reg_pass.get()), "user", self.reg_tip.get().lower())
            )
            con.commit()
            con.close()

            messagebox.showinfo("CoreFit", "Kayıt Başarılı!")
            self.giris_ekranini_goster()
        except:
            messagebox.showerror("Hata", "Kullanıcı adı alınmış.")

    def user_ekranini_goster(self, username, membership):
        self.temizle()
        self.nav_bar_ekle(geri_fonksiyonu=self.giris_ekranini_goster)

        Label(self.root, text=f"Merhaba, {username}", font=FONT_TITLE, bg=BG_MAIN, fg="white").pack(pady=(20, 5))
        badge_color = PREMIUM_COLOR if membership == "premium" else TEXT_SUB
        Label(
            self.root, text=f"{membership.upper()} MEMBER", font=("Segoe UI", 9, "bold"),
            bg=BG_MAIN, fg=badge_color, bd=1, relief="solid"
        ).pack(pady=(0, 20), ipadx=5)

        card = self.create_card()

        Label(card, text="Fiziksel Bilgiler", font=FONT_BOLD, bg=BG_CARD, fg=ACCENT_COLOR).pack(anchor="w", pady=(0, 10))

        row1 = Frame(card, bg=BG_CARD)
        row1.pack(fill="x")
        Label(row1, text="Kilo (kg)", bg=BG_CARD, fg=TEXT_SUB, width=10, anchor="w").pack(side="left")
        self.u_kilo = ModernEntry(row1, width=10)
        self.u_kilo.pack(side="right", ipady=3)

        row2 = Frame(card, bg=BG_CARD)
        row2.pack(fill="x", pady=10)
        Label(row2, text="Boy (cm)", bg=BG_CARD, fg=TEXT_SUB, width=10, anchor="w").pack(side="left")
        self.u_boy = ModernEntry(row2, width=10)
        self.u_boy.pack(side="right", ipady=3)

        Label(card, text="---------------------------", bg=BG_CARD, fg=BG_MAIN).pack()

        Label(card, text="Vücut Hedefi", font=FONT_BOLD, bg=BG_CARD, fg=PREMIUM_COLOR).pack(anchor="w", pady=(10, 5))

        hedef_listesi = ["Genel"]
        if membership == "premium":
            hedef_listesi = ["Genel", "Plaj Vücudu", "Yarışmacı (Hardcore)", "Atletik Performans", "Zayıf Görünüm"]

        self.u_hedef = ttk.Combobox(
            card,
            values=hedef_listesi,
            state="readonly" if membership == "premium" else "disabled",
            font=FONT_BODY
        )
        self.u_hedef.current(0)
        self.u_hedef.pack(fill="x", ipady=3)

        if membership != "premium":
            Label(card, text="🔒 Bu özellik sadece Premium kullanıcılara özeldir.", bg=BG_CARD, fg="gray", font=("Segoe UI", 8)).pack(pady=(2, 0))

        ModernButton(card, text="ANALİZ ET", command=lambda: self.sonuc_goster(membership), bg_color=ACCENT_COLOR).pack(fill="x", pady=20)

    def sonuc_goster(self, membership):
        kilo_val = self.u_kilo.get()
        boy_val = self.u_boy.get()
        secilen_hedef = self.u_hedef.get()

        if not kilo_val or not boy_val:
            messagebox.showwarning("Eksik Bilgi", "Lütfen boy ve kilo giriniz.")
            return

        self.temizle()
        self.nav_bar_ekle(geri_fonksiyonu=self.giris_ekranini_goster)

        try:
            kilo = float(kilo_val)
            boy = float(boy_val)
            bmi = kilo / ((boy / 100) ** 2)

            hedef = secilen_hedef
            if membership != "premium":
                hedef = "Genel"

            con = sqlite3.connect("corefit_final.db")
            cur = con.cursor()

            cur.execute(
                "SELECT program_name, content_std, content_prem FROM programs "
                "WHERE ? >= min_bmi AND ? <= max_bmi AND goal = ?",
                (bmi, bmi, hedef)
            )
            prog = cur.fetchone()

            if not prog:
                cur.execute(
                    "SELECT program_name, content_std, content_prem FROM programs "
                    "WHERE ? >= min_bmi AND ? <= max_bmi AND goal = 'Genel'",
                    (bmi, bmi)
                )
                prog = cur.fetchone()
                if prog:
                    messagebox.showinfo(
                        "Bilgi",
                        f"Seçtiğin '{hedef}' hedefi BMI ({bmi:.1f}) değerine uygun değil.\nSana özel 'Genel' program getirildi."
                    )

            con.close()

            main_frame = Frame(self.root, bg=BG_MAIN)
            main_frame.pack(fill="both", expand=True, padx=20)

            durum_renk = SUCCESS_COLOR
            if bmi > 25:
                durum_renk = DANGER_COLOR
            if bmi < 18.5:
                durum_renk = "#FBBF24"

            Label(main_frame, text=f"BMI: {bmi:.1f}", font=("Segoe UI", 32, "bold"), bg=BG_MAIN, fg=durum_renk).pack(pady=(5, 0))

            if prog:
                Label(main_frame, text=prog[0], font=("Segoe UI", 16, "bold"), bg=BG_MAIN, fg="white", wraplength=400).pack(pady=5)

                content_card = Frame(main_frame, bg=BG_CARD, padx=15, pady=15)
                content_card.pack(fill="both", expand=True, pady=10)

                Label(content_card, text="📋 ANTRENMAN & BESLENME", bg=BG_CARD, fg=ACCENT_COLOR, font=FONT_BOLD).pack(anchor="w")
                Label(
                    content_card,
                    text=prog[1].replace(",", "\n• "),
                    bg=BG_CARD, fg=TEXT_SUB, justify="left",
                    font=FONT_BODY, wraplength=380
                ).pack(anchor="w", padx=10, pady=(5, 15))

                if membership == "premium":
                    header_text = "💉 KÜR DETAYLARI (HARDCORE)" if "Hardcore" in hedef else "⭐ PREMIUM PROTOKOL"
                    header_color = DANGER_COLOR if "Hardcore" in hedef else PREMIUM_COLOR

                    Frame(content_card, height=1, bg=BG_MAIN).pack(fill="x", pady=10)
                    Label(content_card, text=header_text, bg=BG_CARD, fg=header_color, font=FONT_BOLD).pack(anchor="w")
                    Label(
                        content_card,
                        text=prog[2].replace(",", "\n🔹 "),
                        bg=BG_CARD, fg="#FDE047", justify="left",
                        font=FONT_BODY, wraplength=380
                    ).pack(anchor="w", padx=10, pady=5)
                else:
                    Label(content_card, text="🔒 Premium içerikler (Kürler, Supplementler) kilitli", bg=BG_CARD, fg="gray").pack()
            else:
                Label(main_frame, text="Bu BMI aralığı için uygun program bulunamadı.", fg=DANGER_COLOR, bg=BG_MAIN).pack()

        except ValueError:
            messagebox.showerror("Hata", "Lütfen geçerli sayı girin.")

    def admin_ekranini_goster(self):
        self.temizle()
        self.nav_bar_ekle(geri_fonksiyonu=self.giris_ekranini_goster)

        Label(self.root, text="YÖNETİCİ KONSOLU", font=FONT_TITLE, bg=BG_MAIN, fg=ACCENT_COLOR).pack(pady=10)
        card = self.create_card()

        Label(card, text="YENİ PROGRAM EKLE", font=FONT_BOLD, bg=BG_CARD, fg="white").pack(pady=(0, 10))

        entries = {}
        labels = ["Program Adı", "Std. İçerik", "Prem. İçerik", "Min BMI", "Max BMI"]

        Label(card, text="Hedef Kitle", bg=BG_CARD, fg=PREMIUM_COLOR).pack(anchor="w")
        self.adm_goal = ttk.Combobox(
            card,
            values=["Genel", "Plaj Vücudu", "Yarışmacı (Hardcore)", "Atletik Performans", "Zayıf Görünüm"],
            font=FONT_BODY
        )
        self.adm_goal.current(0)
        self.adm_goal.pack(fill="x", pady=(0, 5))

        for lbl in labels:
            Label(card, text=lbl, bg=BG_CARD, fg=TEXT_SUB, font=("Segoe UI", 8)).pack(anchor="w")
            e = ModernEntry(card)
            e.pack(fill="x", pady=(0, 3))
            entries[lbl] = e

        def programlari_guncelle():
            con = sqlite3.connect("corefit_final.db")
            cur = con.cursor()
            cur.execute("SELECT id, program_name FROM programs")
            progs = cur.fetchall()
            con.close()

            liste = [f"{p[0]} - {p[1]}" for p in progs]
            self.combo_sil["values"] = liste
            if liste:
                self.combo_sil.current(0)

        def kaydet():
            try:
                con = sqlite3.connect("corefit_final.db")
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO programs (program_name, goal, content_std, content_prem, min_bmi, max_bmi) "
                    "VALUES (?,?,?,?,?,?)",
                    (
                        entries["Program Adı"].get(),
                        self.adm_goal.get(),
                        entries["Std. İçerik"].get(),
                        entries["Prem. İçerik"].get(),
                        float(entries["Min BMI"].get()),
                        float(entries["Max BMI"].get())
                    )
                )
                con.commit()
                con.close()
                messagebox.showinfo("Admin", "Program Eklendi")
                programlari_guncelle()
            except:
                messagebox.showerror("Hata", "Verileri kontrol et")

        ModernButton(card, text="EKLE", command=kaydet, bg_color=SUCCESS_COLOR).pack(pady=10, fill="x")

        Frame(card, height=1, bg=TEXT_SUB).pack(fill="x", pady=10)

        Label(card, text="PROGRAM SİL", font=FONT_BOLD, bg=BG_CARD, fg=DANGER_COLOR).pack(pady=(0, 5))

        self.combo_sil = ttk.Combobox(card, state="readonly", font=FONT_BODY)
        self.combo_sil.pack(fill="x", pady=5)

        def program_sil():
            secilen = self.combo_sil.get()
            if not secilen:
                return

            prog_id = secilen.split(" - ")[0]
            con = sqlite3.connect("corefit_final.db")
            cur = con.cursor()
            cur.execute("DELETE FROM programs WHERE id = ?", (prog_id,))
            con.commit()
            con.close()

            messagebox.showinfo("Admin", "Program Silindi!")
            programlari_guncelle()

        programlari_guncelle()
        ModernButton(card, text="SEÇİLİ PROGRAMI SİL", command=program_sil, bg_color=DANGER_COLOR).pack(pady=5, fill="x")


if __name__ == "__main__":
    root = Tk()

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "TCombobox",
        fieldbackground=BG_CARD, background=BG_MAIN, foreground="white",
        darkcolor=BG_MAIN, lightcolor=BG_MAIN, arrowcolor="white"
    )
    style.map("TCombobox", fieldbackground=[("readonly", BG_CARD)])
    style.map("TCombobox", selectbackground=[("readonly", BG_CARD)])
    style.map("TCombobox", selectforeground=[("readonly", "white")])

    root.option_add("*TCombobox*Listbox.background", BG_CARD)
    root.option_add("*TCombobox*Listbox.foreground", "white")
    root.option_add("*TCombobox*Listbox.selectBackground", ACCENT_COLOR)
    root.option_add("*TCombobox*Listbox.selectForeground", BG_MAIN)

    app = CoreFitApp(root)
    root.mainloop()
