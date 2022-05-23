def run():
    from primalidad import factores_primos

    dict ={i: factores_primos(i) for i in range(100)}
    print (dict)







if __name__ == "__main__":  
    run()