import pandas as pd 
from googlesearch import search 
from newspaper import Article 
import requests
import json

def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm) 

def csv_to_df(csv_file_path):
    df = pd.read_csv(csv_file_path) 
    return(df)

def get_url(question ,acurracy) :
    url_list = []
    for j in search(question, tld="co.in", num= acurracy,start= 1, stop=acurracy, pause=3): 
        print(j)
        url_list.append(j)
    return(url_list)

def scrap_url_text(url) :
    try :    
        toi_article = Article(url, language="en")
        toi_article.download() 
        toi_article.parse() 
        return (toi_article.text) 
    except :
        return("not found")

def get_ans(article , question) :
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://demo.deeppavlov.ai',
        'Connection': 'keep-alive',
        'Referer': 'https://demo.deeppavlov.ai/',
        'TE': 'Trailers',
    }

    #data = '{"context_raw":["capital of india is delhi"],"question_raw":["what is capital of india ?"]}'
    data = {"context_raw":[article],"question_raw":[question]}
    data = json.dumps(data)

    response = requests.post('https://7008.lnsigo.mipt.ru/model', headers=headers, data=data)
    ans = (json.loads(response.text))
    return(ans[0][0])



df = csv_to_df("ip1.csv")
acurracy = int(input(" Enter Acurracy in range  1 -10 : "))
Coulmn_list =list(df.columns.values)
Row_list = list((df[(Coulmn_list[0])]))
df.set_index(Coulmn_list[0], inplace = True) 
#print(Coulmn_list[1:])
#print(Row_list)
for col in Coulmn_list[1:] :
    for row in Row_list :
        question = (str(col+ " " + row)) #genrate Question
        print(question)
        url_list = get_url(question , acurracy)#get url list fron Question
        #print(url_list)
        probale_ans_list = []
        for url in url_list :
            print(question,"-getting data from url -",url)
            try :    
                text = scrap_url_text(url)
                ans =get_ans(article= text,question=question)
                if len(ans) > 0 :
                    probale_ans_list.append(ans)
            except :
                print("error")
        print(question,"- candidates ans :" , probale_ans_list)
        cell_value = most_frequent(probale_ans_list)
        print("chosen ans : " , cell_value)
        probale_ans_list.clear()
        #print(question ,"--" ,ans)
        #probale_ans_list.append(ans)
        #print(question)
        #print(probale_ans_list)
        #print(df.at[row,col])
        df.loc[row,col] = cell_value
df.to_csv("output.csv")
