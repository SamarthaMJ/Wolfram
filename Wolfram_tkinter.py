import tkinter as tk
import wolframalpha
import keyboard


# Function to query Wolfram Alpha
def get_wolfram_alpha_answer():
    question = question_entry.get()
    if question:
        try:
            # Replace 'YOUR_WOLFRAM_ALPHA_APP_ID' with your actual Wolfram Alpha App ID
            app_id = 'ERT5E3-4HPGR2XXH8'
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            answer_label.config(text="Answer: " + answer)
        except Exception as e:
            answer_label.config(text="Error: " + str(e))
    else:
        answer_label.config(text="Please enter a question.")


# Function to close the application
def close_app():
    root.destroy()

# Create the main Tkinter window
root = tk.Tk()
root.title("Wolfram Alpha Question Answerer")

# Create input field for the question
question_entry = tk.Entry(root, width=50)
question_entry.pack(pady=10)

# Create a button to get the answer
get_answer_button = tk.Button(root, text="Get Answer", command=get_wolfram_alpha_answer)
get_answer_button.pack()

# Create a label to display the answer
answer_label = tk.Label(root, text="", wraplength=400)
answer_label.pack(pady=10)

# Create a button to close the application
close_button = tk.Button(root, text="Close", command=close_app)
close_button.pack()

# Start the Tkinter main loop
root.mainloop()

# Ensure the script exits cleanly on keyboard command 'c'
while True:
    if keyboard.is_pressed('c'):
        break
