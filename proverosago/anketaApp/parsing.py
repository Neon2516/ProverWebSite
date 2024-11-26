import pandas as pd
import mysql.connector

# Настройки подключения к базе данных
db_config = {
    "host" : "127.0.0.1",
        "user": "root",
        "password": "11qaz!!QAZ",
    'database': 'mysite'
}


# Чтение CSV-файла в DataFrame
csv_file_path = 'C:/Users/Nikita/Desktop/base_demo.csv'  # Укажите путь к вашему CSV-файлу
df = pd.read_csv(csv_file_path, encoding='utf-8')  # Убедитесь, что кодировка правильная

# Обработка NaN
df.fillna(0, inplace=True)  # Заполнить NaN нулями, если это допустимо для вашего случая

# Преобразование столбца 'Год до' в целое число

# Подключение к MySQL
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Создание таблицы на основе структуры DataFrame
table_name = 'base'  # Задайте имя таблицы

# Генерация SQL-запроса для создания таблицы
create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
for column in df.columns:
    column_type = 'VARCHAR(255)'  # По умолчанию используем VARCHAR
    if df[column].dtype == 'int64':
        column_type = 'INT'
    elif df[column].dtype == 'float64':
        column_type = 'FLOAT'
    create_table_query += f"`{column}` {column_type}, "  # Обрамляем названия столбцов
create_table_query = create_table_query.rstrip(', ') + ")"

# Выполнение запроса на создание таблицы
cursor.execute(create_table_query)

# Вставка данных в таблицу
for index, row in df.iterrows():
    insert_query = f"INSERT INTO {table_name} (`{'`, `'.join(df.columns)}`) VALUES ({', '.join(['%s'] * len(row))})"
    cursor.execute(insert_query, tuple(row))

# Сохранение изменений и закрытие соединения
connection.commit()
cursor.close()
connection.close()

print("Данные успешно загружены в базу данных.")