import pandas as pd

def json(self):

    list_of_tuples = list(zip(self.raw_localidade, self.raw_faixa_cep))

    print(list_of_tuples)

    df = pd.DataFrame(list_of_tuples, columns=['Localidade', 'Faixa de CEP'])

    # creating a Json Line file
    df.to_json('JsonResult.json', orient='records', lines=True)
