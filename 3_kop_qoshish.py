import sqlite3

ulanish = sqlite3.connect("dars8.db")

talabalar = [
  ("Dilnoza", 19, 92),
  ("Sardor", 21, 67),
  ("Malika", 20, 78),
]

for talaba in talabalar:
  ulanish.execute(
    "INSERT INTO talabalar (ism, yosh, ball) VALUES (?, ?, ?)",
    talaba
  )

ulanish.commit()
ulanish.close()
print(len(talabalar), "ta talaba qo'shildi")
