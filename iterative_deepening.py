from tree import GraphVizTree


def main():
    iterative_deepening = GraphVizTree("R", resolution=192,
                                       output_folder="output/iterative_deepening")
    step = iterative_deepening.sequencer("iterative_deepening")

    per_layer = 3

    for i in range(per_layer):
        iterative_deepening.add_edge("R", f"v{i}")
    step()

    for i in range(per_layer):
        for j in range(per_layer):
            iterative_deepening.add_edge(f"v{i}", f"v{i}v{j}")
    step()

    for i in range(per_layer):
        for j in range(per_layer):
            for ii in range(per_layer):
                iterative_deepening.add_edge(f"v{i}v{j}", f"v{i}v{j}v{ii}")
    step()

    for i in range(per_layer):
        for j in range(per_layer):
            for ii in range(per_layer):
                for jj in range(per_layer):
                    iterative_deepening.add_edge(f"v{i}v{j}v{ii}", f"v{i}v{j}v{ii}v{jj}")
    step()


if __name__ == "__main__":
    main()
