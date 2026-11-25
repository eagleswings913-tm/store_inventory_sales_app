import sqlite3

class Product:
    def __init__(self,product_fields):
        self.id = ""
        self.barcode = product_fields.get("barcode")
        self.brand_name = product_fields.get("brand_name")
        self.category = product_fields.get("category")
        self.color = product_fields.get("color")
        self.color_num = product_fields.get("color_num")
        self.discount = product_fields.get("discount")
        self.fiber_type = product_fields.get("fiber_type")
        self.item_num = product_fields.get("item_num")
        self.product_id = product_fields.get("product_id")
        self.product_name = product_fields.get("product_name")
        self.sold_by = product_fields.get("sold_by")
        self.taxable = product_fields.get("taxable")
        self.type = product_fields.get("type")
        self.unit = product_fields.get("unit")
        self.weight_per_unit = product_fields.get("weight_per_unit")
        self.yarn_line = product_fields.get("yarn_line")
        self.yarn_size = product_fields.get("yarn_size")
        self.discontinued = 'False'
        self.in_inventory = 'False'

    def add_product(self, product):
        pass

    def read_product(self, product):
        pass

    def update_product(self, product):
        pass

    def delete_product(self, product):
        pass

    @classmethod
    def init_db(cls, db_path: str = "aplacetoweave.db"):
        """Create the products table if it doesn't exist."""
        with sqlite3.connect(db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    barcode TEXT NOT NULL,
                    brand_name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    color TEXT NOT NULL,
                    color_num TEXT NOT NULL,
                    discount BOOLEAN NOT NULL,
                    fiber_type TEXT NOT NULL,
                    item_num TEXT NOT NULL,
                    product_id TEXT NOT NULL,
                    product_name TEXT NOT NULL,
                    sold_by TEXT NOT NULL,
                    taxable BOOLEAN NOT NULL,
                    type TEXT NOT NULL,
                    unit TEXT NOT NULL,
                    weight_per_unit TEXT NOT NULL,
                    yarn_line TEXT NOT NULL,
                    yarn_size TEXT NOT NULL,
                    discontinued BOOLEAN NOT NULL,
                    in_inventory BOOLEAN NOT NULL
                )
            """
            )

    def save(self, db_path: str = "aplacetoweave.db"):
        """Write (Insert or Update) the product to the database."""
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                    "INSERT INTO products (barcode,brand_name,category,color,color_num,discount,fiber_type,item_num,product_id,product_name,sold_by,taxable,type,unit,weight_per_unit,yarn_line,yarn_size,discontinued,in_inventory) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (self.barcode, self.brand_name, self.category, self.color, self.color_num, self.discount, self.fiber_type, self.item_num, self.product_id, self.product_name,self.sold_by,self.taxable,self.type,self.unit,self.weight_per_unit,self.yarn_line,self.yarn_size,self.discontinued,self.in_inventory)
                )
            self.id = cursor.lastrowid
            conn.commit()

    def update(self,db_path: str = "aplacetoweave.db"):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                    "UPDATE products SET barcode=?,brand_name=?,category=?,color=?,color_num=?,discount=?,fiber_type=?,item_num=?,product_id=?,product_name=?,sold_by=?,taxable=?,type=?,unit=?,weight_per_unit=?,yarn_line=?,yarn_size=?,discontinued=?,in_inventory=? WHERE id=?",
                    (self.barcode, self.brand_name, self.category, self.color, self.color_num, self.discount, self.fiber_type, self.item_num, self.product_id, self.product_name,self.sold_by,self.taxable,self.type,self.unit,self.weight_per_unit,self.yarn_line,self.yarn_size,self.discontinued,self.in_inventory,self.id)
                )
            conn.commit()

    @classmethod
    def search_product(cls, barcode, db_path: str = "aplacetoweave.db"):
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT id, product_id FROM products WHERE barcode LIKE ?"
            cursor.execute(query, (f"%{barcode}%",))
            results = cursor.fetchall()
            return results

    @classmethod
    def get_by_id(cls, product_id: int, db_path: str = "aplacetoweave.db"):
        """Read a single product by ID."""
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id,barcode,brand_name,category,color,color_num,discount,fiber_type,item_num,product_id,product_name,sold_by,taxable,type,unit,weight_per_unit,yarn_line,yarn_size,discontinued,in_inventory FROM products WHERE id = ?", (product_id,))
            row = cursor.fetchone()
            if row:
                return cls(row)
        return None

    @classmethod
    def get_all(cls, db_path: str = "aplacetoweave.db"):
        """Read all products from the database."""
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id,barcode,brand_name,category,color,color_num,discount,fiber_type,item_num,product_id,product_name,sold_by,taxable,type,unit,weight_per_unit,yarn_line,yarn_size,discontinued,in_inventory FROM products")
            rows = cursor.fetchall()
            return [cls(r) for r in rows]

    @staticmethod
    def delete(product_id, db_path: str = "aplacetoweve.db"):
        """Delete the product from the database."""
        if id is not None:
            with sqlite3.connect(db_path) as conn:
                conn.execute("DELETE FROM products WHERE id = ?", (product_id,))
                conn.commit()
            return True
        return False