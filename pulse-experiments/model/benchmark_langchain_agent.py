import time
import csv
import json
import argparse
import logging
import sys
import init_sql_agent
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
import openai
openai.api_key = ""



def check_response_langchain(response):
    # Check if 'result' key is in response.metadata and it's not an empty list
    if response['intermediate_steps'][0][1]:
        return 1
    else:
        return 0


def benchmark_query_engine(query_engine,
                           queries,
                           folder,
                           query_augm=1,
                           outputfile="results.csv"):
    results = []
    for query in queries:
        for i in range(query_augm) :
            start_time = time.time()

            # Executing the SQL query
            response = query_engine.query(query)
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Quality assessment using GPT-4
            result = {
                'query': query,
                'sql_query': response.metadata["sql_query"],
                'response': response.response,
                'elapsed_time': elapsed_time,
                'quality': "Untested",
                'response_bin': check_response(response)
            }

            results.append(result)
            print(f"Query: {query}\nElapsed Time: {elapsed_time}s\nResponse: {response}\n")

    with open(folder+outputfile,
              'w',
              newline='',
              encoding='utf-8') as csvfile:

        # Define the column headers for the CSV file
        fieldnames = ['query', 'sql_query', 'response', 'elapsed_time', 'quality', 'response_bin']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the rows
        for result in results:
            writer.writerow(result)

    print(f"Data saved to CSV file: {outputfile}")

    return results

def sql_retrieve(response) :
    if response['intermediate_steps'][0] :
        return response['intermediate_steps'][0][0].dict()['tool_input']
    else: return None
def load_global_variables_from_file(file_path):
    # Load global variables fron a file.
    global_vars = {}
    try:
        with open(file_path, 'r') as file:
            # Exécuter le contenu du fichier
            exec(file.read(), global_vars)
    except FileNotFoundError as e:
        print(f"Erreur de fichier : {e}")
    except Exception as e:
        print(f"Erreur lors de l'exécution du script : {e}")

    return global_vars

def experiment(experiment_folder) :
    """
    Function used to run several experiments.
    - Next step: add parallelization - quality metric - LLM Hyperparameters.
    """
    try:
        with open(f"{experiment_folder}/experiment.json", "r") as file:
            experiments = json.load(file)
    except Exception as e:
        print(f"Error reading queries.json: {e}")
        experiments = {}

    global_vars = load_global_variables_from_file(experiment_folder+"/general_prompt_langchain.py")

    for experiment_name,dict_experiment in experiments.items() :
        queries = dict_experiment.get('queries', [])
        llms = dict_experiment.get('llms',[])
        prompt_synthesis_name = dict_experiment.get('prompt_synthesis', None)
        prompt_text_to_sql_name = dict_experiment.get('prompt_text_to_sql', None)
        query_augm = dict_experiment.get('query_augm', 3)

        for llm in llms :
            agent = init_sql_agent.sql_agent(db=None,
                                             llm=llm,
                                             prompt=global_vars.get(prompt_text_to_sql_name,None),
                                             suffix=global_vars.get(prompt_synthesis_name,None))
            benchmark_sql_agent_langchain(queries,
                                          agent,
                                          folder,
                                          query_augm=query_augm,
                                          outputfile=experiment_name+"_llms_results.csv")





if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Experimental query engine management script.")

    parser.add_argument("--folder",
                        help="Path of the folder for the experiment",
                        required=False)

    parser.add_argument("--tables",
                        nargs='+',
                        help="List of tables",
                        required=False,
                        default=["your_table"])

    args = parser.parse_args()

    # Assuming the folder path is stored in a variable named 'folder'
    folder=args.folder
    benchmark_results = experiment(experiment_folder=args.folder)

    print("Operation completed successfully.")