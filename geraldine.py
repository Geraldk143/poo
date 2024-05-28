# from flask import Flask

# app = Flask(__name__)

class web_app():
    def __init__(self):
        return 

    @staticmethod
    def generate_bank_website():
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document Management and Bill Payment Tracker</title>
        </head>
        <body>
            <h1>Welcome to Your Document Management and Bill Payment Tracker</h1>
            <img src="https://images.unsplash.com/photo-1517430816045-df4b7de11d1d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzNjUyOXwwfDF8c2VhcmNofDJ8fGRlc2t8ZW58MHx8fHwxNjI4MDg1ODkz&ixlib=rb-1.2.1&q=80&w=400" width="320" height="240" alt="Organized Desk with Documents">
            <h3>Manage your bills, receipts, and financial documents with ease.</h3>
            
            <!-- Sign Up Form -->
            <h4>Sign Up</h4>
            <form action="/signup" method="post">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                
                <label for="chatbox">Do you need chatbox service for customer support?</label><br>
                <input type="checkbox" id="chatbox" name="chatbox_service" value="yes"><br>
                
                <label for="upload_receipts">Do you want to upload receipts for bill payments?</label><br>
                <input type="checkbox" id="upload_receipts" name="upload_receipts" value="yes"><br>
                
                <label for="report_frequency">How often do you want to receive reports?</label><br>
                <select id="report_frequency" name="report_frequency">
                    <option value="monthly">Monthly</option>
                    <option value="quarterly">Quarterly</option>
                    <option value="yearly">Yearly</option>
                    <option value="never">Never</option>
                </select><br>
                
            </form>
            
            <!-- Document Upload Form -->
            <h4>Upload Documents</h4>
            <form action="/upload_document" method="post" enctype="multipart/form-data">
                <input type="file" name="document" accept=".pdf,.doc,.docx,.txt" required><br>
                <input type="text" name="category" placeholder="Category" required><br>
                <input type="submit" value="Upload Document">
            </form>
            
            <!-- Receipt Upload Form -->
            <h4>Upload Receipts</h4>
            <form action="/upload_receipt" method="post" enctype="multipart/form-data">
                <input type="file" name="receipt" accept=".pdf,.jpg,.jpeg,.png" required><br>
                <input type="text" name="bill_name" placeholder="Bill Name" required><br>
                <input type="submit" value="Upload Receipt">
            </form>
            
            <!-- Document Organization -->
            <h4>Organize Documents</h4>
            <form action="/organize_documents" method="post">
                <label for="sort_by">Sort By:</label>
                <select id="sort_by" name="sort_by">
                    <option value="date">Date</option>
                    <option value="category">Category</option>
                    <option value="name">Name</option>
                </select><br>
                <input type="submit" value="Organize Documents">
            </form>
            
            <!-- Sign In Form -->
            <h4>Sign In</h4>
            <form action="/signin" method="post">
                <input type="text" name="username" placeholder="Username" required><br>
                <input type="password" name="password" placeholder="Password" required><br>
                <input type="submit" value="Sign In">
            </form>
        </body>
        </html>

        """
        return html_content

    @staticmethod
    def save_html_to_file(html_content, filename='C://Users//geral//mom//bank_website.html'):
        with open(filename, 'w') as file:
            file.write(html_content)
        print(f"HTML content saved to '{filename}'")

html_content = web_app.generate_bank_website()
web_app.save_html_to_file(html_content)

if __name__ == '__main__':
    william = web_app()
    run= william.generate_bank_website
    run2 =william.save_html_to_file

# github user: william.ngeow@gmail.com
# github pw: dennis291252@
# Same as render