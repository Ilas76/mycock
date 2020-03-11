import sys
import cv2

from run import process
import fire
"""
main.py

 How to run:
 python3 main.py

"""

# ------------------------------------------------- main()
def main(input, output):

	#Read input image
	dress = cv2.imread(input)

	#Process
	watermark = process(dress)

	# Write output image
	cv2.imwrite(output, watermark)

	#Exit
	sys.exit()

if __name__ == '__main__':
  fire.Fire(main)
