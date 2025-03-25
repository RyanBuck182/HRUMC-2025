import io
import os
import subprocess
import sys
from typing import Callable


class NodeDoesNotExistException(Exception):
    """Exception for when a node is referenced that does not exist."""
    pass


class GraphVizTree:
    """Represents a tree to be displayed with graphviz.

    Doesn't actually do anything to ensure it's used like a tree, you're just
    supposed to. So don't do otherwise or I'll be sad.
    """

    def __init__(self, root: str, resolution: int = 96,
                 output_folder: str = "output") -> None:
        """Initialize the tree."""
        self.children: dict[str, list[str]] = {}
        self.values: dict[str, int | None] = {}

        self.add_node(root)
        self._root: str = root

        self._resolution = resolution
        self._selected: list[str | None] = [None]
        self._selected_edge: tuple[str | None, str | None] = (None, None)
        self._eliminated: dict[str, list[str]] = {}
        self._output_folder: str = os.path.join(os.getcwd(), output_folder)
        self._output_counter: int = 0
        self._alpha_beta: dict[str, tuple[str, str]] = {}

    def node_exists(self, node: str) -> bool:
        """Return whether a node exists."""
        return node in self.children.keys()

    def add_node(self, node: str) -> None:
        """Adds a node to the graph.

        Does nothing if the node is already in the graph.
        """
        if not self.node_exists(node):
            self.children[node] = []
            self.values[node] = None

    def add_edge(self, parent: str, child: str) -> None:
        """Add an edge (and its related nodes) to the graph."""
        self.add_node(parent)
        self.add_node(child)
        self.children[parent].append(child)

    def set_value(self, node: str, value: int) -> None:
        """Set the value of a node."""
        self.add_node(node)
        self.values[node] = value

    def select(self, *nodes):
        """Select node(s) to be highlighted when displayed."""
        self._selected = []
        for node in nodes:
            if node is None or self.node_exists(node):
                self._selected.append(node)
            else:
                raise NodeDoesNotExistException

    def select_edge(self, parent: str | None,
                    child: str | None = None) -> None:
        """Select an edge to be highlighted when displayed."""
        if parent is None:
            self._selected_edge = (None, None)
        else:
            self._selected_edge = (parent, child)

    def eliminate_edge(self, parent: str, child: str) -> None:
        """Eliminate an edge to be grayed out when displayed."""
        if parent not in self._eliminated.keys():
            self._eliminated[parent] = []

        self._eliminated[parent].append(child)

    def set_alpha_beta(self, node: str, alpha: str, beta: str) -> None:
        """Set alpha beta of a node."""
        self._alpha_beta[node] = (alpha, beta)

    def visualize_graph(self, file_name: str) -> None:
        """Output the tree to a file.

        File will be in the specified output folder, or the current working
        directory. Uses graphviz.
        """
        print(f"Outputting {file_name}")

        # Get graph code to be visualized
        graph_code = self._format_graph()

        # Get file path and ensure destination folder exists
        output_file = os.path.join(self._output_folder, f"{file_name}.png")
        os.makedirs(self._output_folder, exist_ok=True)

        # Visualize with graphviz
        p = subprocess.Popen(["dot", "-Tpng", "-o", f"{output_file}"],
                             stdin=subprocess.PIPE, text=True, encoding="utf-8")
        p.stdin.write(graph_code)

    def visualize_graph_sequential(self, file_prefix: str) -> None:
        """Output the tree to a file, incrementing a suffix by one each time.
        """
        suffix = str(self._output_counter).zfill(3)
        self.visualize_graph(f"{file_prefix}{suffix}")
        self._output_counter += 1

    def sequencer(self, file_prefix: str) -> Callable:
        def graph_step():
            self.visualize_graph_sequential(file_prefix)

        return graph_step

    def _format_graph(self, node: str = None, level: int = 0) -> str:
        """Format the graph for output with graphviz.

        Works recursively.
        """
        code = ""

        # Start code if root
        if node is None:
            node = self._root
            code += "graph {\n"
            code += f"resolution={self._resolution}\n"
            code += f"node [shape=box]\n"

        # Add node code
        node_code = f"{node} [label="
        if node not in self._alpha_beta:
            node_code += f'"{self.values[node] or ""}"'
        else:
            node_code += f"""<
            <TABLE BORDER="0" CELLBORDER="0">
                <TR>
                    <TD COLSPAN="2">{self.values[node] or " "}</TD>
                </TR>
                <TR>
                    <TD>{f"a={self._alpha_beta[node][0]}" if self._alpha_beta[node][0] else " "*6}</TD>
                    <TD>{f"b={self._alpha_beta[node][1]}" if self._alpha_beta[node][1] else " "*6}</TD>
                </TR>
            </TABLE>
            >"""

        if node in self._selected:
            node_code += ' fillcolor=green style=filled penwidth=2'
        elif node in [node
                      for nodelist in self._eliminated.values()
                      for node in nodelist]:
            node_code += ' color=gray60'
        node_code += "]\n"
        code += node_code

        # Determine edge color from current level
        edge_color = "blue" if level % 2 == 0 else "red"

        # Add child edge code
        for child in self.children[node]:
            code += f"{node} -- {child}"
            if (node == self._selected_edge[0]
                    and child == self._selected_edge[1]):
                code += " [color=green penwidth=3]"
            elif (node in self._eliminated.keys()
                  and child in self._eliminated[node]):
                code += f" [color=gray60]"
            else:
                code += f" [color={edge_color}]"
            code += "\n"
            code += self._format_graph(child, level + 1)

        # End code if root
        if node == self._root:
            code += "}"

        return code
