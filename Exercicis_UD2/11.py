import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='operacions.log',
    filemode='w'
)


def suma(a, b):
    result = a + b
    logging.info(f"Suma: {a} + {b} = {result}")
    return result

def resta(a, b):
    result = a - b
    logging.info(f"Resta: {a} - {b} = {result}")
    return result

def multiplicacio(a, b):
    result = a * b
    logging.info(f"Multiplicació: {a} * {b} = {result}")
    return result

def divisio(a, b):
    try:
        result = a / b
        logging.info(f"Divisió: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        logging.error(f"Error en divisió: No es pot dividir per zero ({e})")
        return None



def main():
    try:
        num1 = float(input("Introdueix el primer número: "))
        num2 = float(input("Introdueix el segon número: "))
        
        result_suma = suma(num1, num2)
        result_resta = resta(num1, num2)
        result_multiplicacio = multiplicacio(num1, num2)
        result_divisio = divisio(num1, num2)

        print(f"Suma: {result_suma}")
        print(f"Resta: {result_resta}")
        print(f"Multiplicació: {result_multiplicacio}")
        if result_divisio is not None:
            print(f"Divisió: {result_divisio}")
        else:
            print("No es va poder realitzar la divisió.")

    except ValueError as e:
        logging.error(f"Error d'entrada: {e}")
        print("Error: Cal introduir nombres vàlids.")

    finally:
        print("Operacions finalitzades. Consulta 'operacions.log' per veure els registres.")

if __name__ == "__main__":
    main()