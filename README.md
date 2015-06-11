# 3D_Printing_Molecules

Requirements:

    Blender
        with the PDB import module
    Cura
    Makerware
    Slic3r
      With either:
      • source code edits to allow for closer support material
      • the new experimental 1.2.8+ version

PDB file:

    Create all the bonds/connections you want to see rods for before importing into blender.
    You can also change the elements to emphasize certain atoms due to their radii

Blender:

    Import PDB file
        For overlapping spheres:
            Balls: ~1.20
        For Ball and Stick
            Balls 0.80
            Stick Radius: 0.20
    Export as obj file

Cura:

    Open OBJ file, rotate as needed, and save as .stl file.

Makerware:

    Open stl file and size/place on platform as needed. (Can print multiple structures at once)
    Save as .stl file

Slic3r:

    Open STL file. (This will fix any errors in the file)
    Save/Export the fixed STL file.
    Restart Slic3r and open now fixed STL file
    Slice

Clean-Slic3r-GCODE.py
    
    Run python2.7 Clean-Slic3r-GCODE.py -i <input gcode file> -o <output cleaned gcode file>

Makerware:
    
    Print from file the cleaned Slic3r gcode to x3g format.
    Transfer to SD.
    Print

Good Luck!
TJ Mustard
