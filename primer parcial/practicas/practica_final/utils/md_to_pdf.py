import os
import markdown2
import pdfkit
from pathlib import Path

# Add this at the top of the file after imports
WKHTMLTOPDF_PATH = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)

def list_markdown_files(directory):
    """List all markdown files in the given directory and subdirectories"""
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                # Store full path and display path
                full_path = os.path.join(root, file)
                display_path = os.path.relpath(full_path, directory)
                markdown_files.append((display_path, full_path))
    return markdown_files

def convert_to_pdf(markdown_file, output_file):
    """Convert markdown file to PDF"""
    try:
        with open(markdown_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        # Convert markdown to HTML with math support
        html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables'])
        
        # Replace LaTeX delimiters for MathJax
        html_content = html_content.replace('$$', '$')
        
        styled_html = f"""
        <html>
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
                <script type="text/javascript" async
                    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
                </script>
                <script type="text/x-mathjax-config">
                    MathJax.Hub.Config({{
                        tex2jax: {{
                            inlineMath: [['$','$']],
                            displayMath: [['$$','$$']],
                            processEscapes: true
                        }}
                    }});
                </script>
                <style>
                    body {{ 
                        font-family: Arial, sans-serif; 
                        margin: 40px;
                    }}
                    code {{ 
                        background-color: #f4f4f4; 
                        padding: 2px 5px; 
                    }}
                    pre {{ 
                        background-color: #f4f4f4; 
                        padding: 10px; 
                    }}
                </style>
            </head>
            <body>
                {html_content}
            </body>
        </html>
        """
        
        # Add options for better PDF rendering
        options = {
            'encoding': 'UTF-8',
            'enable-local-file-access': None,
            'javascript-delay': 1000,  # Wait for MathJax to render
            'no-stop-slow-scripts': None,
            'enable-javascript': None
        }
        
        pdfkit.from_string(styled_html, output_file, options=options, configuration=config)
        return True
    except Exception as e:
        print(f"Error converting file: {e}")
        return False

def main():
    while True:
        print("\n=== Markdown to PDF Converter ===")
        print("1. Convert a markdown file")
        print("2. Exit")
        
        choice = input("\nEnter your choice (1-2): ")
        
        if choice == '2':
            print("Goodbye!")
            break
        
        elif choice == '1':
            # Get current directory
            current_dir = os.getcwd()
            
            # List markdown files
            markdown_files = list_markdown_files(current_dir)
            
            if not markdown_files:
                print("\nNo markdown files found in any directory!")
                continue
            
            print("\nAvailable markdown files:")
            for i, (display_path, _) in enumerate(markdown_files, 1):
                print(f"{i}. {display_path}")
            
            try:
                file_choice = int(input("\nEnter the number of the file to convert: "))
                if 1 <= file_choice <= len(markdown_files):
                    selected_display_path, selected_full_path = markdown_files[file_choice - 1]
                    output_file = os.path.splitext(selected_full_path)[0] + '.pdf'
                    
                    print(f"\nConverting {selected_display_path} to PDF...")
                    if convert_to_pdf(selected_full_path, output_file):
                        print("Conversion successful!")
                    else:
                        print("Conversion failed!")
                else:
                    print("Invalid file number!")
            except ValueError:
                print("Please enter a valid number!")
        
        else:
            print("Invalid choice! Please enter 1 or 2.")

if __name__ == "__main__":
    main()