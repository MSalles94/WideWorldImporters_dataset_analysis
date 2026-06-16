def app():
    print('------------------------------')
    from pandas import DataFrame
    print(DataFrame({"Test":[1,2,3],
                     "steps":['docker','uv','python']}))
    print('------------------------------')
    print('Good Job!!!!')
    print('------------------------------')

if __name__=="__main__":
    app()