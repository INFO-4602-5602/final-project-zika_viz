## Visualization Panel for Zika Tweets Exploration 
Final Project - INFO 5602

Collaborators:

	Linzi Xing
	Hayeong Song

## File Structure
* data:
	* collect_zika.json: raw zika related tweets
	* sentimet.csv: contains tweets' sentiment coordination and score, output of sentiment analysis code
	* time_series.csv: contains two columns: collected time and content of tweets
	* topic.csv: contains two columns: tweet index and number of topic tweet belongs to, output of topic model code
	* tst.csv: all views above are integrated into this csv file and this is used as direct input of visualization code
* static: some source files and documentations
* csv_generate.py: py code used to generate the final csv file
* topic.model.py: py code used to get most possible topic of each tweets, the output is topic.csv
* collect.py: collecte twitter data
* cofig.py: should edit to run collect.py 
* build_model.py: build mode for word2vec and pca and save it in pkl form
* tokenizer.py: tokenize the input of tweet
* new_test: compute sentiment score, and convert tweet into 2 coordinates using PCA
* tst.csv: the integrated data file used as input of visualization code

## Run the Code

collect.py

To run this code, first edit config.py with your configuration, then:

mkdir data python collect.py -q zika -d data

It will produce the list of tweets for the query "zika" in the file data/collect_zika.json

For visualization:
go to the directory where the code in loacated, in this case tst.hml
python httpserver:$ python -m SimpleHTTPServer 8080

goto
http://127.0.0.1:8080

and click on tst.html and will see the visualization


## Dependency

codes can be run on both python version 2.x or 3.x, in case of tokenizer.py is python 2.x should be used.

Numpy
$pip install numpy

Tweepy
$pip install tweepy

Gensim: 
$pip install gensim

Textblob:
$ pip install -U textblob
$ python -m textblob.download_corpora python -m textblob.download_corpora

Pattern:
$ pip install pattern

Sklearn:
$ pip install -U scikit-learn

NLTK:
$ sudo pip install -U nltk



## References
* For the bootstrap page:
[Bootstrap CSS](http://getbootstrap.com/css/)
[Bootstrap Components](http://getbootstrap.com/components/)
[Bootstrap Javascript](http://getbootstrap.com/javascript/)

* Visualization part:
	* [dc.js heatmap example](https://github.com/dc-js/dc.js/blob/master/web/examples/heat.html)

	* [dc.js row chart example](https://github.com/dc-js/dc.js/blob/master/web/examples/row.html)

	* [dc.js datatable example](https://github.com/dc-js/dc.js/blob/master/web/examples/table-on-aggregated-data.html)

	* [dc.js line chart time series](http://www.d3noob.org/2013/08/add-line-chart-in-dcjs.html)

* Pre-processing part:
	* [topic modeling](https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/)
	
	* [sentiment analysis](https://github.com/jdwittenauer/twitter-viz-demo)
	
	* [tokenizer](http://sentiment.christopherpotts.net/code-data/happyfuntokenizing.py)
	
* Data collecting:
	* [Twitter Streaming APIs](https://dev.twitter.com/streaming/overview)
	* [Twitter Stream Downloader](https://gist.github.com/bonzanini/af0463b927433c73784d)

