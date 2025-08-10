import json
from ms_management_client.src.model.model import Costumer
from ms_management_client.src.infra.connection_postgresql import PostgreSQL

def register_new_client(event, context):
    """
    Function to register a new client from an SQS event.
    :param event: The event data from SQS.
    """
    
    db = PostgreSQL()
    try:
        session = db.get_session()
        for record in event["Records"]:
            body = json.loads(record["body"])
            obj = Costumer(
                name_costumer=body["name_costumer"],
                email=body["email"],
                phone=body["phone"]
            )
            session.add(obj)
        session.commit()
    except Exception as e:
        print(f"Erro ao registrar novo cliente: {e}")
    finally:
        session.close()
    return f"Cliente {body['name_costumer']} registrados com sucesso"