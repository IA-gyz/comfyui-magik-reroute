# Magik Reroute

A simple ComfyUI passthrough node with one universal input and one universal output.
It returns the incoming value unchanged, without copying or converting it.

## Install

Extract the `Magik_Reroute` folder into `ComfyUI/custom_nodes/`, restart ComfyUI,
and refresh the browser. Search for **Magik Reroute** or find it under **Magik/Utils**.

Connect a source to `value`, then connect the output to a compatible destination.
The wildcard socket does not convert data: the destination must accept the actual
value supplied upstream. No extra dependencies or frontend patches are needed.
