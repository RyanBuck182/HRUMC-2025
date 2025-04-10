# HRUMC 2025

The [Hudson River Undergraduate Mathematics Conference](https://sites.google.com/view/hrumc) has a fairly self-explanatory name. Basically, a bunch of undergraduates go to a conference. The cool part is that we can also give presentations to each other.

Last year I had a great time and learned a ton from attending a bunch of presentations. This year, I decided to give a presentation myself.

My talk was on the **minimax** algorithm. I used the code in this repository to help me visualize it. I was originally going to do this manually with an online graphviz editor, but it would take ages if I wanted to go back and change something, as I would have to change every image. So I wrote this code to help me with this.

It doesn't actually implement the minimax algorithm or alpha-beta pruning. This is because I only needed to create one set of images per algorithm, so implementing the algorithm and hooking it up to the visualizer seems like overkill when I only needed to visualize it once.

[Here's](https://docs.google.com/presentation/d/1meLMQG2bs-70P7D5bQUR7LbV_eX2IyHiOageeqeiqT4/edit?usp=sharing) a link to the slides I presented at the conference.

[Here](./example) are the images you would get as output if you ran the program.

## How To Run

No python packages are necessary, however you do need to have [graphviz](https://graphviz.org/download/) installed with the `Graphviz\bin` folder added to the PATH environment variable (which the Windows Installer will do automatically if you choose the right option, if you're on Linux I'm sure you can figure it out yourself).

Awesome have fun!
