from tree import GraphVizTree


def main():
    minimax = GraphVizTree("r", resolution=192)

    # Creating the tree
    minimax.add_edge("r", "a")
    minimax.add_edge("r", "b")
    minimax.add_edge("r", "c")
    minimax.add_edge("a", "a1")
    minimax.add_edge("a", "a2")
    minimax.add_edge("b", "b1")
    minimax.add_edge("b", "b2")
    minimax.add_edge("c", "c1")
    minimax.add_edge("c", "c2")

    # Running through minimax and outputting it
    minimax.visualize_graph_sequential("minimax")

    minimax.select("r")
    minimax.visualize_graph_sequential("minimax")

    # Branch A
    minimax.select("a")
    minimax.visualize_graph_sequential("minimax")

    minimax.select("a1")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("a1", 15)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("a")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("a", 15)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("a2")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("a2", 8)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("a")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("a", 8)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("r")
    minimax.visualize_graph_sequential("minimax")

    # Branch B
    minimax.select("b")
    minimax.visualize_graph_sequential("minimax")

    minimax.select("b1")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("b1", 12)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("b")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("b", 12)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("b2")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("b2", 13)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("b")
    minimax.visualize_graph_sequential("minimax")

    minimax.select("r")
    minimax.visualize_graph_sequential("minimax")

    # Branch C
    minimax.select("c")
    minimax.visualize_graph_sequential("minimax")

    minimax.select("c1")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("c1", 7)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("c")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("c", 7)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("c2")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("c2", 3)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("c")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("c", 3)
    minimax.visualize_graph_sequential("minimax")

    minimax.select("r")
    minimax.visualize_graph_sequential("minimax")

    minimax.set_value("r", 12)
    minimax.visualize_graph_sequential("minimax")

    minimax.select(None)
    minimax.select_edge("r", "b")
    minimax.visualize_graph_sequential("minimax")


if __name__ == "__main__":
    main()
