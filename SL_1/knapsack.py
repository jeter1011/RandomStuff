from ortools.linear_solver import pywraplp


def create_data_model():
    """Create the data for the example."""
    data = {}
    #weights = [92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
    weights = [92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72, 72]
    values = weights
    data['weights'] = weights
    data['values'] = values
    data['items'] = list(range(len(weights)))
    data['num_items'] = len(weights)
    num_bins = 3
    data['bins'] = list(range(num_bins))
    data['bin_capacities'] = [330, 350, 430]
    return data



def main():
    data = create_data_model()

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    # Constraints
    # Each item can be in at most one bin.
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) <= 1)
    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['weights'][i]
                for i in data['items']) <= data['bin_capacities'][j])

    # Objective
    objective = solver.Objective()

    for i in data['items']:
        for j in data['bins']:
            objective.SetCoefficient(x[(i, j)], data['values'][i])
    objective.SetMaximization()

    status = solver.Solve()

    
    if status == pywraplp.Solver.OPTIMAL:
        print('Total packed value:', objective.Value())
        total_weight = 0
        for j in data['bins']:
                bin_weight = 0
                bin_value = 0
                print('Bin ', j, '\n')
                for i in data['items']:
                    if x[i, j].solution_value() > 0:
                        print('Item', i, '- weight:', data['weights'][i], ' value:',
                            data['values'][i])
                        bin_weight += data['weights'][i]
                        bin_value += data['values'][i]
                print('Packed bin weight:', bin_weight)
                print('Packed bin value:', bin_value)
                print()
                total_weight += bin_weight
        print('Total packed weight:', total_weight)
    else:
        print('The problem does not have an optimal solution.')


if __name__ == '__main__':
    main()