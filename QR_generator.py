"""
QR Code Generator
Author  : Bala Krishna Konakanchi
Course  : MSCS-633-A01  Advanced Artificial Intelligence
Assign. : Hands-On Assignment 2
Desc.   : Generates a QR code image from a given URL.
"""

import qrcode


def generate_qr_code(url: str, output_file: str = "qr_code.png") -> None:
    """
    Generate a QR code for the given URL and save it as a PNG.

    Args:
        url (str)         : The URL to encode.
        output_file (str) : Destination filename.
    """
    # Instantiate QRCode with desired configuration
    qr = qrcode.QRCode(
        version=None,                                       # auto-select
        error_correction=qrcode.constants.ERROR_CORRECT_M, # ~15% tolerance
        box_size=10,                                        # pixels/module
        border=4,                                           # quiet-zone
    )

    qr.add_data(url)   # encode the URL
    qr.make(fit=True)  # choose optimal version automatically

    # Render as a black-on-white image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    print(f"QR Code successfully generated: {output_file}")
    print(f"QR CODE LINK: {url}")


def main():
    """Entry point."""
    target_url      = "https://www.bioxsystems.com"
    output_filename = "qr_code.png"
    generate_qr_code(target_url, output_filename)


if __name__ == "__main__":
    main()