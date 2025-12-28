class Student:
    def __init__(self, sid, name, gpa=0.0):
        self.sid = sid          # public
        self.name = name        # public
        self._credits = 0       # protected (convention)
        self.__gpa = gpa        # private (name mangling)

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, value):
        if not (0.0 <= value <= 4.0):
            raise ValueError("GPA harus antara 0.0 dan 4.0")
        self.__gpa = round(value, 2)

    def add_credits(self, n):
        if n < 0:
            raise ValueError("credits tidak boleh negatif")
        self._credits += n

    def classify(self):
        if self.__gpa >= 3.5:
            return "Cum Laude"
        elif self.__gpa >= 2.5:
            return "Good"
        else:
            return "Remedial"

if __name__ == "__main__":
    # Membuat objek siswa
    s = Student("S100", "Ana", 3.1)
    
    # Mengakses public attribute
    print(f"Nama: {s.name}")
    
    # Mengakses private attribute melalui getter
    print(f"GPA Awal: {s.get_gpa()}")
    
    # Mengubah private attribute melalui setter
    s.set_gpa(3.75)
    print(f"GPA Baru: {s.get_gpa()}")
    print(f"Klasifikasi: {s.classify()}")
    
    # Menambah credit (memanipulasi protected attribute)
    s.add_credits(3)
    print(f"Total Credits: {s._credits}")