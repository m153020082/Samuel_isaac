# Guide to Isaac

## Starting Isaac

```bash
cd C:\isaacsim
.\isaac-sim.bat
```
Isaac will start in around 100 seconds

## Export URDF file from SolidWorks
After creating the assembly, initiate the URDF exporter from Tools/Export as URDF, rename the base component and click the base coordinate(or leave it automatically), select the base component.
If there's child links, enable and select it from the tree at the bottom, after renaming the child link and joint(if there's any), select the reference coordinate system(e.g. the midpoint of the revolting pin) and reference axis(e.g. center line connecting the pin's two faces), select the pivoting part and export.
in the Exporter, click joint and set the limits(important), then select child link(e.g. pivot) afterward, click Export URDF and Meshes.

## Import URDF into Isaac


