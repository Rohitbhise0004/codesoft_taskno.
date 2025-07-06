import tkinter as tk

# Chatbot response function using extended if-else logic
def get_response(user_input):
    user_input = user_input.lower()

    if "return" in user_input:
        return "You can return items within 30 days of purchase with a receipt."

    elif "track" in user_input or "order" in user_input:
        return "You can track your order using the link sent to your email."

    elif "payment" in user_input or "pay" in user_input:
        return "We accept credit cards, PayPal, and bank transfers."

    elif "contact" in user_input or "support" in user_input:
        return "You can contact customer support via email or our help center."

    elif "international" in user_input or "shipping" in user_input:
        return "Yes, we offer international shipping at extra cost."

    elif "cancel" in user_input:
        return "To cancel an order, go to your account and select the order to cancel."

    elif "warranty" in user_input:
        return "All products come with a 1-year warranty against manufacturing defects."

    elif "login" in user_input or "account" in user_input:
        return "You can log into your account from the top-right corner of the homepage."

    elif "discount" in user_input or "offer" in user_input:
        return "Discounts are automatically applied during checkout if available."

    elif "delivery time" in user_input or "when will i get" in user_input:
        return "Delivery typically takes 3-5 business days within the country."

    elif "store hours" in user_input or "open" in user_input:
        return "Our stores are open from 9 AM to 9 PM, Monday through Saturday."

    elif "forgot password" in user_input:
        return "Click 'Forgot Password' on the login page to reset your password."

    elif "newsletter" in user_input or "unsubscribe" in user_input:
        return "You can unsubscribe from our newsletter at the bottom of any email."

    else:
        return "Sorry, I don't understand your question. Can you rephrase it?"

# GUI interaction
def send_message():
    user_message = entry.get()
    if user_message.strip() == "":
        return
    chat_log.insert(tk.END, "You: " + user_message + "\n")
    bot_reply = get_response(user_message)
    chat_log.insert(tk.END, "Bot: " + bot_reply + "\n\n")
    entry.delete(0, tk.END)

# GUI window setup
root = tk.Tk()
root.title("Extended FAQ Chatbot")

chat_log = tk.Text(root, height=20, width=60, bg="#f4f4f4")
chat_log.pack(padx=10, pady=10)

frame = tk.Frame(root)
entry = tk.Entry(frame, width=45)
entry.pack(side=tk.LEFT, padx=(0, 10))
send_button = tk.Button(frame, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)
frame.pack(pady=5)

root.mainloop()
