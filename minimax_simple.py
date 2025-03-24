from tree import GraphVizTree


def main():
    minimax_simple = GraphVizTree("R", resolution=192,
                                  output_folder="output/minimax_simple")
    step = minimax_simple.sequencer("minimax_simple")

    # Creating the tree
    minimax_simple.add_edge("R", "A")
    minimax_simple.add_edge("R", "B")
    minimax_simple.add_edge("R", "C")

    # Running through minimax on a simple example and outputting it
    step()

    minimax_simple.select("R")
    step()

    minimax_simple.select("A")
    step()

    minimax_simple.set_value("A", -2)
    step()

    minimax_simple.select("R")
    step()

    minimax_simple.set_value("R", -2)
    step()

    minimax_simple.select("B")
    step()

    minimax_simple.set_value("B", 4)
    step()

    minimax_simple.select("R")
    step()

    minimax_simple.set_value("R", 4)
    step()

    minimax_simple.select("C")
    step()

    minimax_simple.set_value("C", 3)
    step()

    minimax_simple.select("R")
    step()

    minimax_simple.select(None)
    minimax_simple.select_edge("R", "B")
    step()


if __name__ == "__main__":
    main()
