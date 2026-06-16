def app():
    with open("./output/arquivo.txt", "w") as f:
        f.write("Olá mundo!")
    print('txt saved')
    print('------------------------------')
    from pandas import DataFrame
    df_teste=DataFrame({"Test":[1,2,3],
                     "steps":['docker','uv','python']})
    df_teste.to_csv('./output/teste_file.csv',sep=';')
    print('dataframe saved')
    print(df_teste)
    print('------------------------------')
    print('Good Job!!!!')
    print('------------------------------')

if __name__=="__main__":
    app()