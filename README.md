# csv_data_collection
This is python tool which takes input a CSV file and finds answer for each cell. example if a csv file  columns are say x = [population of ,what is capital of] and row label are say y = [India, china, USA] then this tool will scrape the answer from internet and place it in particular cell x1y1 = 123crs , x2y1 = New delhi so on

### exmaple input :
|             | number of covid cases in  | , population of |   |   |
|-------------|---------------------------|-----------------|---|---|
| maharashtra |                           |                 |   |   |
| usa         |                           |                 |   |   |
| india       |                           |                 |   |   |
| china       |                           |                 |   |   |
| uk          |                           |                 |   |   |
| pakisthan   |                           |                 |   |   |

### example Output : with acurracy set to 3 ( accuracy can be set to 1 to 10 depending on time)
|             | number of covid cases in  | , population of                          |   |   |
|-------------|---------------------------|------------------------------------------|---|---|
| maharashtra | ,"6,57,450"               | ,"Total 40,959"                          |   |   |
| usa         | ,COVID-19                 | ,"13.9 births/1,000 population per year" |   |   |
| india       | ,"2,333,577"              | ,Population control                      |   |   |
| china       | ,France                   | ,"65,105,246"                            |   |   |
| uk          | ,"323                     | ,300 confirmed cases "                   |   |   |
| pakisthan   | ," 280,027"               | , 2132542                                |   |   |

