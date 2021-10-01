# task_1
<h2> Mission Requirements </h2>

This Scrapy script should write to the output Category. Website name. Website URL. Extract the website title tag content if possible."
Could you prepare the .csv with following columns:
"Category", "Website_name", "Website_URL", "Website_title",
where the Website_title is a content from the <title></title> tag from the external (related to the catalogue parsed) website
Using http://dmoztools.net.


<h2> Use cmd and python code to implement the function.</h2>
<b> Working environment: Anaconda-Jupyter </b>
First open cmd. to create the scrapy project

<img src="https://github.com/Alecia113/task_1/blob/main/start.png" width="500px"/>

cd DmoTest
scrapy genspider www.dmoztools.net/
