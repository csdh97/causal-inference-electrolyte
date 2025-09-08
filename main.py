import argparse
import numpy as np
import pandas as pd
import networkx as nx
from dowhy import CausalModel
from tqdm import tqdm

from CausalGraph import CausalGraph

def extract_treatment_outcome(causal_graph):

    outcomes = [n for n in causal_graph.nodes if causal_graph.out_degree(n) == 0]
    all_treatments = []
    for outcome in outcomes:

        treatments = nx.ancestors(causal_graph, outcome)
        all_treatments.append(treatments)
    
    return all_treatments, outcomes

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, choices=['custom', 'notears'], default='custom', help='causal graph mode')
    parser.add_argument('--data_path', type=str, default='./data/experiment_data.xlsx', help='data path')
    parser.add_argument('--output_variable', type=str, default='all', help='output variable')
    parser.add_argument('--save_path', type=str, default='./save.xlsx', help='save path')

    args = parser.parse_args()

    return args

if __name__ == "__main__":

    args = parse_args()
    mode, data_path = args.mode, args.data_path
    output_variable = args.output_variable
    save_path = args.save_path

    # read data
    raw_input = pd.read_excel(data_path)

    # define causal graph
    causal_graph = CausalGraph(mode=mode).causal_graph()

    save_results = []
    if output_variable == 'all':

        treatments, outcomes = extract_treatment_outcome(causal_graph)
        assert len(treatments) == 1
        all_pair_treatment_outcome = [(x, y) for x in treatments[0] for y in outcomes]

        for edge in tqdm(all_pair_treatment_outcome, desc='inference on all variables'):

            model = CausalModel(
                data = raw_input,
                treatment=edge[0],
                outcome=edge[1],
                graph=causal_graph
                )

            identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)
            causal_estimate = model.estimate_effect(identified_estimand,
                    method_name="backdoor.linear_regression")

            estimate_value = causal_estimate.value

            save_results.append([edge[0], edge[1], estimate_value])

    elif isinstance(output_variable, str):
        
        items = [x.strip() for x in output_variable.split(',')]
        all_pair_treatment_outcome = [items[i:i+2] for i in range(0, len(items), 2)]

        for variable in tqdm(all_pair_treatment_outcome, desc='inference on specific variables'):

            model = CausalModel(
            data = raw_input,
            treatment=variable[0],
            outcome=variable[1],
            graph=causal_graph
            )

            identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)
            causal_estimate = model.estimate_effect(identified_estimand,
                    method_name="backdoor.linear_regression")

            estimate_value = causal_estimate.value

    df = pd.DataFrame(save_results, columns=["treatment", "outcome", "causal estimate value"])
    df.to_excel(save_path, index=False)