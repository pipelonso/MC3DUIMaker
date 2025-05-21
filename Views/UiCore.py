import customtkinter
from globals import instances as global_instances
from Views.Modules.UiComposer import UIComposer
from Views.Modules.Export import Export as ExportModule


class UICore:

    def __init__(self):

        self.app = customtkinter.CTk()
        self.app.geometry('1000x600')
        customtkinter.set_appearance_mode('dark')
        self.general_frame = customtkinter.CTkFrame(self.app)
        self.general_frame.pack(padx=2, pady=2, fill='both', expand=True)

        solid_tabs_frame = customtkinter.CTkFrame(self.general_frame)
        solid_tabs_frame.pack(padx=2, pady=2, fill='x')

        ui_make_label = customtkinter.CTkLabel(solid_tabs_frame, text='3d UI Maker')
        ui_make_label.pack(padx=5, pady=2, fill='x', side=customtkinter.LEFT)

        code_export_tab_button = customtkinter.CTkButton(
            solid_tabs_frame, text='Export',
            corner_radius=0,
            command=lambda: self.show_export_module()
        )
        code_export_tab_button.pack(padx=0, pady=2, fill='x', side=customtkinter.RIGHT)

        image_inspector_tab_button = customtkinter.CTkButton(
            solid_tabs_frame, text='UI Editor',
            corner_radius=0,
            command=lambda: self.show_ui_composer()
        )
        image_inspector_tab_button.pack(padx=0, pady=2, fill='x', side=customtkinter.RIGHT)

        general_content_frame = customtkinter.CTkFrame(self.general_frame)
        general_content_frame.pack(padx=2, pady=2, fill='both', expand=True)

        self.sidebar = customtkinter.CTkFrame(general_content_frame)
        self.sidebar.pack(padx=2, pady=2, fill='y', side=customtkinter.LEFT)

        self.module_frame = customtkinter.CTkFrame(general_content_frame)
        self.module_frame.pack(padx=2, pady=2, fill='both', expand=True, side=customtkinter.RIGHT)

        global_instances.sidebar = self.sidebar
        global_instances.general_frame = self.general_frame
        global_instances.modular_frame = self.module_frame

        self.ui_composer = UIComposer(self.module_frame)
        self.ui_composer.show_ui()

        self.export_module = ExportModule(self.module_frame)

        self.app.mainloop()

    def unpack_all_modules(self):
        self.ui_composer.hide()
        self.export_module.hide()
        pass

    def show_ui_composer(self):
        self.unpack_all_modules()
        self.ui_composer.show_ui()
        pass

    def show_export_module(self):
        self.unpack_all_modules()
        self.export_module.show_ui()
        pass