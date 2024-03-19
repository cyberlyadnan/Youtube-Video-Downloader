import tkinter
import tkinter.messagebox
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()




        # configure window
        self.title("Yt Downloader")
        self.geometry(f"{900}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Yt Downloader",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))


        # self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,cursor="hand2", text="Video")
        # self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        #
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,cursor="hand2", text="Audio")
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,cursor="hand2", values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20)

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(0,10))

        # create sidebar frame with widgets
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=400,height=400, corner_radius=0, bg_color=("blue", "white"))
        self.sidebar_frame2.grid(row=0, column=1,columnspan=2)
        self.sidebar_frame2.grid_rowconfigure(4, weight=1)
# ????????????????
        # self.url_label = customtkinter.CTkLabel(self.sidebar_frame2, text="URL : ",corner_radius=0, anchor="w")
        # self.url_label.grid(row=0, column=0, padx=(20,10), pady=(0, 0), sticky="w")
        #
        # self.url_entry = customtkinter.CTkEntry(self.sidebar_frame2,width=400, placeholder_text="Enter Your Url")
        # self.url_entry.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
# >>>>>>>>>>>>>>>>>>>>>>>
        # # img = tkinter.PhotoImage(file="/img/download.jpg")
        # # self.sidebar2_button_1 = customtkinter.CTkButton(self.sidebar_frame2,image=img, cursor="hand2", text="Thumbnail")
        # # self.sidebar2_button_1.grid(row=0, column=0, padx=20, pady=10)
        # # ctk.CTkButton(root, image=img).pack(side=LEFT)
        #
        # button_image = customtkinter.CTkImage(Image.open("assets/download.jpg"), size=(260, 200))
        #
        # image_button = customtkinter.CTkButton(master=self.sidebar_frame2, text="", image=button_image)
        # image_button.
        #

        # grid(column=0, row=0, padx=0, pady=0)

        self.tabview = customtkinter.CTkTabview(self.sidebar_frame2, width=700)
        self.tabview.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="n")
        self.tabview.add("Thumbnail")
        self.tabview.add("Video")
        self.tabview.add("Audio")
        self.tabview.tab("Thumbnail").grid_rowconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Video").grid_rowconfigure(0, weight=1)

        #
        tabs = ("Thumbnail")
        self.sidebar_button_1 = customtkinter.CTkButton(master=self.tabview.tab(tabs), cursor="hand2", text="Thumbnail")
        self.sidebar_button_1.grid(row=0, column=0, padx=20, pady=10)
        #





    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()