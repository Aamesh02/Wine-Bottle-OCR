    from PIL import Image, ImageOps

    def correct_orientation_to_portrait(image):
        """
        Forces the image to portrait orientation with the top of the bottle at the top.
        Assumes the bottle may be rotated 90 or 270 degrees.
        """
        # First try EXIF-based correction
        image = ImageOps.exif_transpose(image)
        print(type(image))

        # Now check if width is greater than height (likely landscape)
        if image.width > image.height:
            # Rotate counter-clockwise to make it portrait with bottle up
            print(image.width, image.height)
            image = image.rotate(-90, expand=True)

        return image

    # Load the image
    image_path = "SampleImages/wine1.jpg"
    original_image = Image.open(image_path)

    # Show original image
    original_image.show(title="Original")

    # Correct orientation
    corrected_image = correct_orientation_to_portrait(original_image)

    # Show corrected image
    corrected_image.show(title="Corrected")

    # Save for verification
    corrected_image.save("SampleImages/wine1_corrected.jpg")
