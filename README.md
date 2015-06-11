# 3D_Printing_Molecules

Requirements:
    [Blender](https://www.blender.org/)
        with the PDB import module
    [Cura](https://software.ultimaker.com/)
    [Makerware](http://www.makerbot.com/desktop#download)
    [Slic3r](http://slic3r.org/)
      With either:
        • source code edits to allow for closer support material
        • the new experimental 1.2.8+ version

PDB file:
    1. Create all the bonds/connections you want to see rods for before importing into blender.
        • I recomend PyMol for this.
    2. You can also change the elements to emphasize certain atoms due to their radii

Blender:
    1. Import PDB file
        • For overlapping spheres:
            • Balls: ~1.20
        • For Ball and Stick
            • Balls 0.80
            • Stick Radius: 0.20
    2. Export as obj file

Cura:
    1. Open OBJ file, rotate as needed, and save as .stl file.

Makerware:
    1. Open stl file and size/place on platform as needed. (Can print multiple structures at once)
    2. Save as .stl file

Slic3r:
    1. Open STL file. (This will fix any errors in the file)
    2. Save/Export the fixed STL file.
    3. Restart Slic3r and open now fixed STL file
    4. Slice

Clean-Slic3r-GCODE.py
    1. Run python2.7 Clean-Slic3r-GCODE.py -i <input gcode file> -o <output cleaned gcode file>

Makerware:
    1. Print from file the cleaned Slic3r gcode to x3g format.
    2. Transfer to SD.
    3. Print

Good Luck!
TJ Mustard
