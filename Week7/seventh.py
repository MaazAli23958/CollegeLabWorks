INFINITY = float("inf")
ITERATIONS = 3            


def get_network_topology():
    network = {}

    num_routers = int(input("Enter number of routers: ").strip())
    if num_routers <= 0:
        raise ValueError("Number of routers must be a positive integer.")

    routers = []
    for i in range(num_routers):
        name = input(f"Enter name for router #{i+1}: ").strip()
        if not name:
            raise ValueError("Router name cannot be empty.")
        if name in routers:
            raise ValueError(f"Duplicate router name '{name}' detected.")
        routers.append(name)
        network[name] = {"neighbors": {}}

    for r in routers:
        raw = input(
            f"Enter neighbors of {r} with hop counts "
            f"(format: Neighbor:Cost, Neighbor:Cost) or leave blank if none: "
        ).strip()

        if not raw:
            continue

        for pair in raw.split(","):
            pair = pair.strip()
            if not pair:
                continue

            if ":" not in pair:
                raise ValueError(f"Invalid entry '{pair}'. Expected format Neighbor:Cost.")

            nbr, cost_str = pair.split(":", 1)
            nbr = nbr.strip()
            cost_str = cost_str.strip()

            if not cost_str.isdigit() or int(cost_str) <= 0:
                raise ValueError(
                    f"Invalid hop count '{cost_str}' for neighbor '{nbr}'. "
                    f"Must be a positive integer."
                )

            network[r]["neighbors"][nbr] = int(cost_str)

    for r, data in network.items():
        valid = {}
        for nbr, cost in data["neighbors"].items():
            if nbr not in routers:
                print(f"Warning: Router '{r}' references unknown neighbor '{nbr}'. Ignoring it.")
                continue
            if nbr == r:
                print(f"Warning: Router '{r}' cannot list itself as a neighbor. Ignoring it.")
                continue
            valid[nbr] = cost
        data["neighbors"] = valid

    return network


def initialize_routing_tables(network):
    tables = {}
    all_routers = list(network.keys())
    for r in all_routers:
        tables[r] = {}
        for dest in all_routers:
            if dest == r:
                tables[r][dest] = {"cost": 0, "next_hop": r}
            elif dest in network[r]["neighbors"]:
                cost = network[r]["neighbors"][dest]
                tables[r][dest] = {"cost": cost, "next_hop": dest}
            else:
                tables[r][dest] = {"cost": INFINITY, "next_hop": None}

    return tables


def run_rip_simulation(network, iterations=ITERATIONS):
    tables = initialize_routing_tables(network)

    print("\n--- ROUND 0 (Initialization) ---")
    _print_tables(tables)

    for k in range(1, iterations + 1):
        print(f"\n--- ROUND {k} ---")

        prev = {r: {d: info.copy() for d, info in row.items()} for r, row in tables.items()}

        next_tables = {r: {d: info.copy() for d, info in row.items()} for r, row in prev.items()}

        for r in network.keys():
            for n, link_cost in network[r]["neighbors"].items():
                if n not in prev:
                    print(f"Warning: Neighbor '{n}' missing table; skipping.")
                    continue

                neighbor_view = prev[n]
                for dest, route in neighbor_view.items():
                    if dest == r:
                        continue

                    new_cost = link_cost + route["cost"]

                    if new_cost < next_tables[r][dest]["cost"]:
                        next_tables[r][dest] = {"cost": new_cost, "next_hop": n}

        tables = next_tables

        _print_tables(tables)

    return tables


def _print_tables(tables):
    """Pretty-printer for routing tables with ∞ for infinity."""
    for r, row in tables.items():
        print(f"\nRouting table for {r}:")
        for dest, info in row.items():
            cost = info["cost"] if info["cost"] != INFINITY else "∞"
            print(f"  to {dest}: cost={cost}, next_hop={info['next_hop']}")


if __name__ == "__main__":
    print("RIP Simulation - User Defined Topology and Hop Counts")

    topology = get_network_topology()

    final_tables = run_rip_simulation(topology, iterations=ITERATIONS)

    print("\n=== Final Routing Tables ===")
    _print_tables(final_tables)