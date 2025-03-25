from tree import GraphVizTree


def main():
    ab_pruning = GraphVizTree("R", resolution=192,
                              output_folder="output/ab_pruning")
    step = ab_pruning.sequencer("ab_pruning")

    # Creating the tree
    ab_pruning.add_edge("R", "A")
    ab_pruning.add_edge("R", "B")
    ab_pruning.add_edge("A", "A1")
    ab_pruning.add_edge("A", "A2")
    ab_pruning.add_edge("B", "B1")
    ab_pruning.add_edge("B", "B2")
    ab_pruning.add_edge("B", "B3")
    ab_pruning.add_edge("B", "B4")
    ab_pruning.add_edge("B", "B5")
    ab_pruning.set_alpha_beta("R", "", "")
    ab_pruning.set_alpha_beta("A", "", "")
    ab_pruning.set_alpha_beta("B", "", "")

    # Running through alpha beta pruning and outputting it
    step()

    ab_pruning.select("R")
    step()

    ab_pruning.set_alpha_beta("R", "-∞", "+∞")
    step()

    ab_pruning.select("A")
    step()

    ab_pruning.set_alpha_beta("A", "-∞", "+∞")
    step()

    ab_pruning.select("A1")
    step()

    ab_pruning.set_value("A1", 8)
    step()

    ab_pruning.select("A")
    step()

    ab_pruning.set_value("A", 8)
    step()

    ab_pruning.set_alpha_beta("A", "-∞", "8")
    step()

    ab_pruning.select("A2")
    step()

    ab_pruning.set_value("A2", -6)
    step()

    ab_pruning.select("A")
    step()

    ab_pruning.set_value("A", -6)
    step()

    ab_pruning.set_alpha_beta("A", "-∞", "-6")
    step()

    ab_pruning.select("R")
    step()

    ab_pruning.set_value("R", -6)
    step()

    ab_pruning.set_alpha_beta("R", "-6", "+∞")
    step()

    ab_pruning.select("B")
    step()

    ab_pruning.set_alpha_beta("B", "-6", "+∞")
    step()

    ab_pruning.select("B1")
    step()

    ab_pruning.set_value("B1", -34)
    step()

    ab_pruning.select("B")
    step()

    ab_pruning.set_value("B", -34)
    step()

    ab_pruning.set_alpha_beta("B", "-6", "-34")
    step()

    ab_pruning.eliminate_edge("B", "B2")
    ab_pruning.eliminate_edge("B", "B3")
    ab_pruning.eliminate_edge("B", "B4")
    ab_pruning.eliminate_edge("B", "B5")
    step()

    ab_pruning.select("R")
    step()

    ab_pruning.select(None)
    ab_pruning.select_edge("R", "A")
    step()


if __name__ == "__main__":
    main()
