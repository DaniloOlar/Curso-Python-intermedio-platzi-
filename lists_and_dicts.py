def run():
    lista =[1,2,3,4,5]
    dict = {"Nombre":"Ana", "Edad":30}
    superlist = [
        {"Nombre":"Ana", "Edad":30},
        {"Nombre":"Albert", "Edad":35}, 
        {"Nombre":"Abel", "Edad":20}
    ]

    super_dict = {
        "Naturales":[1,2,3,4],
        "Enteros": [-1,-2,0,1,2], 
        "Float":[1.3,2.05, 4.9, 4.0]}

    for key, value in super_dict.items():
        print(key,"-", value)

if __name__ == "__main__":  
    run()
