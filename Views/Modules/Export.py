import  customtkinter
from typing import Any
from globals import instances as global_instances


class Export:

    def __init__(
            self,
            master: Any
    ):

        self.master = master
        self.general_frame = customtkinter.CTkFrame(self.master)

        export_text_area = customtkinter.CTkTextbox(self.general_frame)
        export_text_area.pack(padx=2, pady=2, fill='both', expand=True)

        self.sidebar_frame = customtkinter.CTkFrame(global_instances.sidebar)

        pass

    def show_ui(self):
        self.general_frame.pack(padx=2, pady=2, fill='both', expand=True)
        self.sidebar_frame.pack(padx=2, pady=2, fill='both', expand=True)

    def hide(self):
        self.general_frame.pack_forget()
        self.sidebar_frame.pack_forget()


