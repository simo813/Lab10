from database.DB_connect import DBConnect
from model.country import Country
from model.country import CountryDAO
import logging

class DAO:

    def __init__(self):
        self.countryDAO = CountryDAO()


    def getNodes(self, anno):
        try:
            conn = DBConnect.get_connection()
            result = []

            with conn.cursor(dictionary=True) as cursor:
                query = """ 
                             SELECT c.CCode, c.StateNme 
                             FROM country c, contiguity c2 
                             WHERE c2.`year` <= COALESCE(%s, c2.`year`) 
                             AND (c.CCode = c2.state1no OR c.CCode = c2.state2no)    
                         """
                cursor.execute(query, (anno,))

                for row in cursor:
                    country = Country(int(row["CCode"]), str(row["StateNme"]))
                    result.append(country)
                    self.countryDAO.add(country)

            conn.close()
            return result
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return []


    def getConnections(self, anno):
        try:
            conn = DBConnect.get_connection()
            result = []

            with conn.cursor(dictionary=True) as cursor:
                query = """ 
                             SELECT c.state1no, c.state2no 
                             FROM contiguity c 
                             WHERE c.conttype = 1 
                             AND c.`year` <= COALESCE(%s, c.`year`)    
                         """
                cursor.execute(query, (anno,))

                for row in cursor:
                    country1 = self.countryDAO.get_country_by_code(int(row["state1no"]))
                    country2 = self.countryDAO.get_country_by_code(int(row["state2no"]))
                    if country1 and country2:
                        result.append((country1, country2))
                    else:
                        logging.warning(f"Country code not found: {row['state1no']} or {row['state2no']}")

            conn.close()
            return result
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return []

if __name__ == "__main__":
    dao = DAO()
    connections = dao.getConnections(950)
    print(connections)
