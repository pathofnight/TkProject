import tkinter as tk
import os
from PIL import Image, ImageTk


class ColorChangeApp:
    def __init__(self, root):
        self.root = root
        self.color_change_dict = {
            "white": [5, 98, 255, 240, 240, 240],  # white in in inverted to white
            "black": [255, 255, 255, 81, 92, 93],  # black in inverted to black
            "red": [207, 54, 108, 52, 152, 219],  # red color for theroem
            "mud": [203, 103, 14, 203, 103, 14],
        }
        self.create_widgets()

    def create_widgets(self):
        # Create interactive dials/sliders for each color channel
        dial_length = 200  # Adjust this value to make the dials longer
        dial_width = 10  # Adjust this value to change the width of the dials
        slider_length = 10  # Adjust this value to change the slider length


        # Create all the dials
        self.white_r_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="White_r",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.white_r_dial.set(self.color_change_dict["white"][3])
        self.white_r_dial.grid(row=0, column=0)

        self.white_g_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="White_g",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.white_g_dial.set(self.color_change_dict["white"][4])
        self.white_g_dial.grid(row=0, column=1)

        self.white_b_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="White_b",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.white_b_dial.set(self.color_change_dict["white"][5])
        self.white_b_dial.grid(row=0, column=2)

        self.black_r_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Black_r",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.black_r_dial.set(self.color_change_dict["black"][3])
        self.black_r_dial.grid(row=1, column=0)

        self.black_g_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Black_g",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.black_g_dial.set(self.color_change_dict["black"][4])
        self.black_g_dial.grid(row=1, column=1)

        self.black_b_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Black_b",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.black_b_dial.set(self.color_change_dict["black"][5])
        self.black_b_dial.grid(row=1, column=2)

        self.red_r_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Red_r",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.red_r_dial.set(self.color_change_dict["red"][3])
        self.red_r_dial.grid(row=2, column=0)

        self.red_g_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Red_g",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.red_g_dial.set(self.color_change_dict["red"][4])
        self.red_g_dial.grid(row=2, column=1)

        self.red_b_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Red_b",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.red_b_dial.set(self.color_change_dict["red"][5])
        self.red_b_dial.grid(row=2, column=2)

        self.mud_r_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Mud_r",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.mud_r_dial.set(self.color_change_dict["mud"][3])
        self.mud_r_dial.grid(row=3, column=0)

        self.mud_g_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Mud_g",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.mud_g_dial.set(self.color_change_dict["mud"][4])
        self.mud_g_dial.grid(row=3, column=1)

        self.mud_b_dial = tk.Scale(
            self.root,
            from_=-255, to=255,
            orient=tk.HORIZONTAL,
            label="Mud_b",
            command=apply_color_change_adapter,
            length=dial_length, width=dial_width,
            sliderlength=slider_length
        )
        self.mud_b_dial.set(self.color_change_dict["mud"][5])
        self.mud_b_dial.grid(row=3, column=2)
        # apply_color_change()

        # Create the buttons
        self.white_r_decrement_btn = tk.Button(self.root, text="White_r-", command=self.decrement_white_r)
        self.white_r_decrement_btn.grid(row=0, column=3)

        self.white_r_increment_btn = tk.Button(self.root, text="White_r+", command=self.increment_white_r)
        self.white_r_increment_btn.grid(row=0, column=4)


        self.white_g_decrement_btn = tk.Button(self.root, text="white_g-", command=self.decrement_white_g)
        self.white_g_decrement_btn.grid(row=0, column=5)

        self.white_g_increment_btn = tk.Button(self.root, text="white_g+", command=self.increment_white_g)
        self.white_g_increment_btn.grid(row=0, column=6)

        self.white_b_decrement_btn = tk.Button(self.root, text="white_b-", command=self.decrement_white_b)
        self.white_b_decrement_btn.grid(row=0, column=7)

        self.white_b_increment_btn = tk.Button(self.root, text="white_b+", command=self.increment_white_b)
        self.white_b_increment_btn.grid(row=0, column=8)


        self.black_r_decrement_btn = tk.Button(self.root, text="black_r-", command=self.decrement_black_r)
        self.black_r_decrement_btn.grid(row=1, column=3)

        self.black_r_increment_btn = tk.Button(self.root, text="black_r+", command=self.increment_black_r)
        self.black_r_increment_btn.grid(row=1, column=4)


        self.black_g_decrement_btn = tk.Button(self.root, text="black_g-", command=self.decrement_black_g)
        self.black_g_decrement_btn.grid(row=1, column=5)

        self.black_g_increment_btn = tk.Button(self.root, text="black_g+", command=self.increment_black_g)
        self.black_g_increment_btn.grid(row=1, column=6)

        self.black_b_decrement_btn = tk.Button(self.root, text="black_b-", command=self.decrement_black_b)
        self.black_b_decrement_btn.grid(row=1, column=7)

        self.black_b_increment_btn = tk.Button(self.root, text="black_b+", command=self.increment_black_b)
        self.black_b_increment_btn.grid(row=1, column=8)


        self.red_r_decrement_btn = tk.Button(self.root, text="red_r-", command=self.decrement_red_r)
        self.red_r_decrement_btn.grid(row=2, column=3)

        self.red_r_increment_btn = tk.Button(self.root, text="red_r+", command=self.increment_red_r)
        self.red_r_increment_btn.grid(row=2, column=4)


        self.red_g_decrement_btn = tk.Button(self.root, text="red_g-", command=self.decrement_red_g)
        self.red_g_decrement_btn.grid(row=2, column=5)

        self.red_g_increment_btn = tk.Button(self.root, text="red_g+", command=self.increment_red_g)
        self.red_g_increment_btn.grid(row=2, column=6)

        self.red_b_decrement_btn = tk.Button(self.root, text="red_b-", command=self.decrement_red_b)
        self.red_b_decrement_btn.grid(row=2, column=7)

        self.red_b_increment_btn = tk.Button(self.root, text="red_b+", command=self.increment_red_b)
        self.red_b_increment_btn.grid(row=2, column=8)


        self.mud_r_decrement_btn = tk.Button(self.root, text="mud_r-", command=self.decrement_mud_r)
        self.mud_r_decrement_btn.grid(row=3, column=3)

        self.mud_r_increment_btn = tk.Button(self.root, text="mud_r+", command=self.increment_mud_r)
        self.mud_r_increment_btn.grid(row=3, column=4)


        self.mud_g_decrement_btn = tk.Button(self.root, text="mud_g-", command=self.decrement_mud_g)
        self.mud_g_decrement_btn.grid(row=3, column=5)

        self.mud_g_increment_btn = tk.Button(self.root, text="mud_g+", command=self.increment_mud_g)
        self.mud_g_increment_btn.grid(row=3, column=6)

        self.mud_b_decrement_btn = tk.Button(self.root, text="mud_b-", command=self.decrement_mud_b)
        self.mud_b_decrement_btn.grid(row=3, column=7)

        self.mud_b_increment_btn = tk.Button(self.root, text="mud_b+", command=self.increment_mud_b)
        self.mud_b_increment_btn.grid(row=3, column=8)


    # All Inclrement Decrement Buttons Methods
    def increment_white_r(self):
        increment_amount = 5
        self.white_r_dial.set(self.white_r_dial.get() + increment_amount)
        apply_color_change()

    def decrement_white_r(self):
        decrement_amount = 5
        self.white_r_dial.set(self.white_r_dial.get() + decrement_amount)
        apply_color_change()

    def increment_white_g(self):
        increment_amount = 5
        self.white_g_dial.set(self.white_g_dial.get() + increment_amount)
        apply_color_change()

    def decrement_white_g(self):
        decrement_amount = 5
        self.white_g_dial.set(self.white_g_dial.get() + decrement_amount)
        apply_color_change()

    def increment_white_b(self):
        increment_amount = 5
        self.white_b_dial.set(self.white_b_dial.get() + increment_amount)
        apply_color_change()

    def decrement_white_b(self):
        decrement_amount = 5
        self.white_b_dial.set(self.white_b_dial.get() + decrement_amount)
        apply_color_change()


    def increment_black_r(self):
        increment_amount = 5
        self.black_r_dial.set(self.black_r_dial.get() + increment_amount)
        apply_color_change()

    def decrement_black_r(self):
        decrement_amount = 5
        self.black_r_dial.set(self.black_r_dial.get() + decrement_amount)
        apply_color_change()

    def increment_black_g(self):
        increment_amount = 5
        self.black_g_dial.set(self.black_g_dial.get() + increment_amount)
        apply_color_change()

    def decrement_black_g(self):
        decrement_amount = 5
        self.black_g_dial.set(self.black_g_dial.get() + decrement_amount)
        apply_color_change()

    def increment_black_b(self):
        increment_amount = 5
        self.black_b_dial.set(self.black_b_dial.get() + increment_amount)
        apply_color_change()

    def decrement_black_b(self):
        decrement_amount = 5
        self.black_b_dial.set(self.black_b_dial.get() + decrement_amount)
        apply_color_change()


    def increment_red_r(self):
        increment_amount = 5
        self.red_r_dial.set(self.red_r_dial.get() + increment_amount)
        apply_color_change()

    def decrement_red_r(self):
        decrement_amount = 5
        self.red_r_dial.set(self.red_r_dial.get() + decrement_amount)
        apply_color_change()

    def increment_red_g(self):
        increment_amount = 5
        self.red_g_dial.set(self.red_g_dial.get() + increment_amount)
        apply_color_change()

    def decrement_red_g(self):
        decrement_amount = 5
        self.red_g_dial.set(self.red_g_dial.get() + decrement_amount)
        apply_color_change()

    def increment_red_b(self):
        increment_amount = 5
        self.red_b_dial.set(self.red_b_dial.get() + increment_amount)
        apply_color_change()

    def decrement_red_b(self):
        decrement_amount = 5
        self.red_b_dial.set(self.red_b_dial.get() + decrement_amount)
        apply_color_change()

    def increment_mud_r(self):
        increment_amount = 5
        self.mud_r_dial.set(self.mud_r_dial.get() + increment_amount)
        apply_color_change()

    def decrement_mud_r(self):
        decrement_amount = 5
        self.mud_r_dial.set(self.mud_r_dial.get() + decrement_amount)
        apply_color_change()

    def increment_mud_g(self):
        increment_amount = 5
        self.mud_g_dial.set(self.mud_g_dial.get() + increment_amount)
        apply_color_change()

    def decrement_mud_g(self):
        decrement_amount = 5
        self.mud_g_dial.set(self.mud_g_dial.get() + decrement_amount)
        apply_color_change()

    def increment_mud_b(self):
        increment_amount = 5
        self.mud_b_dial.set(self.mud_b_dial.get() + increment_amount)
        apply_color_change()

    def decrement_mud_b(self):
        decrement_amount = 5
        self.mud_b_dial.set(self.mud_b_dial.get() + decrement_amount)
        apply_color_change()



def apply_color_change_adapter(temp):
    apply_color_change()

def apply_color_change():

    def remove_grid_and_invert(image_path):
        remove_grid_dict = {
            '"#0A0D18"': '"RGB(0, 0, 0)"',
        }

        def recolor_one_image(image_path):
            for original, desired in remove_grid_dict.items():
                target_path = '/home/caffeinemachine/Desktop/1Processing/TK/mod.png'
                remove_grid_command = f'convert {image_path} -fill {desired} -fuzz 15% -opaque {original} {target_path}'
                invert_command = f'convert {image_path} -negate {target_path}'
                os.system(remove_grid_command)
                os.system(invert_command)

        recolor_one_image(image_path)

    remove_grid_and_invert('/home/caffeinemachine/Desktop/1Processing/TK/2.png')


def main():
    root = tk.Tk()
    root.title("Interactive Color Change")
    app = ColorChangeApp(root)
    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
