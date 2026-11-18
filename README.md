# cafeteria_menu – Hito 3 (TI3041)

## Puesta en marcha
1. Crear esquema en MySQL Workbench:
   `CREATE DATABASE cafeteria_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
2. `python -m venv .venv`, activarlo y `pip install -r requirements.txt`
3. Editar `DATABASES` en `config/settings.py` (usuario/clave).
4. `python manage.py makemigrations menu`
5. `python manage.py migrate`
6. `python manage.py createsuperuser`
7. `python manage.py loaddata datos_iniciales` (4 categorías + 12 productos)
8. `python manage.py runserver`

## Consultas de verificación (Workbench)
```sql
SELECT COUNT(*) AS total_padres FROM menu_categoria;
SELECT COUNT(*) AS total_hijos FROM menu_producto;
SELECT h.id, h.nombre, p.nombre AS clasificacion
FROM menu_producto h INNER JOIN menu_categoria p ON h.categoria_id = p.id;
```
