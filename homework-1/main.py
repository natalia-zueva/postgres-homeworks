"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='9uJICBlNaJPJizw8lCGU')
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(file)
                for row in reader:
                    customer_id = row[0]
                    company_name = row[1]
                    contact_name = row[2]
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (customer_id, company_name, contact_name))

    with conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(file)
                for row in reader:
                    employee_id = int(row[0])
                    first_name = row[1]
                    last_name = row[2]
                    title = row[3]
                    birth_date = row[4]
                    notes = row[5]
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                (employee_id, first_name, last_name, title, birth_date, notes))

    with conn:
        with conn.cursor() as cur:
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(file)
                for row in reader:
                    order_id = row[0]
                    customer_id = row[1]
                    employee_id = row[2]
                    order_date = row[3]
                    ship_city = row[4]
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (order_id, customer_id, employee_id, order_date, ship_city))

finally:
    conn.close()