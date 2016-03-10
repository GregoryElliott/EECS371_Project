Greg Elliott, Greg Crow, Corey Grief
### Set Up
```sh
To get started using our system, follow these steps:
1. Clone our code from the following github repo: https://github.com/GregoryElliott/EECS371_Project. 
3. Due to the size of the 2015 corpus, we have commented the line of code that generates the graph for it; in order to view the graph for it, add the ‘gg2015.json’ file to the clone repo locally (this file is included in a zip in our canvas submission) and uncomment line 774 in gg_api.py (it says #g2015 = generate_graph("2015")))
3. Install the required dependencies:
-pip install rdflib
-pip install requests
-pip install bs4
4. Install nltk for python (http://www.nltk.org/install.html) 
-Open a python terminal and type the follow commands:
--import nltk
--nltk.download()
--in the separate window that opens up, select ‘all’ and click download
5. Run the main function in the gg_api.py python file (running it the first time will be very slow, around 5 minutes for 2013 and 20-30 minutes if the 2015 corpus is included; it will run much faster subsequently as we save the results of our twitter parsing locally)
6. Doing so will open the text interface (described below) 
```
```sh
Using our text interface is explained as follows:
1. Type ‘help’ to see all available commands (appendix A)
2. Type ‘hosts 2013’ to see the hosts for the 2013 golden globes (appendix B)
3. Type ‘awards 2013’ to see the awards for the 2013 golden globes (appendix C)
4. Type ‘visualize 2013’ to see the facts populating our ontology in the 2013 graph (appendix D)
5. Type ‘nominees 2013’ to see all the nominees mapped to their corresponding awards in the 2013 golden globes (appendix E)
6. Type ‘nominees 2013 best director’ to see all the nominees for best director in the 2013 golden globes (you can replace ‘best director’ with another award such as ‘best actor drama’ and you can be liberal in your naming of the award as we map what you type to the actual award name using regular expressions) (appendix F)
-The full syntax for commands is as follows [type] [year] [optional:award query string] where [type] can be visualize, hosts, awards, winners, nominees, or presenters and the optional argument is only for winners, nominees, and presenters
* note that ‘2013’ can be replaced by ‘2015’ below to view the data for 2015 and ‘nominees’ can be replaced by ‘winners’ or ‘presenters’ to view the winners or presenters instead of nominees
```

# EECS371_Project
