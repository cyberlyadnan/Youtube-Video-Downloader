import time
import webbrowser
from tkinter import filedialog
import re

import customtkinter
from PIL import Image, ImageTk
from pytube import YouTube

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.data= ["Yt Download"]
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        # configure window
        self.title("Yt Downloader")
        self.geometry(f"{900}x{450}")

        def go():
            time.sleep(1)


            self.loading_label.configure(text="Loading...")
            # time.sleep(1)
            yt = YouTube(self.entry1.get())
            self.entry2.configure(state="normal")
            self.entry2.insert(0, f"")
            self.entry2.insert(0, f"{yt.title}")
            self.entry2.configure(state="disabled")
            videos = yt.streams.filter(type="video")
            if self.seg_button_1.get() == "Thumbnail":
                self.loading_label.configure(text="Now Press Download")
            elif self.seg_button_1.get() == "Video":
                self.data.clear()
                videos = yt.streams.filter(type="video")

            elif self.seg_button_1.get() == "Audio":
                self.data.clear()
                videos = yt.streams.filter(only_audio=True)

            self.data.clear()

            x=0
            for rest in videos:
                print(rest)
                self.data.append(f"{x}. {rest.resolution}/{rest.mime_type}")
                x+=1

            # self.optionmenu_1["value"] = self.data
            self.optionmenu_1.configure(values=self.data)
            self.optionmenu_1.set(self.data[0])
            self.loading_label.configure(text="")
            # self.progressbar_1.destroy()


        def download():
            # fln = filedialog.asksaveasfilename(title="Save File", filetypes=())
            fln = filedialog.askdirectory(title="Save File")
            # fln = fielddialog.
            yt = YouTube(self.entry1.get())
            if self.seg_button_1.get() == "Thumbnail":
                webbrowser.open_new_tab(yt.thumbnail_url)

            elif self.seg_button_1.get() == "Video":
                # self.data.clear()
                videos = yt.streams.filter(type="video")
                str1 = self.optionmenu_1.get()[0:2]
                value = list(map(int, re.findall('\d+', str1)))
                videos[value[0]].download(fln)
                self.optionmenu_1.configure(values=self.data)
                self.optionmenu_1.set(self.data[0])
                print("success")

            elif self.seg_button_1.get() == "Audio":
                # self.data.clear()
                videos = yt.streams.filter(only_audio=True)
                str1 = self.optionmenu_1.get()[0:2]
                value= list(map(int, re.findall('\d+', str1)))
                videos[value[0]].download(fln)
                self.optionmenu_1.configure(values=self.data)
                self.optionmenu_1.set(self.data[0])
                print("success")
        # self.frame_sidebar= customtkinter.CTkFrame(self)
        # self.frame_sidebar.grid(column=0, row=0)


        # create sidebar frame with widgets
        self.sidebar_frame_left = customtkinter.CTkFrame(self, width=200, corner_radius=1)
        self.sidebar_frame_left.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame_left.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame_left, text="Yt Downloader",
                                                 font=customtkinter.CTkFont(size=22, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 0))

        # img = tkinter.PhotoImage(file="yt.png")
        img = customtkinter.CTkImage(Image.open("yt.png"), size=(120, 80))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame_left, text="", image=img)
        self.logo_label.grid(row=1, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame_left, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame_left,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(0, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame_left, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame_left,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(0, 20))

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, )
        self.slider_progressbar_frame.grid(row=0, column=1, rowspan=8, columnspan=2, padx=(10, 10), pady=(10, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(8, weight=1)

        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame,values=["Thumbnail", "Video", "Audio"])
        self.seg_button_1.grid(row=0, column=0, padx=(5, 10), pady=(10, 10), sticky="ew")
        self.seg_button_1.set("Video")
        self.seg_button_1.configure(font=customtkinter.CTkFont(size=16, weight="bold"))

        self.url_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Url :", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.url_label.grid(column=0, row=1, sticky="w", padx=(20, 10), pady=(15, 10))

        # self.url_text= StringVar()
        self.entry1 = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Enter Your Url....")
        self.entry1.grid( column=0, row=1, columnspan=2, padx=(60, 20), pady=(15, 10), sticky="nsew")

        self.go_button = customtkinter.CTkButton(self.slider_progressbar_frame, text="Go", bg_color="transparent", cursor="hand2", font=customtkinter.CTkFont(size=16, weight="bold"), command=go)
        self.go_button.grid(column=0, row=2,  padx=60, pady=(0, 10))

        self.loading_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="...", anchor="w")
        self.loading_label.grid(row=3, column=0, padx=20, pady=(10, 0))



        self.title_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Video Title :",
                                                font=customtkinter.CTkFont(size=16, weight="bold"))
        self.title_label.grid(column=0, row=6, sticky="w", padx=(20, 10), pady=(50, 10))

        self.entry2 = customtkinter.CTkEntry(self.slider_progressbar_frame,state="disabled", placeholder_text="Your Video Title...")
        self.entry2.grid(column=0, row=6, columnspan=2, padx=(130, 20), pady=(50, 10), sticky="nsew")

        self.resolution_label = customtkinter.CTkLabel(self.slider_progressbar_frame, text="Select Resolution: ",
                                                  font=customtkinter.CTkFont(size=16, weight="bold"))
        self.resolution_label.grid(column=0, row=7, sticky="w", padx=(20, 10), pady=(30, 10))

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.slider_progressbar_frame, dynamic_resizing=True,
                                                        values=self.data)
        self.optionmenu_1.grid(row=7, column=0, padx=(200, 20), pady=(30, 10), sticky="w")

        self.download_button = customtkinter.CTkButton(self.slider_progressbar_frame, text="Download", bg_color="transparent",
                                                 cursor="hand2", font=customtkinter.CTkFont(size=20, weight="bold"),
                                                 command=download)
        self.download_button.grid(column=0, row=8, padx=60, pady=(0, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)



if __name__ == "__main__":
    app = App()
    app.mainloop()