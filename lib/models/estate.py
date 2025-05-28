from  __init__ import CONN,CURSOR

class Estate:
    def __init__(self,name,id=None):
       self.id=id
       self.name=name

    def save(self):
        sql="""INSERT INTO estates(name) VALUES(?)"""
        CURSOR.execute(sql,(self.name,))
        CONN.commit()
        self.id=CURSOR.lastrowid

    @classmethod
    def add_estate(cls,name):
        estate=cls(name)
        estate.save()

    @classmethod
    def remove_estate(cls,id):
        sql="""DELETE FROM estates WHERE id=?"""
        CURSOR.execute(sql,(id,))
        CONN.commit()

    @classmethod
    def clients_in_estate(cls,id):
        sql="""SELECT * FROM houses WHERE estate_id=?"""
        rows=CURSOR.execute(sql,(id,))
        return [row[2] for row in rows if not row[2]==None]
    
    @classmethod
    def show_my_estates(cls):
        sql="""SELECT * FROM estates """
        rows=CURSOR.execute(sql)
        return [row[1] for row in rows]


# Estate.add_estate("Lion park")
print(Estate.show_my_estates())

