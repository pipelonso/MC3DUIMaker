import customtkinter
from typing import Any
from globals import instances as global_instances
from tkinter import filedialog
from PIL import Image, ImageTk
from DataClasses.composerDetection import ComposerDetection


class UIComposer:

    def __init__(
            self,
            master: Any
    ):

        self.master = master
        self.general_frame = customtkinter.CTkFrame(self.master)

        self.sidebar_frame = customtkinter.CTkFrame(global_instances.sidebar)

        self.mouse_pos_label = customtkinter.CTkLabel(self.sidebar_frame, text='', width=200, anchor='w')
        self.mouse_pos_label.pack(padx=2, pady=2, fill='x')

        self.render_ui_image = None
        self.detections_render_lis: list[ComposerDetection] = []

        det = ComposerDetection(2, 2, 100, 100, 'test', 'test')
        self.detections_render_lis.append(det)

        (customtkinter.CTkLabel(self.sidebar_frame, text='Archivo', anchor='w')
         .pack(padx=2, pady=2, fill='x'))

        customtkinter.CTkButton(
            self.sidebar_frame,
            text='📁 Load file',
            command=lambda:self.request_open()
            ).pack(padx=2, pady=2, fill='x')

        (customtkinter.CTkLabel(self.sidebar_frame, text='Components', anchor='w')
         .pack(padx=2, pady=2, fill='x'))

        components_frame = customtkinter.CTkFrame(self.sidebar_frame)
        components_frame.pack(padx=2, pady=2, fill='x')

        add_detection_button = customtkinter.CTkButton(
            components_frame, text='❏ Add detection',
            fg_color=('#424949', '#424949'),
            hover_color='gray',
            text_color=('black', 'white'),
            anchor='w'
        )

        add_detection_button.pack(padx=2, pady=2, fill='x')

        self.mouse_x = 0
        self.mouse_y = 0

        self.canvas = customtkinter.CTkCanvas(self.general_frame, cursor='cross')
        self.canvas.pack(padx=2, pady=2, fill='both', expand=True)

        self.h_scrollbar = customtkinter.CTkScrollbar(self.canvas, orientation='horizontal',
                                                      command=self.canvas.xview)
        self.h_scrollbar.pack(side='bottom', fill='x')

        self.v_scrollbar = customtkinter.CTkScrollbar(self.canvas, orientation='vertical',
                                                      command=self.canvas.yview)
        self.v_scrollbar.pack(side='right', fill='y')

        self.canvas.configure(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)

        self.canvas.bind('<Motion>', self.mouse_motion_callback)

        pass

    def mouse_motion_callback(self, event):

        self.mouse_x = event.x
        self.mouse_y = event.y

        self.mouse_pos_label.configure(text=f"x: {self.mouse_x} | y: {self.mouse_y}")

        pass

    def show_ui(self):
        self.general_frame.pack(padx=2, pady=2, fill='both', expand=True)
        self.sidebar_frame.pack(padx=2, pady=2, fill='both', expand=True)
        pass

    def hide(self):
        self.general_frame.pack_forget()
        self.sidebar_frame.pack_forget()
        pass

    def update_render(self) :

        if self.render_ui_image is not None:
            self.canvas.create_image(0,0, image=self.render_ui_image, anchor='nw')
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        for i in self.detections_render_lis:

            self.canvas.create_rectangle(i.x1, i.y1, i.x2, i.y2, outline='red')

            pass

    def request_open(self):

        path = filedialog.askopenfilename()

        if path.endswith('.ckf3u'):

            pass
        else:
            if path.endswith('.png'):
                image = Image.open(path)
                self.render_ui_image = ImageTk.PhotoImage(image)
                self.update_render()



        pass