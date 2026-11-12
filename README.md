## Starting Isaac
```bash
cd C:\isaacsim
.\isaac-sim.bat
```

## Export URDF file from SolidWorks
After creating the assembly, initiate the URDF exporter from Tools/Export as URDF, rename the base component and click the base coordinate(or leave it automatically), select the base component.
If there's child links, enable and select it from the tree at the bottom, after renaming the child link and joint(if there's any), select the reference coordinate system(e.g. the midpoint of the revolting pin) and reference axis(e.g. center line connecting the pin's two faces), select the pivoting part and export.
in the Exporter, click joint and set the limits(important), then select child link(e.g. pivot) afterward, click Export URDF and Meshes.
<img width="1919" height="1079" alt="Screenshot 2026-11-12 174656" src="https://github.com/user-attachments/assets/ef282605-9886-4caf-b3d6-daff5b23e64c" />
<img width="1919" height="1079" alt="Screenshot 2026-11-12 174705" src="https://github.com/user-attachments/assets/5c0ec2f7-af6b-440d-8dac-fc564d3fb868" />


## Export URDF assembly with multiple joints
URDF exporter in Solidworks uses branches, it can't link back to the same part if it has multiple joints, solve this by assembling in the Isaac GUI.

## Import URDF into Isaac
Click File->Import->Select URDF file
