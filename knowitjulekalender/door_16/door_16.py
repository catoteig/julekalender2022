from PIL import Image


def main():

	# I modified this code: https://pastebin.com/CWkGcRjw

	im1 = Image.open('giraffe.png')
	im2 = Image.open('harambe.png')

	pix1 = im1.getchannel('R').load()
	pix2 = im2.getchannel('R').load()

	w, h = im1.size

	imn = Image.new("RGB", (w, h), "black")
	pixn = imn.load()

	for i in range(w):
		for j in range(h):
			r1 = pix1[i, j]
			r2 = pix2[i, j]

			rn = r1 ^ r2

			pixn[i, j] = (rn)

	imn.save("xored_image.png")
	# Put this image into Aperisolv.com 🦊


if __name__ == '__main__':
	main()
