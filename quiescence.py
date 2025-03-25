from tree import GraphVizTree


def main():
    quiescence = GraphVizTree("R", resolution=192,
                              output_folder="output/quiescence")
    step = quiescence.sequencer("quiescence")

    # Creating the tree
    quiescence.add_edge("R", "A")
    quiescence.add_edge("R", "B")
    quiescence.add_edge("R", "C")

    quiescence.select("R")
    quiescence.select("A")
    quiescence.set_value("A", -2)
    quiescence.select("R")
    quiescence.set_value("R", -2)
    quiescence.select("B")
    quiescence.set_value("B", 4)
    quiescence.select("R")
    quiescence.set_value("R", 4)
    step()

    quiescence.select("C")
    step()

    quiescence.add_edge("C", "C1")
    quiescence.add_edge("C", "C2")
    step()

    quiescence.select("C1")
    step()

    quiescence.add_edge("C1", "C1A")
    quiescence.add_edge("C1", "C1B")
    step()

    quiescence.select("C1A")
    step()

    quiescence.set_value("C1A", 4)
    step()

    quiescence.select("C1")
    step()

    quiescence.set_value("C1", 4)
    step()

    quiescence.select("C1B")
    step()

    quiescence.set_value("C1B", 9)
    step()

    quiescence.select("C1")
    step()

    quiescence.set_value("C1", 9)
    step()

    quiescence.select("C")
    step()

    quiescence.set_value("C", 9)
    step()

    quiescence.select("C2")
    step()

    quiescence.set_value("C2", 12)
    step()

    quiescence.select("C")
    step()

    quiescence.select("R")
    step()

    quiescence.set_value("R", 9)
    step()

    quiescence.select(None)
    quiescence.select_edge("R", "C")
    step()


if __name__ == "__main__":
    main()
