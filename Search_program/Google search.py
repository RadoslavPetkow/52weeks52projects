import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from tkinterweb import HtmlFrame

search_results = []
current_page = 1
results_per_page = 10

def get_title_description(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No Title'
        desc_tag = soup.find('meta', attrs={'name': 'description'}) or soup.find('meta', attrs={'name': 'Description'})
        description = desc_tag['content'].strip() if desc_tag else 'No Description'
        return title, description
    except Exception:
        return 'No Title', 'No Description'

def perform_search(*args):
    global search_results, current_page
    query = search_entry.get()
    if not query.strip():
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return
    try:
        for widget in results_frame.winfo_children():
            widget.destroy()
        current_page = 1
        search_results = []
        for idx, url in enumerate(search(query, num_results=20)):
            title, description = get_title_description(url)
            search_results.append({'title': title, 'url': url, 'description': description})
        display_results(current_page)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_results(page_number):
    for widget in results_frame.winfo_children():
        widget.destroy()
    start_idx = (page_number - 1) * results_per_page
    end_idx = start_idx + results_per_page
    for result in search_results[start_idx:end_idx]:
        rframe = ttk.Frame(results_frame, padding=(5, 5))
        rframe.pack(fill=tk.X, pady=3)
        title_label = ttk.Label(rframe, text=result['title'], style="Title.TLabel", cursor="hand2", wraplength=400, anchor="w")
        title_label.pack(fill=tk.X)
        title_label.bind("<Button-1>", lambda e, u=result['url']: open_webpage(u))
        title_label.bind("<Enter>", lambda e: e.widget.configure(style="HoverTitle.TLabel"))
        title_label.bind("<Leave>", lambda e: e.widget.configure(style="Title.TLabel"))
        url_label = ttk.Label(rframe, text=result['url'], style="Url.TLabel", cursor="hand2", wraplength=400, anchor="w")
        url_label.pack(fill=tk.X)
        url_label.bind("<Button-1>", lambda e, u=result['url']: open_webpage(u))
        url_label.bind("<Enter>", lambda e: e.widget.configure(style="HoverUrl.TLabel"))
        url_label.bind("<Leave>", lambda e: e.widget.configure(style="Url.TLabel"))
        desc_label = ttk.Label(rframe, text=result['description'], style="Description.TLabel", wraplength=400, anchor="w")
        desc_label.pack(fill=tk.X, pady=(3, 0))
    update_pagination_buttons()

def update_pagination_buttons():
    total_pages = (len(search_results) + results_per_page - 1) // results_per_page
    prev_button.config(state=tk.DISABLED if current_page <= 1 else tk.NORMAL)
    next_button.config(state=tk.DISABLED if current_page >= total_pages else tk.NORMAL)

def next_page():
    global current_page
    current_page += 1
    display_results(current_page)

def prev_page():
    global current_page
    current_page -= 1
    display_results(current_page)

def open_webpage(url):
    for widget in results_frame.winfo_children():
        widget.destroy()
    frame = HtmlFrame(results_frame, horizontal_scrollbar="auto")
    frame.pack(fill="both", expand=True)
    frame.load_website(url)
    back_button = ttk.Button(results_frame, text="Back to Search Results", command=lambda: display_results(current_page))
    back_button.pack(pady=5)

app = tk.Tk()
app.title("Modern Search Engine")
app.geometry("500x500")
app.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("Title.TLabel", foreground="#1a0dab", font=("Arial", 11, "bold"), background="#ffffff")
style.configure("HoverTitle.TLabel", foreground="#d14836", font=("Arial", 11, "bold"), background="#ffffff")
style.configure("Url.TLabel", foreground="#006621", font=("Arial", 9), background="#ffffff")
style.configure("HoverUrl.TLabel", foreground="#0b0080", font=("Arial", 9), background="#ffffff")
style.configure("Description.TLabel", foreground="#4d5156", font=("Arial", 10), background="#ffffff")
style.configure("TLabel", background="#f0f0f0")

header_frame = ttk.Frame(app, padding=(5, 5))
header_frame.pack(fill=tk.X)
search_entry = ttk.Entry(header_frame, font=("Arial", 10), width=35)
search_entry.pack(side=tk.LEFT, padx=(0, 5))
search_entry.bind("<Return>", perform_search)
search_button = ttk.Button(header_frame, text="Search", command=perform_search)
search_button.pack(side=tk.LEFT)

results_frame = ttk.Frame(app)
results_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

pagination_frame = ttk.Frame(app, padding=(5, 5))
pagination_frame.pack(fill=tk.X)
prev_button = ttk.Button(pagination_frame, text="Previous", command=prev_page)
prev_button.pack(side=tk.LEFT, padx=5)
prev_button.config(state=tk.DISABLED)
next_button = ttk.Button(pagination_frame, text="Next", command=next_page)
next_button.pack(side=tk.RIGHT, padx=5)
next_button.config(state=tk.DISABLED)

app.mainloop()
