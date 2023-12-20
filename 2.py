import streamlit as st
import random

# Menentukan pertanyaan dan jawaban untuk setiap level
pertanyaan = {
    'beginner': [
        {"Soal nomor 1": "Aldi, Sesil, Aji, Anum, Farhan dan Amar mengikuti ujian statistika dengan rata-rata nilai ujian mereka adalah 85. Pada ujian tersebut Aldi mendapatkan nilai 80, Sesil mendapatkan nilai 70, Aji mendaptkan nilai 90, Anum mendapatkan nilai 85, dan Amar mendapatkan nilai 90, dan Farhan akan mendapatkan nilai", 
         "pilihan": ["A. 90 ", "B. 95", "C. 85", "D. 100"], "jawaban": "B. 95"},
        {"Soal nomor 2": "Nilai rata-rata ulangan matematika dari 4 orang siswa adalah 7,5 dengan selisih nilai tertinggi dan terendah adalah 2, jika ada 1 siswa yang mendapat nilai tertingi dan 3 siswa lainnya mendapatkan nilai yang sama , nilai tertinggi tersebut adalah?", 
         "pilihan": ["A. 10", "B. 9", "C. 8 ", "D. 11"], "jawaban": "B. 9"},
        {"Soal nomor 3": "Diberikan sebuah data berurutan a,a+1,a+1,7,b,b,9 dari terkecil hingga yang terbesar dan memiliki rata-rata 7 berapakah nilai dari 3a+2b??", 
         "pilihan": ["A. 34", "B. 35", "C. 30 ", "D. 31"], "jawaban": "d. 31"},
        {"Soal nomor 4": "Nilai rata-rata ulangan  matematika suatu kelas adalah 6,8 jika dua siswa yang memiliki nilai 4 dan 6 diabaikan, maka rata-rata kelas tersebut naik menjadi 6,9. Banyaknya siswa mula-mula adalah?",
          "pilihan": ["A. 38", "B. 40", "C. 37 ", "D. 41"], "jawaban": "A. 38"},
        {"Soal nomor 5": "Rata-rata bilangan adalah 40. Ada bilangan yang sebenarnya 60, tetapi terbaca 30. Setelah dihitung ulang, rata-rata yang sebenarnya adalah 41. Banyak bilangan dalam kelompok itu adalah", 
         "pilihan": ["A. 29 ", "B. 27", "C. 32", "D. 30"], "jawaban": "D.30"},
        {"Soal nomor 6": "Nilai rata-rata tes matematika dari 10 siswa adalah 55 dan jika digabung lagi dengan 5 siswa nilai rata-rata menjadi 53. Nilai rata-rata dari 5 siswa tersebut adalah?", "pilihan": ["A. 48", "B. 49", "C. 52 ", "D. 45"], "jawaban": "B. 49"},
        {"Soal nomor 7": "Suatu data dengan rata-rata 16 dan jangkauan 6. jika setiap nilai dalam dat dikalikan p kemudian dikurangi q di dapat data baru dengan rata-rata 20 dan jangkauan 9. Nilai dari 2p + q?", 
         "pilihan": ["A. 7", "B. 9", "C. 11 ", "D. 8"], "jawaban": "A. 7"},
        {"Soal nomor 8": "Pada ulangan matematika, diketahui nilai rata-rata kelas 58. Jika rata-rata nilai matematika untuk siswa prianya adalah 65 sedang untuk siswa wanita rata-ratanya 54, maka perbandingan jumlah siswa pria dan wanita pada kelas itu adalah",
          "pilihan": ["A. 4:8", "B. 5:7", "C. 4:7 ", "D. 7:6"], "jawaban": "C. 4:7"},
        # Tambahkan pertanyaan-pertanyaan beginner lainnya
    ],
    'intermediate': [
        {"Soal nomor 1": " Perhatikan data berikut!5,5,7,3,7,8, median data tersebut adalah", 
         "pilihan": ["A. 7 ", "B. 6", "C. 6.5", "D. 5.5"], "jawaban": "C. 6"},
        {"Soal nomor 2": "Pemusatan data yang membagi suatu data menjadi setengah data terkecil dan terbesar dikenal dengan istilah", 
         "pilihan": ["A. Variansi", "B. Median", "C. Mean ", "D. Modus"], "jawaban": "B. Median"},
        {"Soal nomor 3": "Data yang paling banyak muncul dalam suatu kumpulan data adalah", 
         "pilihan": ["A. Variansi", "B. Median ", "C. Mean", "D. Modus"], "jawaban": "D. Modus"},
        {"Soal nomor 4": "Rata-Rata dari kuadrat deviasi antara setiap titik data dan rata-rata keseluruhan data adalah?", 
         "pilihan": ["A. Variansi", "B. Median", "C. Mean ", "D. Modus"], "jawaban": "A. variansi"},
        {"Soal nomor 5": "Nilai rata-rata yang didapatkan dengan membagi jumlah data dengan banyaknya data adalah", 
         "pilihan": ["A. Variansi", "B. Median", "C. Mean ", "D. Modus"], "jawaban": "C. Mean"},
        {"Soal nomor 6": "Ragam dari data 7, 4, 3, 6 adalah",
          "pilihan": ["A. 2", "B. 4", "C. 2.5 ", "D. 3"], "jawaban": "C. 2.5"},
        {"Soal nomor 7": " Simpangan rata-rata dari data 4, 5, 6 adalah",
          "pilihan": ["A. 2", "B. 4", "C. 2.5 ", "D. 3"], "jawaban": "B. 2"},
        {"Soal nomor 8": "Sebuah data tersebar sebagai berikut12   9      	6      	8      	15    	11    	1011   19    	12    	12    	14    	14    	15Modus dari data tersebut adalah..", 
         "pilihan": ["A. 12", "B. 14", "C. 11 ", "D. 11"], "jawaban": "C. 11"},
        # Pertanyaan-pertanyaan intermediate
    ],
    'expert': [
        {"Soal nomor 1": "  Data x1 , x2 , x3 , ..., xn   memiliki mean 8. Mean dari x1 + 5, x2  + 5, x3  +5, ... , xn + 5adalah", 
         "pilihan": ["A. 12 ", "B. 10", "C. 14", "D. 13"], "jawaban": "D. 13"},
        {"Soal nomor 2": " Data x1 , x2 , x3 , ..., xn   memiliki mean 5. Mean dari x1 + 8, x2  + 8, x3  +8, ... , xn + 8adalah",
          "pilihan": ["A. 12 ", "B. 10", "C. 14", "D. 13"], "jawaban": "D. 13"},
        {"Soal nomor 3": " Data x1 , x2 , x3 , ..., xn   memiliki mean 12. Mean dari x1 + 3, x2  + 3, x3  +3, ... , xn + 3adalah", 
         "pilihan": ["A. 15", "B. 14 ", "C. 17", "D. 12"], "jawaban": "D. 15"},
        {"Soal nomor 4": "Berikut merupakan data produksi (dalam ribuan) di sebuah perusahaan mainan anak-anak 2 minggu:8	9      	9      	9      	10    	10    	10  11  12    	12    	13    	14    	14    	15 , Tentukan nilai jangkauan inter-kuartil dari datadi atas",
          "pilihan": ["A. 5", "B. 2", "C. 4", "D. 6"], "jawaban": "C. 4"},
        {"Soal nomor 5": "  Tentukan jangkauan dari data berikut: 12  	9  	6      	3      	8      	9      	15    	14    	13    	4      	5",
          "pilihan": ["A. 10", "B. 12", "C. 15 ", "D. 14"], "jawaban": "B. 12"},
        {"Soal nomor 6": "Dari data: 3, 4, 5, 5, 6, 6, 6. Tentukan mean, median dan modusnya berturut-turut", 
         "pilihan": ["A. 5:6:7", "B. 5.5:6:7", "C. 6:6.5:7 ", "D. 5:5:6"], "jawaban": "D. 5:5:6"},
        
        # Pertanyaan-pertanyaan expert
    ]
}
def  hitung_nilai(jawaban_user , jawaban):
    return 12.5 if jawaban_user.lower() == jawaban.lower() else 0
