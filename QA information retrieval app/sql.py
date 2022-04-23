import db_connection as db

connection= db.connect()

def get_subject(relation, objectt):
    sql_select_Query = "SELECT Distinct Subject FROM knowledge WHERE Relation = %s and Object = %s; "
    cursor = connection.cursor()
    cursor.execute(sql_select_Query, (relation, objectt))
    # get all records
    records = cursor.fetchall()
    return records[0][0]
    
def get_object(subject, relation):
    sql_select_Query = "SELECT Distinct Object FROM knowledge WHERE Subject = %s and Relation = %s; "
    cursor = connection.cursor()
    cursor.execute(sql_select_Query, (subject, relation))
    # get all records
    records = cursor.fetchall()
    return records[0][0]
    
def get_relation(subject, objectt):
    sql_select_Query = "SELECT Distinct Relation FROM knowledge WHERE Subject = %s and Object = %s; "
    cursor = connection.cursor()
    cursor.execute(sql_select_Query, (subject, objectt))
    # get all records
    records = cursor.fetchall()
    return records[0][0]

def get_answer(query_list):
    for index, param in enumerate(query_list):
        if param == 'null':
            if index == 0:
                return get_subject(query_list[1],query_list[2])
            elif index == 1:
                return get_relation(query_list[0],query_list[2])
            else:
                return get_object(query_list[0],query_list[1])
      
def get_subject2(objectt):
    sql_select_Query = f"SELECT Distinct Subject FROM knowledge WHERE Object = '{objectt}';"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    return records[0][0]
    
def get_object2(subject):
    sql_select_Query = f"SELECT Distinct Object FROM knowledge WHERE Subject = '{subject}';"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    return records[0][0]
    
def get_answer2(query_list):
    for index, param in enumerate(query_list):
        if param != 'null':
            if index == 0:
                print(get_object2(param))
            elif index == 2:
                print(get_subject2(param))
            else:
                print(get_subject2(param))