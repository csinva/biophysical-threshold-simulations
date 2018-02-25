# installing NEURON
- download the OS installer for Mac
- to get nrn to run, I also had to install X11 as described on their website


# compiling mod files
- the files in the `mechanism` directory must be compiled before they are usable
- to do this on mac, drag the entire `mechanism` directory into the mknrndll function in Applications
    - this results in the creation of an x86_64 subfolder in the mechanism folder


# running
- to run, cd into the mechanism directory
- running `nrngui run_act.hoc` should open the NEURON gui and display a plot of an action potential with the current settings
- `run_main.hoc` has more complicated settings