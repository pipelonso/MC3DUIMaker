import customtkinter
from typing import Any
from globals import instances as global_instances


class UIComposer:

    def __init__(
            self,
            master: Any
    ):

        self.master = master
        self.general_frame = customtkinter.CTkFrame(self.master)
        self.sidebar_frame = customtkinter.CTkFrame(global_instances.sidebar)

        self.canvas = customtkinter.CTkCanvas(self.general_frame, cursor='cross')
        self.canvas.pack(padx=2, pady=2, fill='both', expand=True)

        self.canvas.bind('<Motion>', self.mouse_motion_callback)

        pass

    def mouse_motion_callback(self, event):

        pass

    def show_ui(self):
        self.general_frame.pack(padx=2, pady=2, fill='both', expand=True)
        self.sidebar_frame.pack(padx=2, pady=2, fill='both', expand=True)
        pass

    def hide(self):
        self.general_frame.pack_forget()
        self.sidebar_frame.pack_forget()
        pass