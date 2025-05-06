from database.DB_connect import DBConnect
from model.country import Country
from model.country import CountryDAO

class DAO():
    @staticmethod
    def getNodes(anno):
        try:
            conn = DBConnect.get_connection()
            result = []

            cursor = conn.cursor(dictionary=True)
            query = """ 
                         SELECT c.CCode, c.StateNme 
                         FROM country c, contiguity c2 
                         WHERE c2.`year` <= COALESCE(%s, c2.`year`) 
                         AND (c.CCode = c2.state1no OR c.CCode = c2.state2no)    
                     """

            cursor.execute(query, (anno,))

            for row in cursor:
                result.append(Country(row["CCode"], row["StateNme"]))


            cursor.close()
            conn.close()
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @staticmethod
    def getConnections(anno):
        try:
            conn = DBConnect.get_connection()
            result = []

            cursor = conn.cursor(dictionary=True)
            query = """ 
                         SELECT c.state1no, c.state2no 
                         FROM contiguity c 
                         WHERE c.conttype = 1 
                         AND c.`year` <= COALESCE(%s, c.`year`)    
                     """

            cursor.execute(query, (anno,))

            for row in cursor:
                result.append((row["state1no"], row["state2no"]))

            cursor.close()
            conn.close()
            return result

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

if __name__ == "__main__":
    dao = DAO()
    connections = dao.getConnections(950)
    print(connections)
