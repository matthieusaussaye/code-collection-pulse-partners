# code-collection-pulse-partners 1 - text-to-sql

This repo is at the destination of any IT teams, Data Science agency, Data Scientist Freelance aiming to unlock growth through LLMs use in the specific case of text-to-SQL

## Pulse Experiments

### Initialisation :

*1. Initialize ```experiment.json``` with the different experiments you want to try - the key names.*

*1. Initialize ```init_sql_agent.py``` with the URI containing DB/tables/user/port.. experiments you want to try - the key names.*


### Step 1:

*1. Fill ```general_prompt_langchain.py``` with the prefix and suffix prompt for you text_to_sql_agent. 1 pref prompt and 1 suffix prompt.*

*2. In order to have good performance in production, it is very important to complete the example of natural language query vs sql query*

### Step 2:

*1. Fill ```experiment.json``` with the user natural language query you want to try in your live model and the corresponding SQL Queries.*

### Step 3:

*1. Fill ```experiment.json``` with the models (llms you want to test) for your live model.*

### Step 4:

*1. Fill ```queries.json``` with the queries ( you want to test to evaluate) your live model.*

### Step 5:

*1. Launch ```benchmark_sql_agent_langchain``` with the experiments folder parameters to launch your experiment and get an evaluation for your live system.*
*2. Launching command: ```nohup python model/benchmark_langchain_agent.py --folder EXPERIMENTS/<name_of_experiment_folder> > experiment_xyz.log```

*Please notice that this open source repository is not perfect and contains some amelioration that could be made such as adding quality metrics, llm parameters...*

*The objective is to contribute to your development acceleration of any companies by proviting a robust text-to-sql benchmarking code which would be an helpful engine to test your text-to-sql engine before deploying into production, for your specific use-case.*

*For any new ideas or contributions, you could send an e-mail to info@pulse-partners.ch and we would be happy to assist and help you in <72H*