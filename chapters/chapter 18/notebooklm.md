# Executive Summary

The primary goal of **Chapter 18: Sending Email and Text Messages** is to teach readers how to automate digital communication. While manually checking and replying to emails is a significant "time sink," Python can be used to send mass personalized notifications, respond to specific triggers, or notify you when a long task is finished. The chapter covers three main methods: the user-friendly **EZGmail** module for Gmail accounts, the standard **SMTP/IMAP** protocols for other providers, and **SMS** (text message) automation via email gateways or the **Twilio** service.

---

# Deep-Dive Content: Communication Automation

## 1. Sending and Receiving Email with the Gmail API

Because Gmail has strict security measures, standard protocols often fail. The author recommends the **EZGmail** module as a simplified way to interact with the official Gmail API.

### 1.1 Installation and Setup

- **Module Installation**: Use the command `pip install --user --upgrade ezgmail` to ensure you have the latest version for interacting with Google's changing services.
- **Enabling the API**: You must enable the API in the Google Developers Console and download a `credentials.json` file.
- **Token Generation**: Running `ezgmail.init()` opens a browser for login. This creates a `token.json` file, which allows your script to access your account without needing your actual password in the code.

### 1.2 Common Operations

- **Sending Email**: A single line can send text or attachments.
    
    ```
    import ezgmail
    ezgmail.send('recipient@example.com', 'Subject', 'Body text', ['file.pdf'])
    ```
    
- **Reading/Searching**: Use `ezgmail.unread()` or `ezgmail.recent()` to get a list of **GmailThread** objects. Each thread contains **GmailMessage** objects with attributes like `subject`, `body`, and `sender`.
- **Attachments**: Call `downloadAllAttachments()` on a message object to save files to your computer.

## 2. Standard Email Protocols (SMTP and IMAP)

For non-Gmail accounts, Python uses the standard protocols that most email clients use.

### 2.1 SMTP: Sending Emails

**SMTP (Simple Mail Transfer Protocol)** is the "sending" protocol.

- **Connection Workflow**:
    1. Create an object: `smtplib.SMTP('domain', port)` (usually port 587).
    2. "Say Hello": Call `ehlo()` to establish the connection.
    3. Encryption: Call `starttls()` to enable security.
    4. Login: Call `login('user', 'pass')`.
- **Example Code**:
    
    ```
    import smtplib
    smtpObj = smtplib.SMTP('smtp.example.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login('my_email@example.com', 'password')
    smtpObj.sendmail('my_email@example.com', 'recipient@example.com', 'Subject: Hi\nBody here.')
    smtpObj.quit()
    ```
    

### 2.2 IMAP: Retrieving Emails

**IMAP (Internet Message Access Protocol)** allows you to retrieve and delete messages.

- **Workflow**: Select a folder (like 'INBOX'), search for specific **UIDs** (unique IDs) using search keys (like 'SINCE', 'FROM', 'UNSEEN'), and then fetch the content.
- **Parsing**: Raw IMAP data is hard to read. Use the `pyzmail` module to turn the data into readable strings.
- **Deleting**: Use `delete_messages([UIDs])` followed by `expunge()` to permanently remove emails.

## 3. Sending Text Messages (SMS)

Automating texts is ideal for immediate notifications while you are away from your computer.

### 3.1 SMS Email Gateways

- Many cell providers have a specific email address (e.g., `number@vtext.com`) that forwards emails to a phone as a text.
- This is free but can be unreliable or delayed.

### 3.2 The Twilio Service

For a more professional and reliable solution, the **Twilio** service provides a Python API.

- **Requirements**: You need an **Account SID**, an **Auth Token**, and a Twilio phone number.
- **Example Code**:
    
    ```
    from twilio.rest import Client
    client = Client('ACxxxx', 'auth_token')
    client.messages.create(body='Hello!', from_='+12345', to='+67890')
    ```
    

---

# ⚠️ Important Warnings & Notes

- **Account Safety**: The author strongly suggests creating a **separate "throwaway" email account** for your scripts. This prevents bugs from accidentally deleting your real inbox or spamming your contacts.
- **Password Security**: **Never** type your password directly into your source code. Use `input()` or command line arguments (`sys.argv`) so the password is only in memory while the script runs.
- **Token Safety**: Treat `token.json` or `token-sheets.pickle` files like passwords. If a hacker gets these, they can access your account even without your password.
- **Handshake Rule**: Always call `ehlo()` immediately after connecting to an SMTP server, or later commands will fail.

---

# 📘 Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**Protocol**|A set of rules that computers use to talk to each other.|بروتوكول / نظام قواعد|
|**Credentials**|Information (like username/password) that proves who you are.|أوراق اعتماد / بيانات دخول|
|**Deduplicate**|To remove repeated or copied code to make it cleaner.|إزالة التكرار|
|**Handshake**|The first message two computers send to start a connection.|مصافحة (رقمية)|
|**Payload**|The actual data or "body" inside an email or message.|الحمولة / البيانات الفعلية|
|**UID**|A "Unique ID" number given to every email in a folder.|معرف فريد|
|**Expunge**|To permanently delete emails that were marked for removal.|شطب / حذف نهائي|
|**Snippet**|A small piece of text, like a short preview of an email.|مقتطف|

---

# Key Takeaways

- Digital communication automation turns your computer into a personal assistant that can notify you of events or handle customer service tasks.
- **EZGmail** is the best choice for Gmail users because it handles complex security automatically.
- Professional scripts use `try/except` blocks with communication functions because internet connections can often fail or time out.
- **Twilio** is the standard way to send high-quality, reliable text messages, though it requires a separate account.
- Using `token.json` files is a "modern" way to log in that keeps your actual account password secret.