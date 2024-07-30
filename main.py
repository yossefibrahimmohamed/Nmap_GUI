import customtkinter
import nmap

nmap_page = customtkinter.CTk()
nmap_page.geometry('400x400')
nmap_page.resizable(False, False)
nmap_page.iconbitmap("D:\\My Projects\\Python Project\\Nmap_GUI\img\\Nmap.ico")
nmap_page.title(" Nmap By Yossef Ibrahim ")

def result():
    nmap_page.update()
    # name of Frame
    result_page = customtkinter.CTk()
    # size you make it
    result_page.geometry('300x400')
    # this is a random
    result_page.overrideredirect(True)

    # Initialize the Nmap PortScanner
    nm = nmap.PortScanner()
    # Define the IP address and scan arguments
    ip_address = ip_add.get()
    scan_arguments = '-sV'  # Ping scan, change as needed for your scan type
    nm.scan(ip_address, arguments=scan_arguments)

    # Print scan results
    customtkinter.CTkLabel(master=result_page, text="-----------------------------").pack()

    customtkinter.CTkLabel(master=result_page, text=f"Scan report for {ip_address}").pack()
    for host in nm.all_hosts():
        customtkinter.CTkLabel(master=result_page, text=f"Host : {host} ({nm[host].hostname()})").pack()
        customtkinter.CTkLabel(master=result_page, text=f"State : {nm[host].state()}").pack()
        for proto in nm[host].all_protocols():
            customtkinter.CTkLabel(master=result_page, text=f"----------\nProtocol : {proto}").pack()
            lport = nm[host][proto].keys()
            for port in lport:
                customtkinter.CTkLabel(master=result_page,
                                       text=f"port : {port}\tstate : {nm[host][proto][port]['state']}").pack()
    exit_btn = customtkinter.CTkButton(master=result_page, text='Close', width=100, border_width=0, text_color='black'
                                       , fg_color='#4CC2FF', hover_color='#48B2E9', command=result_page.destroy)
    exit_btn.place(relx=0.1, rely=0.9)
    result_page.mainloop()


customtkinter.CTkLabel(master=nmap_page, text='Nmap', font=customtkinter.CTkFont('Bold', 20)).place(relx=0.1, rely=0.1)
ip_add = customtkinter.CTkEntry(master=nmap_page, placeholder_text=" Enter Ip", width=200, corner_radius=2)
ip_add.place(relx=0.1, rely=0.3)
btn_results = customtkinter.CTkButton(master=nmap_page, text='Find', width=100, border_width=0, text_color='black',
                                      fg_color='#4CC2FF', hover_color='#48B2E9', command=result)
btn_results.place(relx=0.1, rely=0.5)

# Run the scan

nmap_page.mainloop()
