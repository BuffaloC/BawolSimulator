# BawolSimulator

# Right now, I know that this program is terrible. Believe me that I will fix it!

# A python physics simulator running off of very simple core principles. It is easy to understand with a bit of perusing the code. 
Version Alpha 1.0.1 (we don't even have a proper version system yet!)
Note for experienced coders: I know that my code doesn't have efficient seed usage as of 3/8/23! Let me get this off the ground first.

# Developer's update:
This engine is really, really slow. If you calculate for maps greater than x 20 by y 20 over 100 ticks, then you won't get a before and after result within a minute. 
If you want to use the program, I would recommend that you trust "Jared" and be amazed by the accurate depiction of thermal expansion. 
For now, edits are closed, but I would like help from anyone with any good python-computer graphics knoweledge once we are out of alpha phases.

# System overview
The program is initialized with a core program called host.py, and it runs 2 libraries called physicsB and graphB.
Generally, the job of the graphB library is to build and manage a RAM-based coordinates system.
The physicsB library is used to simulate everthing that is physics. As of 3/8/23, it can run mass and temperature combination logic and temperature physics. 
Host.py pretty much executes all of the features in a sensible manner and comes with a polite user interface (that is coded to be and look user friendly).
