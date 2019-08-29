# All That's *Fit* To Print()
Get and generate article titles based on work published in the New York Times.

# Usage
The purpose of this tool is to generate novel (or semi-novel, at least) op-ed titles based on work published in the New York Times based on a particular search query - for example, you can generate article titles for particular authors and probably predict what future article titles will be.

To run the program, run 
```sh
python3 AllThatsFitToPrint.py
```
This script will prompt you for the value of your query. Note that this query should be an elasticsearch style query consistent with the requirements of the [NYT Search API](https://developer.nytimes.com/docs/articlesearch-product/1/overview). For example, should I want to predict what Ross Douthat's next piece will be, I would input "Ross+Douthat" (including the quotation marks). 

The text generation engine will then create a text file with all of the titles it could retrieve and then run for the specified number of epochs while printing new values to the console.

# Dependencies and Installation
This program requires an installation of [Python 3](https://www.python.org/downloads/).

It also uses json, requests, and textgenrnn, which can all be installed via [pip](https://pypi.org/project/pip/). 

Then, clone this repository to get the code:
```sh
git clone https://github.com/anushadatar/AllThatsFitToPrint.git
```
Additionally, you will need to populate the API_KEY field in nyt_search.py. You can generate your own key by registering your application with the New York Times [developer console](https://developer.nytimes.com/). You can then fill this value in as a string, and this should allow you to access data from the Times.
