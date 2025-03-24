from tree import GraphVizTree


def main():
    minimax = GraphVizTree("R", resolution=192,
                           output_folder="output/minimax")
    step = minimax.sequencer("minimax")

    # Creating the tree
    minimax.add_edge("R", "A")
    minimax.add_edge("R", "B")
    minimax.add_edge("A", "A1")
    minimax.add_edge("A", "A2")
    minimax.add_edge("B", "B1")
    minimax.add_edge("B", "B2")

    # Running through minimax and outputting it
    step()

    minimax.select("R")
    step()

    minimax.select("A")
    step()

    minimax.select("A1")
    step()

    minimax.set_value("A1", 8)
    step()

    minimax.select("A")
    step()

    minimax.set_value("A", 8)
    step()

    minimax.select("A2")
    step()

    minimax.set_value("A2", -6)
    step()

    minimax.select("A")
    step()

    minimax.set_value("A", -6)
    step()

    minimax.select("R")
    step()

    minimax.set_value("R", -6)
    step()

    minimax.select("B")
    step()

    minimax.select("B1")
    step()

    minimax.set_value("B1", 4)
    step()

    minimax.select("B")
    step()

    minimax.set_value("B", 4)
    step()

    minimax.select("B2")
    step()

    minimax.set_value("B2", 7)
    step()

    minimax.select("B")
    step()

    minimax.select("R")
    step()

    minimax.set_value("R", 4)
    step()

    minimax.select(None)
    minimax.select_edge("R", "B")
    step()


if __name__ == "__main__":
    main()
