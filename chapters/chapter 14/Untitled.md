# Executive Summary

The primary goal of **Chapter 14: Working with Google Sheets** is to introduce students to the **EZSheets** third-party module. While Google Sheets is a popular and free web-based alternative to Excel, its official API is complex and difficult for beginners to use. This chapter teaches how to programmatically create, read, and modify online spreadsheets, automate data entry, and convert between different file formats using simplified Python commands.

---

# Deep-Dive Content: Working with Google Sheets

## 1. Installation and Authentication Setup

Before using Python to talk to Google's servers, you must configure security settings and install the necessary tools.

### 1.1 The EZSheets Module

- **Installation**: You can install the module by running `pip install --user ezsheets` in your terminal.
- **Dependencies**: Installing EZSheets automatically includes other Google API libraries needed for server communication.

### 1.2 Credentials and Tokens

- **Enabling APIs**: Users must visit the Google Developers Console to enable both the **Google Sheets API** and the **Google Drive API**.
- **The Credentials File**: You must download a `credentials.json` file from Google and rename it to `credentials-sheets.json` in your script folder.
- **The Token Files**: The first time you run `import ezsheets`, a browser window opens for you to log in; this generates `token-sheets.pickle` and `token-drive.pickle` files.
- **⚠️ Warning**: You must treat these token and credential files like passwords and never share them.

## 2. Managing Spreadsheet Objects

A **Spreadsheet object** represents an entire file which may contain several individual sheets.

### 2.1 Creating and Opening Spreadsheets

- **New Files**: Use `ezsheets.createSpreadsheet('Title')` to start a blank document.
- **Existing Files**: You can open a sheet using its unique **ID** (found in the URL) or its full URL via `ezsheets.Spreadsheet('ID')`.
- **Example Code**:
    
    ```
    import ezsheets
    ss = ezsheets.createSpreadsheet('My New Sheet')
    print(ss.title) # Output: My New Sheet
    ```
    

### 2.2 Uploading and Downloading

- **Uploading**: The `ezsheets.upload('file.xlsx')` function allows you to turn local Excel or CSV files into Google Sheets.
- **Downloading**: You can save online sheets as Excel (`.xlsx`), PDF, CSV, or HTML using methods like `ss.downloadAsExcel()`.
- **Deleting**: The `ss.delete()` method moves a file to the Google Drive Trash.

## 3. Manipulating Sheet Objects and Data

Within a spreadsheet, you interact with specific **Sheet objects** to handle the actual data in cells.

### 3.1 Accessing Cells

- **Addressing**: Google Sheets uses **1-based** indexing, meaning the first row and column are index 1, not 0.
- **Direct Access**: Cells can be read or written using string addresses like `sheet['A1']` or coordinate tuples like `sheet`.
- **Note on Speed**: Reading is fast because data is cached, but **writing** a single cell requires a web request and can take about a second.

### 3.2 Reading and Writing in Bulk

- **Efficient Updates**: To avoid slow performance, use `getRow()`, `getColumn()`, or `getRows()` to retrieve entire blocks of data at once.
- **Updating**: Correspondingly, `updateRow()` and `updateColumn()` send a whole list of data to the server in a single request.
- **Example Code**:
    
    ```
    sheet = ss
    column_data = sheet.getColumn(1) # Gets all values in column A
    sheet.updateRow(1, ['Name', 'Age', 'City']) # Updates the first row
    ```
    

## 4. Quotas and Limitations

Because Google Sheets is a shared online service, Google restricts how fast you can make changes.

### 4.1 Usage Limits

- **Daily/Timed Quotas**: Free accounts are restricted to 250 new spreadsheets per day and 100 requests every 100 seconds.
- **Handling Errors**: If you exceed your quota, EZSheets will automatically catch the error and retry the request later, which might make your script pause for several seconds.

---

# 📘 Vocabulary Table

|Word/Term|Simple English Definition|Arabic Translation|
|:--|:--|:--|
|**API**|A set of rules that lets one program talk to another.|واجهة برمجة التطبيقات|
|**Credential**|Information that proves who you are to a system.|أوراق اعتماد / هوية|
|**Token**|A digital key that gives a program access to an account.|رمز وصول|
|**Refresh**|To update local data with the latest version from the server.|تحديث البيانات|
|**Quota**|A limit on the number of actions you can take in a time period.|حصة نسبية / حد مسموح|
|**1-based Index**|A system where the first item is number 1 instead of 0.|فهرسة تبدأ من الرقم 1|
|**Binary File**|A complex file containing data like fonts and colors.|ملف ثنائي|

---

# Key Takeaways

- **EZSheets simplifies Google Automation**: It handles the difficult parts of the official Google API so you can focus on data tasks.
- **Security is priority**: You must keep your credentials and token files secret to protect your Google account.
- **Batch processing is faster**: Updating entire rows or columns at once is much more efficient than updating single cells due to network lag.
- **Conversion is built-in**: Python can easily convert Google Sheets into local files like PDFs or Excel spreadsheets.
- **Understand the limits**: Always be aware of Google's quotas, especially when running large scripts that edit thousands of cells.