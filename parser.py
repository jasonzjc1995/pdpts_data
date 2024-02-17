def read_instance(filename, display=False):
    '''
    Read instance from a filename
    '''
    print(filename)
    f = open(filename, 'r')
    
    # numbers of ...
    param = f.readline()
    list_param = param.split()
    instance_ID = int(list_param[0])
    num_nodes = int(list_param[1])
    num_deges = int(list_param[2])
    num_trucks = int(list_param[3])
    num_cargos = int(list_param[4])
    
    # initialization
    constant = {}
    nodes = []
    coordinates = {}
    edges = {}
    trucks = {}
    cargos = {}

    # constant
    param = f.readline()
    list_param = param.split()
    constant['truck_fixed_cost'] = float(list_param[0])
    constant['truck_running_cost'] = float(list_param[1])
    constant['cargo_reloading_cost'] = float(list_param[2])
    constant['node_fixed_time'] = float(list_param[3])
    constant['loading_variation_coefficient'] = float(list_param[4])

    # coordinates
    for r in range(num_nodes):
        param = f.readline()
        list_param = param.split()
        nodes.append(str(list_param[0]))
        coordinates[str(list_param[0])] = (float(list_param[1]), float(list_param[2]))

    # edges
    for r in range(num_deges):
        param = f.readline()
        list_param = param.split()
        edges[(str(list_param[0]), str(list_param[1]))] = int(list_param[2])

    # trucks
    for r in range(num_trucks):
        param = f.readline()
        list_param = param.split()
        trucks[str(list_param[0])] = (str(list_param[1]), str(list_param[2]), 
                                      int(list_param[3]), int(list_param[4]))

    # cargos
    for r in range(num_cargos):
        param = f.readline()
        list_param = param.split()
        cargos[str(list_param[0])] = (int(list_param[1]), int(list_param[2]), 
                                      int(list_param[3]), str(list_param[4]), str(list_param[5]))
    
    f.close()

    if display:
        print("The ID of the instance is:", instance_ID)
        print("The constants are:")
        for k,v in constant.items():
            print(k, v)
        print("The nodes are:\n", nodes)
        print("The edges are:\n", edges)
        print("The trucks are:")
        for k,v in trucks.items():
            print(k, v)
        print("The cargos are:")
        for k,v in cargos.items():
            print(k, v)
    
    return instance_ID, constant, nodes, coordinates, edges, trucks, cargos