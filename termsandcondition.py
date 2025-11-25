from tkinter import *


root=Tk()
root.title("Terms and Condition")

frame=Frame(root)
frame.pack()

def agreeandcontinue():
    root.destroy();

txt=Text(frame)
txt.pack(side=LEFT, padx=20,pady=10)
txt.tag_configure("bold",font=("Arial",12,"bold"))

scroll = Scrollbar(frame, command=txt.yview)
scroll.pack(side=RIGHT, fill=Y)

txt.config(yscrollcommand=scroll.set)

terms = """

1. Acceptance of Terms
By using this application, you agree to comply with and be bound by these terms.

2. Use of Application
You may use this application for personal and non-commercial purposes only. 
Unauthorized use, reproduction, or distribution is prohibited.

3. Privacy
We respect your privacy. Any data you provide will be handled responsibly 
and will not be shared without your consent.

4. Limitation of Liability
This application is provided "as is" without warranties of any kind. 
We are not liable for any damages arising from its use.

5. Changes to Terms
We reserve the right to update or modify these terms at any time. 
Continued use of the application constitutes acceptance of the revised terms.

6. Contact
For questions regarding these terms, please contact the developer.
"""

txt.insert(END,"Terms and conditions\n","bold")
txt.insert(END, terms)

extended_terms="""
7. Intellectual Property
All content, design, and code within this application are the property of the developer. 
You may not copy, modify, or distribute any part of the application without prior written consent.

8. User Responsibilities
You agree not to misuse the application, attempt unauthorized access, or interfere with its functionality. 
Any misuse may result in termination of your access.

9. Data Security
While we take reasonable measures to protect your information, you acknowledge that no system is completely secure. 
You are responsible for maintaining the confidentiality of your login credentials.

10. Governing Law
These terms shall be governed by and interpreted in accordance with the laws of your jurisdiction. 
Any disputes will be resolved in the courts of that jurisdiction.

11. Termination
We reserve the right to suspend or terminate your access to the application at our discretion, 
without prior notice, if you violate these terms.

12. Entire Agreement
These terms constitute the entire agreement between you and the developer regarding the use of this application 
and supersede any prior agreements or understandings."""

txt.insert(END, extended_terms)
txt.configure(state= DISABLED)

Int=IntVar()
chbx=Checkbutton(root,text="Agree and Continue",variable=Int, anchor="center",command=agreeandcontinue,font=("bold"))
chbx.pack(pady=10)

root.resizable(False, False)

root.mainloop()