st.session_state.level = None

def main():
    st.title("QuizTest")
    st.subheader("Halo, Selamat Datang Di QuizTest :wave:")
    st.write("---")
    st.write(
    "Pada kali ini kami akan membantu kamu untuk mengetahui tingkat kehebatanmu dalam mengerjakan ilmu statistika. Sebelum mengerjakan test, kami akan memberikan pilihan level yang akan kamu kerjakan. Terdiri atas BEGINNER, INTERMDIATE, dan EXPERT"
    )
    st.write("Selamat Mengerjakan --> Tekan Tombol 'Mulai Quiz'")
    if 'jawan_user' not in st.session_state:
        st.session_state.jawaban_user = {}


    # Menambahkan pilihan level
    level_options = ['beginner', 'intermediate', 'expert']
    #st.sidebar.selectbox("Pilih Level", level_options, key="level")
  
    if 'mulai' not in st.session_state:
        st.session_state.mulai = False

    if st.sidebar.button("Mulai Quiz"):
        st.session_state.mulai =True

    if st.session_state.mulai:
        st.session_state.level = st.sidebar.selectbox("Pilih Level", level_options)
        st.write(st.session_state.level)
        st.subheader(f"Level: {st.session_state.level.capitalize()}")

        total_nilai = 0

        # Mendapatkan pertanyaan sesuai dengan level yang dipilih
        pertanyaan_level = pertanyaan.get(st.session_state.level, [])
        #random.shuffle(pertanyaan_level)  # Acak urutan pertanyaan
       
        # Menampilkan pertanyaan dan pilihan jawaban menggunakan radio button
        for i, pertanyaan_data in enumerate(pertanyaan_level[:8]):
            # Menampilkan pertanyaan dan hilangkan 'pilihan' kebelakang
            # get key 1 dari dictionary
  
            st.write(f"{i + 1}. {list(pertanyaan_data.values())[0]}")
            st.session_state.jawaban_user[f"jawaban_{i}"] = st.radio("Pilih Jawaban:", pertanyaan_data["pilihan"], key=f"jawaban_{i}")




        # Menampilkan tombol untuk menghitung nilai
        if st.button("Hitung Nilai"):
            for i, pertanyaan_data in enumerate(pertanyaan_level[:8]):
                total_nilai += hitung_nilai(st.session_state.jawaban_user[f"jawaban_{i}"], pertanyaan_data["jawaban"])

            st.session_state.total_nilai = total_nilai
            st.session_state.mulai = False
            
            persentase_nilai = total_nilai 

            st.subheader("Hasil Kuis:")
    
            st.write(f"Persentase Nilai: {persentase_nilai}%")

            if persentase_nilai >= 80:
                st.success("Selamat! Anda lulus dengan baik.")
            else:
                st.warning("Anda perlu memperbaiki beberapa jawaban untuk lulus.")

        # Menambahkan fitur kepuasan konsumen
        st.subheader("Kepuasan Konsumen:")
        kepuasan_options = ["Puas", "Cukup Puas", "Tidak Puas"]
        kepuasan = st.selectbox("Pilih tingkat kepuasan konsumen:", kepuasan_options)
        st.write(f"Kepuasan Konsumen: {kepuasan}")

        # Menambahkan tombol selesai
        if st.button("Selesai"):
            st.balloons()  # Menampilkan balon sebagai efek selesai
            st.success("Terima kasih telah mengikuti kuis!")

if __name__ == "__main__":
    main()