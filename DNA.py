import random, sys, time, os

# Enable ANSI color codes on Windows
if sys.platform == 'win32':
    os.system('color')

# Define ANSI color codes for a more realistic look
COLORS = {
    'A': '\033[92m',  # Green
    'T': '\033[91m',  # Red
    'C': '\033[94m',  # Blue
    'G': '\033[93m',  # Yellow
    'BACKBONE': '\033[90m',  # Dark Gray
    'RESET': '\033[0m'   # Reset to default
}

PAUSE = 0.15  # (!) Try changing this to 0.5 or 0.0.

# Using the wider ROWS from the previous example
ROWS = [
    #12345678901234567890123 <- Use this to measure the number of spaces:
    '           ##',  # Index 0
    '          #{}--{}#',
    '         #{}-----{}#',
    '        #{}--------{}#',
    '       #{}----------{}#',
    '      #{}----------{}#',
    '       #{}--------{}#',
    '        #{}-----{}#',
    '         #{}--{}#',
    '          ##',  # Index 9
    '         #{}--{}#',
    '        #{}-----{}#',
    '       #{}--------{}#',
    '      #{}----------{}#',
    '       #{}----------{}#',
    '        #{}--------{}#',
    '         #{}-----{}#',
    '          #{}--{}#']
    #12345678901234567890123 <- Use this to measure the number of spaces:

try:
   
    rowIndex = 0

    while True:  # Main program loop.
        # Increment rowIndex to draw next row:
        rowIndex = rowIndex + 1
        if rowIndex == len(ROWS):
            rowIndex = 0

        # Get the row template
        row_template = ROWS[rowIndex]

        # String to be printed
        final_row = ""

        # Row indexes 0 and 9 don't have nucleotides:
        if rowIndex == 0 or rowIndex == 9:
            final_row = row_template.replace('#', COLORS['BACKBONE'] + '#' + COLORS['RESET'])
        else:
            # Select random nucleotide pairs
            randomSelection = random.randint(1, 4)
            if randomSelection == 1:
                n1, n2 = 'A', 'T'
            elif randomSelection == 2:
                n1, n2 = 'T', 'A'
            elif randomSelection == 3:
                n1, n2 = 'C', 'G'
            elif randomSelection == 4:
                n1, n2 = 'G', 'C'
            
            # Create colored nucleotide strings
            leftN_colored = COLORS[n1] + n1 + COLORS['RESET']
            rightN_colored = COLORS[n2] + n2 + COLORS['RESET']
            
            # Format the row with colored nucleotides
            formatted_row = row_template.format(leftN_colored, rightN_colored)
            
            # Color the backbone
            final_row = formatted_row.replace('#', COLORS['BACKBONE'] + '#' + COLORS['RESET'])

        # Print the row.
        print(final_row)
        time.sleep(PAUSE)  # Add a slight pause (now pauses on every line).

except KeyboardInterrupt:
    print("\nDNA Animation stopped.")
    sys.exit()  