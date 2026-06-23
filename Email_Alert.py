import requests
import smtplib
import time
from email.message import EmailMessage
from datetime import datetime


# -------------------------
# Email Alert Function
# -------------------------
def send_email(site):

    msg = EmailMessage()

    msg["Subject"] = "Website DOWN Alert"
    msg["From"] = "kusalsanjula@gmail.com"
    msg["To"] = "senujathisumekanayake@gmail.com"


    msg.set_content(
        f"""
ALERT!

Website is DOWN


hutto site eka watila tiyenne balapaaaaan............

Website: {site}
Time: {datetime.now()}

Please check immediately.
"""
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                "kusalsanjula040@gmail.com",
                "zrbk cfmk jbix ewwc"
            )

            smtp.send_message(msg)

        print(f"Email sent for {site}")

    except Exception as e:
        print("Email Error:", e)


# -------------------------
# Website Input
# -------------------------
websites = []

print("Enter websites (type 'exit' to stop)")

while True:

    site = input("Website: ")

    if site.lower() == "exit":
        break

    websites.append(site)


# -------------------------
# Monitoring Loop
# -------------------------
print("\nStarting Monitoring...\n")

while True:

    print("=" * 50)
    print("Check Time:", datetime.now())
    print("=" * 50)

    with open("website_logs.txt", "a") as file:

        file.write("\n")
        file.write("=" * 50 + "\n")
        file.write(f"Check Time: {datetime.now()}\n")
        file.write("=" * 50 + "\n")

        for site in websites:

            try:

                response = requests.get(
                    site,
                    timeout=5
                )

                if response.status_code == 200:

                    status = "UP"

                    print(
                        f"{site} ---> UP"
                    )


                else:

                    status = "DOWN"

                    print(
                        f"{site} ---> DOWN"
                    )

                    send_email(site)

            except Exception:

                status = "DOWN"

                print(
                    f"{site} ---> DOWN"
                )

                send_email(site)

            file.write(
                f"{site} ---> {status}\n"
            )

    print("\nWaiting 60 seconds...\n")

    time.sleep(60)