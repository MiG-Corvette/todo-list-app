import psycopg2

# データベース接続情報
db_name = "todo_list_db"
db_user = "postgres"
db_password = "Postgres2024!"
db_host = "localhost"
db_port = "5432"

# データベースに接続
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# カーソルを作成
cur = conn.cursor()

# テーブル一覧を取得
cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")

# 結果を取得して表示
tables = cur.fetchall()
for table in tables:
    print(table)

# 接続を閉じる
cur.close()
conn.close()
