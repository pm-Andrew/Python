# pdf-sand.py
# Andrew
# Shirtificate Sandbox


from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Setting font: helvetica 32
        self.set_font("helvetica", size=40)
        # Moving cursor to the right: or centers the Title
        self.cell(45)
        # Printing title:
        self.cell(25, 10, "CS50 Shirtificate")

    def add_shirt_image_and_text(self, user_name):
        # adding the shirt image
        PDF.image(self,"shirtificate.png", x="C", y=50, w=200, h=200, keep_aspect_ratio=True)
        # Setting font: helvetica 32
        self.set_font("helvetica", size=24)
        # Setting Color: white
        self.set_text_color(255,255,255)
        # Printing title:
        self.cell(250, 200, f"{user_name} took CS50", align="C", center=True)


def main():
    # get name
    user_name = input("Name: ")
    # Instantiation of inherited class
    pdf = PDF()
    # Adding a Page
    pdf.add_page()
    # Calling the add_shirt_image_and_text()
    pdf.add_shirt_image_and_text(user_name)
    # Printing out the pdf
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
