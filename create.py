from aztec_code_generator import AztecCode

# Create an Aztec code
aztec = AztecCode("https://www.youtube.com/")

# Save as PNG
aztec.save("aztec_code.png", module_size=4)
