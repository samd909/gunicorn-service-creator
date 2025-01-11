import os

project_name = input("Your django project name: ")
document_root = input("Enter the document root path (Dont add a / at the end make it like this '/var/www/Praktijk-Jobs/praktijkjobs'): ")

output_directory = os.getcwd()

filename = os.path.join(output_directory, f"{project_name.lower()}-gunicorn.service")

with open(filename, "w") as file:
    file.write(f"""
[Unit]
Description=Gunicorn daemon for {project_name} Django project
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory={document_root}
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:{document_root}/{project_name.lower()}.sock {project_name.lower()}.wsgi:application --access-logfile {document_root}/gunicorn-access.log --error-logfile {document_root}/gunicorn-error.log

[Install]
WantedBy=multi-user.target
""")

print(f"Service file '{filename}' created successfully in the directory: {output_directory}")
