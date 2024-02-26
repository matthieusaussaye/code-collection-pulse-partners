# code-collection-pulse-partners 1 - text-to-sql

This repository is at the destination of any IT teams, Data Science agency, Data Scientist Freelance aiming to unlock growth through LLMs by deploying text-to-SQL systems.

## Pulse Experiments

### Initialisation :

1. Initialize ```experiment.json``` with the experiments names.

2Initialize ```init_sql_agent.py``` with the URI containing: DB | tables | user | port.


### Step 1:

1. Fill ```general_prompt_langchain.py``` with the prefix and suffix prompt content used in your text_to_sql_agent.

2. In order to get good performance in production, it is very important to complete the examples (few-shots learning part).

### Step 2:

1. Fill ```experiment.json``` with the user natural language queries, representative of the final use in your live model + corresponding SQL Queries.

### Step 3:

1. Fill ```experiment.json``` with the models (llms you want to test) for your live model.

### Step 4:

1. Fill ```queries.json``` with the queries ( you want to test to evaluate) your live model.

### Step 5:

1. Launch ```benchmark_sql_agent_langchain``` with the experiments (folder parameters) and save the evaluation file.
2. Launching command: ```nohup python model/benchmark_langchain_agent.py --folder EXPERIMENTS/<name_of_experiment_folder> > experiment_xyz.log```

Please notice that this open source repository is not perfect and contains some amelioration that could be made such as: adding quality metrics, tuning llm parameters....
The goal is to contribute to the growth of any data-driven companies by providing a robust text-to-sql benchmarking code which would be a key engine to test your text-to-sql system before deploying it into production, for your specific use-case.
For any new ideas or contributions, you could send an e-mail to info@pulse-partners.ch and we would be happy to assist and help you in <72H