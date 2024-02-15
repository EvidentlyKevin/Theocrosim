import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import simpledialog, messagebox

def set_fullscreen(window, fullscreen=True):
    window.attributes("-fullscreen", fullscreen)

def set_popout_window(window, size="800x600"):
    window.geometry(size)

def user_preference_window(root):
    # Exit fullscreen for the dialog
    set_fullscreen(root, fullscreen=False)

    # Temporarily set the dialog font larger
    root.option_add("*Dialog.msg.font", "Helvetica 14")
    user_choice = simpledialog.askstring("Screen Mode", "Enter 'fullscreen' or 'popout':", parent=root)
    
    # Reset the default font to normal
    root.option_add("*Dialog.msg.font", "TkDefaultFont")

    # Re-enable fullscreen based on user choice later in the main function
    return user_choice

def display_title_screen(window, title_art, intro_text):
    # Display title art in a label
    title_label = tk.Label(window, text=title_art, font=("Courier", 12), justify="left")
    title_label.pack()

    # Display intro text in a scrolled text area
    intro_text_area = scrolledtext.ScrolledText(window, width=120, height=15, wrap=tk.WORD)
    intro_text_area.insert(tk.INSERT, intro_text)
    intro_text_area.configure(state='disabled')  # Make the text area read-only
    intro_text_area.pack(pady=20)

    # Button to continue, simulating "Press ENTER to continue..."
    continue_button = tk.Button(window, text="Begin your divine journey...", command=lambda: on_continue(window))
    continue_button.pack(padx=10, pady=10)

def on_continue(window):
    # Placeholder for what happens when user chooses to continue
    messagebox.showinfo("Initializing", "Initializing game...")
    window.destroy()  # This closes the window, you might want to replace this with the actual game initialization

def main():
    window = tk.Tk()
    window.title("THEOCROSIM")


    # Initially set the window to fullscreen for the dialog
    set_fullscreen(window)


    # Get user preference without starting in fullscreen to avoid issues with the dialog
    user_choice = user_preference_window(window)

    if user_choice and user_choice.lower() == 'fullscreen':
        set_fullscreen(window)
    elif user_choice and user_choice.lower() == 'popout':
        set_popout_window(window)
    else:
        messagebox.showerror("Invalid Input", "Invalid choice or no choice made. Defaulting to popout window.")
        set_popout_window(window)

    title_art = """

████████╗██╗  ██╗███████╗ ██████╗  ██████╗██████╗  ██████╗ ███████╗██╗███╗   ███╗
╚══██╔══╝██║  ██║██╔════╝██╔═══██╗██╔════╝██╔══██╗██╔═══██╗██╔════╝██║████╗ ████║
   ██║   ███████║█████╗  ██║   ██║██║     ██████╔╝██║   ██║███████╗██║██╔████╔██║
   ██║   ██╔══██║██╔══╝  ██║   ██║██║     ██╔══██╗██║   ██║╚════██║██║██║╚██╔╝██║
   ██║   ██║  ██║███████╗╚██████╔╝╚██████╗██║  ██║╚██████╔╝███████║██║██║ ╚═╝ ██║
   ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝╚═╝     ╚═╝
                                                                                 
"""
    intro_text = """

Welcome to THEOCROSIM, a text-based simulation where divinity and strategy intertwine. 
In this world, you ascend to the role of a deity, crafting your own religion to guide and influence 
the civilizations within the simulation. Your divine touch shapes the fate of entire countries, 
balancing their fear, faith, prosperity, and awareness of the greater powers that be.

As the creator of all, you must navigate the complexities of divine governance, responding to the 
prayers, fears, and aspirations of your followers. But beware, for the people within your simulation 
grow increasingly aware of their reality, challenging your omnipotence with their burgeoning 
meta-awareness.

Your decisions echo through the ages. Will you lead your followers into a new era of enlightenment, 
or will the seeds of heresy undermine your divine authority? Fate awaits you.

"""

    display_title_screen(window, title_art, intro_text)

    window.mainloop()

if __name__ == "__main__":
    main()
