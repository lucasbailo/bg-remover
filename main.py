import easygui
from PIL import Image
from rembg import remove

inputPath = easygui.fileopenbox(title="Select Image file")
outputPath = easygui.filesavebox(title="Save file image to")

input = Image.open(inputPath)
output = remove(input)
output.save(outputPath)