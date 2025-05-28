from __init__ import CONN,CURSOR

class House:
    def __init__(self,location,estate_id,owner=None,id=None):
        self.location=location
        self.estate_id=estate_id
        self.owner=owner
        self.id=id

    def save(self):
        sql="""INSERT INTO houses(location,estate_id,owner) VALUES (?,?,?)"""
        CURSOR.execute(sql,(self.location,self.estate_id,self.owner))
        CONN.commit()
        self.id=CURSOR.lastrowid

    @classmethod
    def add_house(cls,location,estate_id):
        house=cls(location,estate_id)
        house.save()

    @classmethod
    def see_available_houses(cls):
        sql="""SELECT * FROM houses WHERE owner=none"""
        rows=CURSOR.execute(sql)
        return [row[1] for row in rows]
    


# House.add_house("Ngong lane",1)
print()